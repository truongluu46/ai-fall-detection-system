from dataclasses import dataclass

import cv2


@dataclass
class VideoMeta:
    fps: float
    total_frames: int


class VideoReader:
    def open(self, source: str | int):
        cap = cv2.VideoCapture(source)
        return cap

    def meta(self, cap) -> VideoMeta:
        fps = cap.get(cv2.CAP_PROP_FPS) or 0.0
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
        return VideoMeta(fps=fps, total_frames=total_frames)
