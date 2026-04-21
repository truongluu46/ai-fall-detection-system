from __future__ import annotations

from typing import Optional

import cv2

try:
    import mediapipe as mp
except Exception:  # pragma: no cover - import error is handled gracefully at runtime
    mp = None


class PoseEstimator:
    def __init__(self) -> None:
        self.available = mp is not None
        self._pose = None
        if self.available:
            self._pose = mp.solutions.pose.Pose(
                static_image_mode=False,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5,
                model_complexity=1,
            )

    def estimate(self, frame_bgr) -> Optional[list[tuple[float, float, float, float]]]:
        if not self.available or self._pose is None:
            return None

        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        result = self._pose.process(frame_rgb)
        if not result.pose_landmarks:
            return None

        landmarks = []
        for landmark in result.pose_landmarks.landmark:
            landmarks.append((landmark.x, landmark.y, landmark.z, landmark.visibility))
        return landmarks
