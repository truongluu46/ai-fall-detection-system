from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.api.deps import get_db_session
from backend.app.repositories.camera_repository import CameraRepository
from backend.app.schemas.camera import CameraCreate, CameraRead, CameraUpdate
from backend.app.schemas.common import MessageResponse
from backend.app.services.camera_service import CameraService

router = APIRouter(prefix="/cameras", tags=["cameras"])


def get_service(db: Session) -> CameraService:
    return CameraService(CameraRepository(db))


@router.get("", response_model=list[CameraRead])
def list_cameras(db: Session = Depends(get_db_session)):
    return get_service(db).list_cameras()


@router.post("", response_model=CameraRead, status_code=status.HTTP_201_CREATED)
def create_camera(payload: CameraCreate, db: Session = Depends(get_db_session)):
    return get_service(db).create_camera(payload)


@router.get("/{camera_id}", response_model=CameraRead)
def get_camera(camera_id: int, db: Session = Depends(get_db_session)):
    camera = get_service(db).get_camera(camera_id)
    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")
    return camera


@router.patch("/{camera_id}", response_model=CameraRead)
def update_camera(camera_id: int, payload: CameraUpdate, db: Session = Depends(get_db_session)):
    camera = get_service(db).update_camera(camera_id, payload)
    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")
    return camera


@router.delete("/{camera_id}", response_model=MessageResponse)
def delete_camera(camera_id: int, db: Session = Depends(get_db_session)):
    deleted = get_service(db).delete_camera(camera_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Camera not found")
    return MessageResponse(message="Camera deleted successfully")
