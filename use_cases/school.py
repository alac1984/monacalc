# type: ignore[attr-defined]
from repository.repo import Repository
from requests.models.school import (
    ListSchoolsValidRequest,
    ListSchoolsInvalidRequest,
)
from responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request,
)


def list_schools(
    repo: Repository, request: ListSchoolsValidRequest | ListSchoolsInvalidRequest
):
    if not request:
        return build_response_from_invalid_request(request)

    try:
        schools = repo.list_schools(request.filters)
        return ResponseSuccess(schools)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, 500, exc)
