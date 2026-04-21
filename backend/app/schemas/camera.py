from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator

from backend.app.core.constants import CameraSourceType, CameraStatus
from backend.app.schemas.common import ORMBase


class CameraBase(BaseModel):
    name: str
    location: Optional[str] = None
    source_type: CameraSourceType
    source_url: Optional[str] = None
    source_path: Optional[str] = None
    status: CameraStatus = CameraStatus.INACTIVE
    description: Optional[str] = None
    fps: Optional[int] = None

    @field_validator("source_url")
    @classmethod
    def normalize_source_url(cls, value: Optional[str]) -> Optional[str]:
        return value.strip() if value else value

    @field_validator("source_path")
    @classmethod
    def normalize_source_path(cls, value: Optional[str]) -> Optional[str]:
        return value.strip() if value else value


class CameraCreate(CameraBase):
    pass


class CameraUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    source_type: Optional[CameraSourceType] = None
    source_url: Optional[str] = None
    source_path: Optional[str] = None
    status: Optional[CameraStatus] = None
    description: Optional[str] = None
    fps: Optional[int] = None


class CameraRead(CameraBase, ORMBase):
    id: int
    last_seen_at: Optional[datetime] = None
    created_by: Optional[int] = None
    created_at: datetime
    updated_at: datetime
