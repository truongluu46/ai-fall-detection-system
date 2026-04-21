from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, DateTime, Numeric, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.models.base import Base


class ModelVersion(Base):
    __tablename__ = "model_versions"
    __table_args__ = (
        UniqueConstraint("model_name", "version", name="uq_model_versions_name_version"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    model_name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    version: Mapped[str] = mapped_column(String(50), nullable=False)
    algorithm: Mapped[str] = mapped_column(String(100), nullable=False)
    pose_backend: Mapped[str] = mapped_column(String(100), nullable=False)
    feature_schema_version: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    accuracy: Mapped[Optional[float]] = mapped_column(Numeric(5, 4), nullable=True)
    precision_score: Mapped[Optional[float]] = mapped_column(Numeric(5, 4), nullable=True)
    recall_score: Mapped[Optional[float]] = mapped_column(Numeric(5, 4), nullable=True)
    f1_score: Mapped[Optional[float]] = mapped_column(Numeric(5, 4), nullable=True)
    file_path: Mapped[str] = mapped_column(Text, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, index=True)
    trained_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False)
