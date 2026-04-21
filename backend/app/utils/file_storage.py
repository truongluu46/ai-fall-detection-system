from pathlib import Path
from uuid import uuid4

import cv2
from fastapi import UploadFile

from backend.app.core.config import settings


def ensure_storage_dirs() -> None:
    settings.snapshot_dir_path.mkdir(parents=True, exist_ok=True)
    settings.video_dir_path.mkdir(parents=True, exist_ok=True)
    settings.model_dir_path.mkdir(parents=True, exist_ok=True)


def save_uploaded_file(file: UploadFile) -> Path:
    ensure_storage_dirs()
    suffix = Path(file.filename or ".mp4").suffix or ".mp4"
    output_path = settings.video_dir_path / f"{uuid4().hex}{suffix}"

    with output_path.open("wb") as buffer:
        buffer.write(file.file.read())

    return output_path


def save_snapshot(frame, prefix: str = "fall") -> str | None:
    ensure_storage_dirs()
    output_path = settings.snapshot_dir_path / f"{prefix}_{uuid4().hex}.jpg"
    success = cv2.imwrite(str(output_path), frame)
    return str(output_path) if success else None
