from backend.app.core.constants import CameraSourceType
from backend.app.ai.inference import InferencePipeline


class WebcamCamera:
    source_type = CameraSourceType.WEBCAM
    source_url = None
    source_path = None


def main() -> None:
    pipeline = InferencePipeline()
    camera = WebcamCamera()
    result = pipeline.process_source(camera)
    print(result)


if __name__ == "__main__":
    main()
