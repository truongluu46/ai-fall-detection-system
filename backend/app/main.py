from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.router import api_router
from backend.app.core.config import settings
from backend.app.utils.file_storage import ensure_storage_dirs
from backend.app.utils.logger import configure_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    ensure_storage_dirs()
    yield


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.api_v1_prefix)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.get_app_host(),
        port=settings.get_app_port(),
    )
