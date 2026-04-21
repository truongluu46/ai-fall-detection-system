from __future__ import annotations

from dataclasses import dataclass

from backend.app.ai.classifier import FallClassifier
from backend.app.ai.feature_extractor import FeatureExtractor
from backend.app.ai.pose_estimator import PoseEstimator
from backend.app.ai.video_reader import VideoReader
from backend.app.core.config import settings
from backend.app.core.constants import CameraSourceType
from backend.app.utils.file_storage import save_snapshot


@dataclass
class InferenceResult:
    fall_detected: bool
    confidence_score: float
    snapshot_path: str | None
    processed_frames: int
    total_frames: int
    sampled_frames: int
    best_frame_index: int | None
    error_message: str | None
    video_path: str | None = None


class InferencePipeline:
    def __init__(self) -> None:
        self.reader = VideoReader()
        self.pose_estimator = PoseEstimator()
        self.feature_extractor = FeatureExtractor()
        self.classifier = FallClassifier()

    def _run_capture(self, source) -> dict:
        cap = self.reader.open(source)
        if not cap or not cap.isOpened():
            return InferenceResult(
                fall_detected=False,
                confidence_score=0.0,
                snapshot_path=None,
                processed_frames=0,
                total_frames=0,
                sampled_frames=0,
                best_frame_index=None,
                error_message=f"Cannot open source: {source}",
            ).__dict__

        meta = self.reader.meta(cap)
        frame_idx = 0
        processed_frames = 0
        sampled_frames = 0
        best_frame_idx = None
        best_conf = 0.0
        best_snapshot_path = None

        while True:
            ok, frame = cap.read()
            if not ok:
                break

            if frame_idx >= settings.max_frames_to_process:
                break

            processed_frames += 1
            if frame_idx % settings.sample_every_n_frames == 0:
                sampled_frames += 1
                landmarks = self.pose_estimator.estimate(frame)
                if landmarks:
                    features = self.feature_extractor.extract(landmarks)
                    if features is not None:
                        label, conf = self.classifier.predict(features)
                        if label == "fall" and conf > best_conf:
                            best_conf = conf
                            best_frame_idx = frame_idx
                            best_snapshot_path = save_snapshot(frame, prefix="fall")
            frame_idx += 1

        cap.release()

        fall_detected = best_conf >= settings.fall_confidence_threshold
        if not fall_detected:
            best_snapshot_path = None

        return InferenceResult(
            fall_detected=fall_detected,
            confidence_score=round(best_conf, 4),
            snapshot_path=best_snapshot_path,
            processed_frames=processed_frames,
            total_frames=meta.total_frames or processed_frames,
            sampled_frames=sampled_frames,
            best_frame_index=best_frame_idx,
            error_message=None,
        ).__dict__

    def process_video_file(self, video_path: str) -> dict:
        result = self._run_capture(video_path)
        result["video_path"] = video_path
        return result

    def process_source(self, camera) -> dict:
        if camera.source_type == CameraSourceType.WEBCAM:
            source = 0
        else:
            source = camera.source_url or camera.source_path
        return self._run_capture(source)
