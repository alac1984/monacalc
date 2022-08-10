# type: ignore[import, attr-defined]
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.contract import Contract
from repository.objects import Base


class Repository:
    def __init__(
        self,
        connstr: str = "postgresql+psycopg2://monacalcdbuser:a1k8u2@localhost/monacalcdb",  # noqa
    ):
        self.engine = create_engine(connstr)
        self.session = Session(self.engine)
        self.base = Base

    def _create_contract(self, obj):
        return Contract(
            id=obj.id,
            school_id=obj.school_id,
            mat=obj.mat,
            start=obj.start,
            end=obj.end,
            work_hours=obj.work_hours,
        )
