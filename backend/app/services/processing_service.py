from datetime import datetime
from pathlib import Path

from fastapi import UploadFile
from sqlalchemy.orm import Session

from backend.app.ai.inference import InferencePipeline
from backend.app.core.constants import ProcessingRunStatus
from backend.app.models.camera import Camera
from backend.app.repositories.fall_event_repository import FallEventRepository
from backend.app.repositories.model_version_repository import ModelVersionRepository
from backend.app.repositories.processing_run_repository import ProcessingRunRepository
from backend.app.schemas.fall_event import FallEventCreate
from backend.app.schemas.processing_run import ProcessingRunCreate, ProcessingRunUpdate
from backend.app.utils.file_storage import save_uploaded_file


class ProcessingService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.run_repo = ProcessingRunRepository(db)
        self.event_repo = FallEventRepository(db)
        self.model_repo = ModelVersionRepository(db)
        self.pipeline = InferencePipeline()

    def _resolve_camera_or_raise(self, camera_id: int) -> Camera:
        camera = self.db.get(Camera, camera_id)
        if not camera:
            raise ValueError(f"Camera {camera_id} not found")
        return camera

    def process_uploaded_video(self, *, file: UploadFile, camera_id: int | None = None, model_version_id: int | None = None):
        saved_path = save_uploaded_file(file)

        active_model = self.model_repo.get(model_version_id) if model_version_id else self.model_repo.get_active()
        run = self.run_repo.create(
            ProcessingRunCreate(
                camera_id=camera_id,
                model_version_id=active_model.id if active_model else model_version_id,
                input_type="video_file",
                input_path=str(saved_path),
                run_status=ProcessingRunStatus.QUEUED,
            )
        )

        self.run_repo.update(
            run,
            ProcessingRunUpdate(
                run_status=ProcessingRunStatus.PROCESSING,
                started_at=datetime.utcnow(),
            ),
        )

        result = self.pipeline.process_video_file(str(saved_path))

        run = self.run_repo.update(
            run,
            ProcessingRunUpdate(
                run_status=ProcessingRunStatus.COMPLETED if not result["error_message"] else ProcessingRunStatus.FAILED,
                ended_at=datetime.utcnow(),
                total_frames=result["total_frames"],
                processed_frames=result["processed_frames"],
                error_message=result["error_message"],
            ),
        )

        event_id = None
        if result["fall_detected"]:
            resolved_camera_id = camera_id or 1
            event = self.event_repo.create(
                FallEventCreate(
                    camera_id=resolved_camera_id,
                    processing_run_id=run.id,
                    model_version_id=active_model.id if active_model else None,
                    event_time=datetime.utcnow(),
                    confidence_score=result["confidence_score"],
                    snapshot_path=result["snapshot_path"],
                    video_path=str(saved_path),
                    frame_index=result["best_frame_index"],
                )
            )
            event_id = event.id

        return {
            "processing_run": run,
            "event_id": event_id,
            **result,
            "video_path": str(saved_path),
        }

    def process_from_camera(self, *, camera_id: int, model_version_id: int | None = None):
        camera = self._resolve_camera_or_raise(camera_id)

        input_path = camera.source_url or camera.source_path or str(camera_id)
        input_type = camera.source_type.value

        active_model = self.model_repo.get(model_version_id) if model_version_id else self.model_repo.get_active()
        run = self.run_repo.create(
            ProcessingRunCreate(
                camera_id=camera_id,
                model_version_id=active_model.id if active_model else model_version_id,
                input_type=input_type,
                input_path=input_path,
                run_status=ProcessingRunStatus.QUEUED,
            )
        )

        self.run_repo.update(
            run,
            ProcessingRunUpdate(
                run_status=ProcessingRunStatus.PROCESSING,
                started_at=datetime.utcnow(),
            ),
        )

        result = self.pipeline.process_source(camera)

        run = self.run_repo.update(
            run,
            ProcessingRunUpdate(
                run_status=ProcessingRunStatus.COMPLETED if not result["error_message"] else ProcessingRunStatus.FAILED,
                ended_at=datetime.utcnow(),
                total_frames=result["total_frames"],
                processed_frames=result["processed_frames"],
                error_message=result["error_message"],
            ),
        )

        event_id = None
        if result["fall_detected"]:
            event = self.event_repo.create(
                FallEventCreate(
                    camera_id=camera_id,
                    processing_run_id=run.id,
                    model_version_id=active_model.id if active_model else None,
                    event_time=datetime.utcnow(),
                    confidence_score=result["confidence_score"],
                    snapshot_path=result["snapshot_path"],
                    video_path=result.get("video_path"),
                    frame_index=result["best_frame_index"],
                )
            )
            event_id = event.id

        return {
            "processing_run": run,
            "event_id": event_id,
            **result,
        }
