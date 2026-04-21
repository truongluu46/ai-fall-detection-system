from backend.app.ai.inference import InferencePipeline


def main() -> None:
    pipeline = InferencePipeline()
    path = input("Nhap duong dan video: ").strip()
    result = pipeline.process_video_file(path)
    print(result)


if __name__ == "__main__":
    main()
