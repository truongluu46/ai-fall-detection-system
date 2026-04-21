from sqlalchemy import select, update
from sqlalchemy.orm import Session

from backend.app.models.model_version import ModelVersion
from backend.app.schemas.model_version import ModelVersionCreate, ModelVersionUpdate


class ModelVersionRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list(self) -> list[ModelVersion]:
        stmt = select(ModelVersion).order_by(ModelVersion.id.desc())
        return list(self.db.scalars(stmt).all())

    def get(self, model_version_id: int) -> ModelVersion | None:
        return self.db.get(ModelVersion, model_version_id)

    def get_active(self) -> ModelVersion | None:
        stmt = select(ModelVersion).where(ModelVersion.is_active.is_(True)).order_by(ModelVersion.id.desc())
        return self.db.scalars(stmt).first()

    def create(self, payload: ModelVersionCreate) -> ModelVersion:
        if payload.is_active:
            self.db.execute(update(ModelVersion).values(is_active=False))
        model_version = ModelVersion(**payload.model_dump(), created_at=payload.trained_at or __import__("datetime").datetime.utcnow())
        self.db.add(model_version)
        self.db.commit()
        self.db.refresh(model_version)
        return model_version

    def update(self, model_version: ModelVersion, payload: ModelVersionUpdate) -> ModelVersion:
        data = payload.model_dump(exclude_unset=True)
        if data.get("is_active") is True:
            self.db.execute(update(ModelVersion).values(is_active=False))
        for field, value in data.items():
            setattr(model_version, field, value)
        self.db.commit()
        self.db.refresh(model_version)
        return model_version
