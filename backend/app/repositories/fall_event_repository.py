from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.models.fall_event import FallEvent
from backend.app.schemas.fall_event import FallEventCreate


class FallEventRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list(self) -> list[FallEvent]:
        stmt = select(FallEvent).order_by(FallEvent.id.desc())
        return list(self.db.scalars(stmt).all())

    def get(self, event_id: int) -> FallEvent | None:
        return self.db.get(FallEvent, event_id)

    def create(self, payload: FallEventCreate) -> FallEvent:
        event = FallEvent(**payload.model_dump())
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event

    def save(self, event: FallEvent) -> FallEvent:
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event
