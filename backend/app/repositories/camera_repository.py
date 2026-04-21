from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.models.camera import Camera
from backend.app.schemas.camera import CameraCreate, CameraUpdate


class CameraRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list(self) -> list[Camera]:
        stmt = select(Camera).order_by(Camera.id.desc())
        return list(self.db.scalars(stmt).all())

    def get(self, camera_id: int) -> Camera | None:
        return self.db.get(Camera, camera_id)

    def create(self, payload: CameraCreate) -> Camera:
        camera = Camera(**payload.model_dump())
        self.db.add(camera)
        self.db.commit()
        self.db.refresh(camera)
        return camera

    def update(self, camera: Camera, payload: CameraUpdate) -> Camera:
        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(camera, field, value)
        self.db.commit()
        self.db.refresh(camera)
        return camera

    def delete(self, camera: Camera) -> None:
        self.db.delete(camera)
        self.db.commit()
