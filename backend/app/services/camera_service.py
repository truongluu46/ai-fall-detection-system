from backend.app.repositories.camera_repository import CameraRepository
from backend.app.schemas.camera import CameraCreate, CameraUpdate


class CameraService:
    def __init__(self, repo: CameraRepository) -> None:
        self.repo = repo

    def list_cameras(self):
        return self.repo.list()

    def get_camera(self, camera_id: int):
        return self.repo.get(camera_id)

    def create_camera(self, payload: CameraCreate):
        return self.repo.create(payload)

    def update_camera(self, camera_id: int, payload: CameraUpdate):
        camera = self.repo.get(camera_id)
        if not camera:
            return None
        return self.repo.update(camera, payload)

    def delete_camera(self, camera_id: int) -> bool:
        camera = self.repo.get(camera_id)
        if not camera:
            return False
        self.repo.delete(camera)
        return True
