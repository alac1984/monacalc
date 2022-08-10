# type: ignore[attr-defined]
from sqlalchemy import select
from repository.objects import ContractDB


def test_repo_create_contract(repo):
    stmt = select(ContractDB).where(ContractDB.id == 1)
    contractdb = repo.session.scalars(stmt).first()
    contract = repo._create_contract(contractdb)

    assert contract is not None
    assert contract.id == 1
