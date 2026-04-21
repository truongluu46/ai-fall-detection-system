from pathlib import Path

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from backend.app.core.config import settings
from backend.app.utils.file_storage import ensure_storage_dirs


def main() -> None:
    ensure_storage_dirs()

    rng = np.random.default_rng(42)

    # features:
    # aspect_ratio, torso_angle_deg, center_y, mean_visibility,
    # shoulder_width, hip_width, width, height
    n = 600

    not_fall = np.column_stack(
        [
            rng.normal(0.55, 0.12, n),
            rng.normal(82, 9, n),
            rng.normal(0.50, 0.08, n),
            rng.normal(0.90, 0.05, n),
            rng.normal(0.15, 0.03, n),
            rng.normal(0.14, 0.03, n),
            rng.normal(0.20, 0.04, n),
            rng.normal(0.38, 0.06, n),
        ]
    )

    fall = np.column_stack(
        [
            rng.normal(1.35, 0.20, n),
            rng.normal(22, 12, n),
            rng.normal(0.68, 0.10, n),
            rng.normal(0.83, 0.07, n),
            rng.normal(0.22, 0.04, n),
            rng.normal(0.20, 0.04, n),
            rng.normal(0.42, 0.08, n),
            rng.normal(0.25, 0.05, n),
        ]
    )

    X = np.vstack([not_fall, fall]).astype(np.float32)
    y = np.array(["not_fall"] * len(not_fall) + ["fall"] * len(fall))

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=8,
        random_state=42,
        class_weight="balanced",
    )
    model.fit(X, y)

    output_path = settings.model_file_path_abs
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_path)

    print(f"Saved mock model to: {output_path}")


if __name__ == "__main__":
    main()
