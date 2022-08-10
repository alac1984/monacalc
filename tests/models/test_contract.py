import pytest
from datetime import date
from models.contract import Contract


@pytest.fixture
def contract_data():
    return {
        "id": 1,
        "school_id": 1,
        "mat": "19039203DBX",
        "start": date(2022, 1, 1),
        "end": date(2022, 9, 1),
        "work_hours": 20,
    }


def test_contract_instantiation(contract_data):
    assert Contract(**contract_data) is not None


def test_contract_planning_hours(contract_data):
    contract = Contract(**contract_data)
    assert contract.planning_hours == 7


def test_contract_total_hours(contract_data):
    contract = Contract(**contract_data)
    assert contract.total_hours == 27
