# type: ignore[import, attr-defined]
from typing import Iterable
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models.contract import Contract
from repository.objects import Base, ContractDB


class Repository:
    def __init__(
        self,
        connstr: str = "postgresql+psycopg2://monacalc:a1k8u2@localhost:5432/monacalc",  # noqa
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

    def _create_contracts(self, objs: Iterable):
        return [self._create_contract(obj) for obj in objs]

    def list_contracts(self, filters: dict):
        stmt = select(ContractDB)
        result = self.session.scalars(stmt)

        return self._create_contracts(result)
