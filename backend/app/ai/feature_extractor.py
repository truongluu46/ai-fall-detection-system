from __future__ import annotations

import math
from typing import Sequence

import numpy as np


class FeatureExtractor:
    LEFT_SHOULDER = 11
    RIGHT_SHOULDER = 12
    LEFT_HIP = 23
    RIGHT_HIP = 24

    def extract(self, landmarks: Sequence[tuple[float, float, float, float]]) -> np.ndarray | None:
        if not landmarks:
            return None

        xs = np.array([lm[0] for lm in landmarks], dtype=np.float32)
        ys = np.array([lm[1] for lm in landmarks], dtype=np.float32)
        vis = np.array([lm[3] for lm in landmarks], dtype=np.float32)

        width = float(xs.max() - xs.min())
        height = float(ys.max() - ys.min())
        aspect_ratio = width / max(height, 1e-6)
        center_y = float(ys.mean())
        mean_visibility = float(vis.mean())

        ls = landmarks[self.LEFT_SHOULDER]
        rs = landmarks[self.RIGHT_SHOULDER]
        lh = landmarks[self.LEFT_HIP]
        rh = landmarks[self.RIGHT_HIP]

        shoulder_mid = ((ls[0] + rs[0]) / 2.0, (ls[1] + rs[1]) / 2.0)
        hip_mid = ((lh[0] + rh[0]) / 2.0, (lh[1] + rh[1]) / 2.0)

        dx = hip_mid[0] - shoulder_mid[0]
        dy = hip_mid[1] - shoulder_mid[1]
        torso_angle_deg = abs(math.degrees(math.atan2(dy, dx)))  # 0: ngang, 90: đứng

        shoulder_width = abs(ls[0] - rs[0])
        hip_width = abs(lh[0] - rh[0])

        return np.array(
            [
                aspect_ratio,
                torso_angle_deg,
                center_y,
                mean_visibility,
                shoulder_width,
                hip_width,
                width,
                height,
            ],
            dtype=np.float32,
        )
