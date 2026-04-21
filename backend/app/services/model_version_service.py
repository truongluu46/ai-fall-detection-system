from backend.app.repositories.model_version_repository import ModelVersionRepository
from backend.app.schemas.model_version import ModelVersionCreate, ModelVersionUpdate


class ModelVersionService:
    def __init__(self, repo: ModelVersionRepository) -> None:
        self.repo = repo

    def list_model_versions(self):
        return self.repo.list()

    def get_model_version(self, model_version_id: int):
        return self.repo.get(model_version_id)

    def get_active_model_version(self):
        return self.repo.get_active()

    def create_model_version(self, payload: ModelVersionCreate):
        return self.repo.create(payload)

    def update_model_version(self, model_version_id: int, payload: ModelVersionUpdate):
        model_version = self.repo.get(model_version_id)
        if not model_version:
            return None
        return self.repo.update(model_version, payload)
