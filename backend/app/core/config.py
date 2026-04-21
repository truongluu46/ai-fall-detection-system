import os
from functools import lru_cache
from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Fall Detection API"
    app_env: str = "development"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"
    host: str = "0.0.0.0"
    port: int = 8000

    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/fall_detection_db"

    media_root: str = "storage"
    snapshot_dir: str = "storage/snapshots"
    video_dir: str = "storage/videos"
    model_dir: str = "storage/models"
    model_file_path: str = "storage/models/fall_detector_v1.pkl"

    fall_confidence_threshold: float = 0.60
    sample_every_n_frames: int = 5
    max_frames_to_process: int = 900

    cors_allow_origins: list[str] = ["*"]

    @field_validator("fall_confidence_threshold")
    @classmethod
    def validate_threshold(cls, value: float) -> float:
        if not 0 <= value <= 1:
            raise ValueError("fall_confidence_threshold must be between 0 and 1")
        return value

    @property
    def snapshot_dir_path(self) -> Path:
        return BASE_DIR / self.snapshot_dir

    @property
    def video_dir_path(self) -> Path:
        return BASE_DIR / self.video_dir

    @property
    def model_dir_path(self) -> Path:
        return BASE_DIR / self.model_dir

    @property
    def model_file_path_abs(self) -> Path:
        return BASE_DIR / self.model_file_path

    @staticmethod
    def get_app_port() -> int:
        return os.environ.get("PORT", 8000)

    @staticmethod
    def get_app_host() -> str:
        return os.environ.get("HOST", "127.0.0.1")

    @staticmethod
    def get_db_url() -> str:
        return os.environ.get("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/fall_detection_db")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
