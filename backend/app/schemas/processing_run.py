from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from backend.app.core.constants import ProcessingRunStatus
from backend.app.schemas.common import ORMBase


class ProcessingRunBase(BaseModel):
    camera_id: Optional[int] = None
    model_version_id: Optional[int] = None
    input_type: str
    input_path: Optional[str] = None
    run_status: ProcessingRunStatus = ProcessingRunStatus.QUEUED


class ProcessingRunCreate(ProcessingRunBase):
    pass


class ProcessingRunUpdate(BaseModel):
    run_status: Optional[ProcessingRunStatus] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    total_frames: Optional[int] = None
    processed_frames: Optional[int] = None
    error_message: Optional[str] = None
    model_version_id: Optional[int] = None


class ProcessingRunRead(ProcessingRunBase, ORMBase):
    id: int
    triggered_by: Optional[int] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    total_frames: Optional[int] = None
    processed_frames: Optional[int] = None
    error_message: Optional[str] = None
    created_at: datetime


class VideoProcessResponse(BaseModel):
    processing_run: ProcessingRunRead
    fall_detected: bool
    confidence_score: float
    event_id: Optional[int] = None
    snapshot_path: Optional[str] = None
    video_path: Optional[str] = None
    processed_frames: int
    total_frames: int
    sampled_frames: int
    best_frame_index: Optional[int] = None
