from fastapi import APIRouter

from backend.app.api.v1.endpoints.cameras import router as cameras_router
from backend.app.api.v1.endpoints.fall_events import router as fall_events_router
from backend.app.api.v1.endpoints.health import router as health_router
from backend.app.api.v1.endpoints.model_versions import router as model_versions_router
from backend.app.api.v1.endpoints.processing import router as processing_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(cameras_router)
api_router.include_router(model_versions_router)
api_router.include_router(fall_events_router)
api_router.include_router(processing_router)
