# type: ignore[attr-defined]
from repository.repo import Repository
from requests.models.contract import (
    ListContractsValidRequest,
    ListContractsInvalidRequest,
    CreateContractValidRequest,
    CreateContractInvalidRequest,
)
from responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request,
)


def list_contracts(
    repo: Repository, request: ListContractsValidRequest | ListContractsInvalidRequest
):
    if not request:
        return build_response_from_invalid_request(request)

    try:
        contracts = repo.list_contracts(request.filters)
        return ResponseSuccess(contracts)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, 500, exc)


def create_contract(
    repo: Repository,
    request: CreateContractValidRequest | CreateContractInvalidRequest,
):
    if not request:
        return build_response_from_invalid_request(request)

    try:
        contract = repo.create_contract(request.data)
        return ResponseSuccess(contract)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, 500, exc)
