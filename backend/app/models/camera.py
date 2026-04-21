from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.core.constants import CameraSourceType, CameraStatus
from backend.app.models.base import Base, TimestampMixin


class Camera(Base, TimestampMixin):
    __tablename__ = "cameras"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    location: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    source_type: Mapped[CameraSourceType] = mapped_column(
        Enum(CameraSourceType, native_enum=False),
        nullable=False,
    )
    source_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    source_path: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[CameraStatus] = mapped_column(
        Enum(CameraStatus, native_enum=False),
        default=CameraStatus.INACTIVE,
        nullable=False,
        index=True,
    )
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    fps: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    last_seen_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False), nullable=True)
    created_by: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
