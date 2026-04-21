from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator

from backend.app.core.constants import FallEventStatus
from backend.app.schemas.common import ORMBase


class FallEventBase(BaseModel):
    camera_id: int
    processing_run_id: Optional[int] = None
    model_version_id: Optional[int] = None
    event_time: datetime
    confidence_score: float
    status: FallEventStatus = FallEventStatus.NEW
    snapshot_path: Optional[str] = None
    video_path: Optional[str] = None
    frame_index: Optional[int] = None
    review_note: Optional[str] = None

    @field_validator("confidence_score")
    @classmethod
    def validate_confidence(cls, value: float) -> float:
        if not 0 <= value <= 1:
            raise ValueError("confidence_score must be between 0 and 1")
        return value


class FallEventCreate(FallEventBase):
    pass


class FallEventStatusUpdate(BaseModel):
    status: FallEventStatus
    review_note: Optional[str] = None
    reviewed_by: Optional[int] = None


class FallEventRead(FallEventBase, ORMBase):
    id: int
    reviewed_by: Optional[int] = None
    reviewed_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
