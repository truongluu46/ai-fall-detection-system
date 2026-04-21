from pathlib import Path
from typing import Any

import joblib

from backend.app.core.config import settings


class ModelLoader:
    def __init__(self, model_path: Path | None = None) -> None:
        self.model_path = model_path or settings.model_file_path_abs
        self._cached_model: Any | None = None

    def exists(self) -> bool:
        return self.model_path.exists()

    def load(self):
        if not self.model_path.exists():
            return None
        if self._cached_model is None:
            self._cached_model = joblib.load(self.model_path)
        return self._cached_model
