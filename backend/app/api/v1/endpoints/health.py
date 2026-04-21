from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.app.api.deps import get_db_session
from backend.app.core.config import settings
from backend.app.schemas.common import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health_check(db: Session = Depends(get_db_session)) -> HealthResponse:
    database_status = "ok"
    try:
        db.execute(text("SELECT 1"))
    except Exception:
        database_status = "error"

    return HealthResponse(
        status="ok",
        app_name=settings.app_name,
        environment=settings.app_env,
        database=database_status,
        timestamp=datetime.utcnow(),
    )
