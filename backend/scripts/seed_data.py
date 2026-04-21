from datetime import datetime

from sqlalchemy import select

from backend.app.core.constants import CameraSourceType, CameraStatus
from backend.app.core.database import SessionLocal
from backend.app.models.camera import Camera
from backend.app.models.model_version import ModelVersion


def main() -> None:
    db = SessionLocal()
    try:
        if not db.scalars(select(Camera).where(Camera.name == "Laptop Webcam")).first():
            db.add(
                Camera(
                    name="Laptop Webcam",
                    location="Demo Room",
                    source_type=CameraSourceType.WEBCAM,
                    status=CameraStatus.ACTIVE,
                    description="Nguồn webcam để test MVP",
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                )
            )

        if not db.scalars(select(ModelVersion).where(ModelVersion.version == "v1.0.0")).first():
            db.add(
                ModelVersion(
                    model_name="fall_detector",
                    version="v1.0.0",
                    algorithm="random_forest",
                    pose_backend="mediapipe_pose",
                    feature_schema_version="v1",
                    accuracy=0.9000,
                    precision_score=0.8800,
                    recall_score=0.8600,
                    f1_score=0.8700,
                    file_path="storage/models/fall_detector_v1.pkl",
                    is_active=True,
                    trained_at=datetime.utcnow(),
                    created_at=datetime.utcnow(),
                )
            )

        db.commit()
        print("Seed data inserted successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
