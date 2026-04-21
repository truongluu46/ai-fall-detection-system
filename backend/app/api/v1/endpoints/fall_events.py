from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.api.deps import get_db_session
from backend.app.repositories.fall_event_repository import FallEventRepository
from backend.app.schemas.fall_event import FallEventCreate, FallEventRead, FallEventStatusUpdate
from backend.app.services.fall_event_service import FallEventService

router = APIRouter(prefix="/fall-events", tags=["fall_events"])


def get_service(db: Session) -> FallEventService:
    return FallEventService(FallEventRepository(db))


@router.get("", response_model=list[FallEventRead])
def list_fall_events(db: Session = Depends(get_db_session)):
    return get_service(db).list_events()


@router.post("", response_model=FallEventRead, status_code=status.HTTP_201_CREATED)
def create_fall_event(payload: FallEventCreate, db: Session = Depends(get_db_session)):
    return get_service(db).create_event(payload)


@router.get("/{event_id}", response_model=FallEventRead)
def get_fall_event(event_id: int, db: Session = Depends(get_db_session)):
    event = get_service(db).get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Fall event not found")
    return event


@router.patch("/{event_id}/status", response_model=FallEventRead)
def update_fall_event_status(event_id: int, payload: FallEventStatusUpdate, db: Session = Depends(get_db_session)):
    event = get_service(db).update_status(event_id, payload)
    if not event:
        raise HTTPException(status_code=404, detail="Fall event not found")
    return event
