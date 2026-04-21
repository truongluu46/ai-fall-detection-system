from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.core.constants import ProcessingRunStatus
from backend.app.models.base import Base


class ProcessingRun(Base):
    __tablename__ = "processing_runs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    camera_id: Mapped[Optional[int]] = mapped_column(ForeignKey("cameras.id", ondelete="SET NULL"), nullable=True, index=True)
    model_version_id: Mapped[Optional[int]] = mapped_column(ForeignKey("model_versions.id", ondelete="SET NULL"), nullable=True, index=True)
    triggered_by: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    input_type: Mapped[str] = mapped_column(String(30), nullable=False)
    input_path: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    run_status: Mapped[ProcessingRunStatus] = mapped_column(
        Enum(ProcessingRunStatus, native_enum=False),
        default=ProcessingRunStatus.QUEUED,
        nullable=False,
        index=True,
    )
    started_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False), nullable=True)
    ended_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False), nullable=True)
    total_frames: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    processed_frames: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False)
