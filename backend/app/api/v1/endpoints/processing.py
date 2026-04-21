from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from backend.app.api.deps import get_db_session
from backend.app.schemas.processing_run import VideoProcessResponse
from backend.app.services.processing_service import ProcessingService

router = APIRouter(prefix="/processing", tags=["processing"])


@router.post("/upload-video", response_model=VideoProcessResponse)
def process_uploaded_video(
    file: UploadFile = File(...),
    camera_id: int | None = Form(default=None),
    model_version_id: int | None = Form(default=None),
    db: Session = Depends(get_db_session),
):
    service = ProcessingService(db)
    result = service.process_uploaded_video(file=file, camera_id=camera_id, model_version_id=model_version_id)
    return result


@router.post("/from-camera/{camera_id}", response_model=VideoProcessResponse)
def process_from_camera(
    camera_id: int,
    model_version_id: int | None = None,
    db: Session = Depends(get_db_session),
):
    service = ProcessingService(db)
    try:
        result = service.process_from_camera(camera_id=camera_id, model_version_id=model_version_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return result
