from __future__ import annotations

from typing import Any

import numpy as np

from backend.app.ai.model_loader import ModelLoader


class FallClassifier:
    def __init__(self, model_loader: ModelLoader | None = None) -> None:
        self.model_loader = model_loader or ModelLoader()

    def _heuristic_predict(self, features: np.ndarray) -> tuple[str, float]:
        aspect_ratio = float(features[0])
        torso_angle_deg = float(features[1])
        mean_visibility = float(features[3])

        if mean_visibility < 0.35:
            return "not_fall", 0.15

        if aspect_ratio > 1.20 and torso_angle_deg < 35:
            return "fall", 0.82
        if aspect_ratio > 0.95 and torso_angle_deg < 50:
            return "fall", 0.62
        return "not_fall", 0.10

    def predict(self, features: np.ndarray) -> tuple[str, float]:
        model: Any | None = self.model_loader.load()
        if model is None:
            return self._heuristic_predict(features)

        X = features.reshape(1, -1)
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(X)[0]
            classes = list(model.classes_)
            if "fall" in classes:
                fall_idx = classes.index("fall")
                fall_prob = float(proba[fall_idx])
                label = "fall" if fall_prob >= 0.5 else "not_fall"
                return label, fall_prob
        label = str(model.predict(X)[0])
        return label, 0.5 if label == "fall" else 0.1
