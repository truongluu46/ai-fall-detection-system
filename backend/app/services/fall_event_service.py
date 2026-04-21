from datetime import datetime

from backend.app.core.constants import FallEventStatus
from backend.app.repositories.fall_event_repository import FallEventRepository
from backend.app.schemas.fall_event import FallEventCreate, FallEventStatusUpdate


class FallEventService:
    def __init__(self, repo: FallEventRepository) -> None:
        self.repo = repo

    def list_events(self):
        return self.repo.list()

    def get_event(self, event_id: int):
        return self.repo.get(event_id)

    def create_event(self, payload: FallEventCreate):
        return self.repo.create(payload)

    def update_status(self, event_id: int, payload: FallEventStatusUpdate):
        event = self.repo.get(event_id)
        if not event:
            return None

        event.status = payload.status
        event.review_note = payload.review_note
        event.reviewed_by = payload.reviewed_by
        event.reviewed_at = datetime.utcnow()

        if payload.status == FallEventStatus.NEW:
            event.reviewed_at = None

        return self.repo.save(event)
