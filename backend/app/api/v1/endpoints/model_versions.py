from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.api.deps import get_db_session
from backend.app.repositories.model_version_repository import ModelVersionRepository
from backend.app.schemas.model_version import ModelVersionCreate, ModelVersionRead, ModelVersionUpdate
from backend.app.services.model_version_service import ModelVersionService

router = APIRouter(prefix="/model-versions", tags=["model_versions"])


def get_service(db: Session) -> ModelVersionService:
    return ModelVersionService(ModelVersionRepository(db))


@router.get("", response_model=list[ModelVersionRead])
def list_model_versions(db: Session = Depends(get_db_session)):
    return get_service(db).list_model_versions()


@router.post("", response_model=ModelVersionRead, status_code=status.HTTP_201_CREATED)
def create_model_version(payload: ModelVersionCreate, db: Session = Depends(get_db_session)):
    return get_service(db).create_model_version(payload)


@router.get("/active", response_model=ModelVersionRead | None)
def get_active_model_version(db: Session = Depends(get_db_session)):
    return get_service(db).get_active_model_version()


@router.patch("/{model_version_id}", response_model=ModelVersionRead)
def update_model_version(model_version_id: int, payload: ModelVersionUpdate, db: Session = Depends(get_db_session)):
    item = get_service(db).update_model_version(model_version_id, payload)
    if not item:
        raise HTTPException(status_code=404, detail="Model version not found")
    return item
