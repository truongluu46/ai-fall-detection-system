from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.core.constants import FallEventStatus
from backend.app.models.base import Base, TimestampMixin


class FallEvent(Base, TimestampMixin):
    __tablename__ = "fall_events"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    camera_id: Mapped[int] = mapped_column(ForeignKey("cameras.id", ondelete="RESTRICT"), nullable=False, index=True)
    processing_run_id: Mapped[Optional[int]] = mapped_column(ForeignKey("processing_runs.id", ondelete="SET NULL"), nullable=True, index=True)
    model_version_id: Mapped[Optional[int]] = mapped_column(ForeignKey("model_versions.id", ondelete="SET NULL"), nullable=True, index=True)
    event_time: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False, index=True)
    confidence_score: Mapped[float] = mapped_column(Numeric(5, 4), nullable=False)
    status: Mapped[FallEventStatus] = mapped_column(
        Enum(FallEventStatus, native_enum=False),
        default=FallEventStatus.NEW,
        nullable=False,
        index=True,
    )
    snapshot_path: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    video_path: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    frame_index: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    reviewed_by: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    reviewed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False), nullable=True)
    review_note: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
