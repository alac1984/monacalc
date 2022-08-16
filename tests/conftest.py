# type: ignore[import]
import pytest
from datetime import date
from repository.repo import Repository
from repository.objects import SchoolDB, ContractDB


@pytest.fixture(scope="module")
def repo():
    repo = Repository("sqlite+pysqlite:///:memory:")

    repo.base.metadata.create_all(repo.engine)

    s1 = SchoolDB(name="Rogério Fróes")

    c1 = ContractDB(
        school_id=1,
        mat="AB2093043043X",
        start=date(2022, 1, 1),
        end=date(2022, 9, 1),
        work_hours=20,
    )

    repo.session.add_all([s1, c1])
    repo.session.commit()

    yield repo
