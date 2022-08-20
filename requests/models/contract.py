from datetime import date
from collections.abc import Iterable
from requests.base import BaseValidRequest, BaseInvalidRequest


class ListContractsInvalidRequest(BaseInvalidRequest):
    pass


class ListContractsValidRequest(BaseValidRequest):
    pass


class CreateContractValidRequest(BaseValidRequest):
    pass


class CreateContractInvalidRequest(BaseInvalidRequest):
    pass


def build_list_contracts_request(
    filters=None,
) -> ListContractsInvalidRequest | ListContractsValidRequest:
    accepted_filters = ["start__gt", "start__lt", "end__gt", "end__lt"]
    invalid_req = ListContractsInvalidRequest()

    # TODO: insert all conditions

    # filters.update({"start": filters.get("start") or 1})
    # filters.update({"end": filters.get("end") or 100})

    # if filters is not None:
    #     if not isinstance(filters, Iterable):
    #         invalid_req.add_error("filters", "Is not iterable")

    # for key, value in filters.items():
    #     if key not in accepted_filters:
    #         invalid_req.add_error("filters", "Key {key} is not a valid filter")

    # if filters.get("start") >= filters.get("end"):
    #     invalid_req.add_error("filters", "start value should be less than end value")

    # if invalid_req.has_errors():
    #     return invalid_req

    return ListContractsValidRequest(filters=filters)


def build_create_contract_request(
    school_id: int,
    mat: str,
    start: date,
    end: date,
    work_hours: int,
) -> CreateContractInvalidRequest | CreateContractValidRequest:
    invalid_req = CreateContractInvalidRequest()

    # TODO: insert all conditions

    data = {
        "school_id": school_id,
        "mat": mat,
        "start": start,
        "end": end,
        "work_hours": work_hours,
    }

    return CreateContractValidRequest(data=data)
