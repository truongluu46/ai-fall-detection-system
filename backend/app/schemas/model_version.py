from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from backend.app.schemas.common import ORMBase


class ModelVersionBase(BaseModel):
    model_name: str
    version: str
    algorithm: str
    pose_backend: str
    feature_schema_version: Optional[str] = None
    accuracy: Optional[float] = None
    precision_score: Optional[float] = None
    recall_score: Optional[float] = None
    f1_score: Optional[float] = None
    file_path: str
    is_active: bool = False
    trained_at: Optional[datetime] = None


class ModelVersionCreate(ModelVersionBase):
    pass


class ModelVersionUpdate(BaseModel):
    model_name: Optional[str] = None
    version: Optional[str] = None
    algorithm: Optional[str] = None
    pose_backend: Optional[str] = None
    feature_schema_version: Optional[str] = None
    accuracy: Optional[float] = None
    precision_score: Optional[float] = None
    recall_score: Optional[float] = None
    f1_score: Optional[float] = None
    file_path: Optional[str] = None
    is_active: Optional[bool] = None
    trained_at: Optional[datetime] = None


class ModelVersionRead(ModelVersionBase, ORMBase):
    id: int
    created_at: datetime
