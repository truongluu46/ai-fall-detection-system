from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.models.processing_run import ProcessingRun
from backend.app.schemas.processing_run import ProcessingRunCreate, ProcessingRunUpdate


class ProcessingRunRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list(self) -> list[ProcessingRun]:
        stmt = select(ProcessingRun).order_by(ProcessingRun.id.desc())
        return list(self.db.scalars(stmt).all())

    def get(self, run_id: int) -> ProcessingRun | None:
        return self.db.get(ProcessingRun, run_id)

    def create(self, payload: ProcessingRunCreate) -> ProcessingRun:
        import datetime as dt

        run = ProcessingRun(**payload.model_dump(), created_at=dt.datetime.utcnow())
        self.db.add(run)
        self.db.commit()
        self.db.refresh(run)
        return run

    def update(self, run: ProcessingRun, payload: ProcessingRunUpdate) -> ProcessingRun:
        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(run, field, value)
        self.db.commit()
        self.db.refresh(run)
        return run
