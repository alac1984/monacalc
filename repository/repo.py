# type: ignore[import, attr-defined]
from typing import Iterable
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models.contract import Contract
from models.school import School
from repository.objects import Base, ContractDB, SchoolDB


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

    def _create_school(self, obj):
        return School(id=obj.id, name=obj.name)

    def _create_schools(self, objs: Iterable):
        return [self._create_school(obj) for obj in objs]

    def list_contracts(self, filters: dict):
        stmt = select(ContractDB)
        result = self.session.scalars(stmt)

        return self._create_contracts(result)

    def list_schools(self, filters: dict):
        stmt = select(SchoolDB)
        result = self.session.scalars(stmt)

        return self._create_schools(result)

    def create_contract(self, data: dict):
        ...

        contract = ContractDB(**data)
        self.session.add(contract)
        self.session.commit()
        return contract.id
