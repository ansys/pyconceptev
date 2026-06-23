from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_job_backend_availability_response_check_job_backend_availability import (
    CheckJobBackendAvailabilityResponseCheckJobBackendAvailability,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    concept_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/concept/{concept_id}/job/availability".format(
            concept_id=quote(str(concept_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | CheckJobBackendAvailabilityResponseCheckJobBackendAvailability
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = CheckJobBackendAvailabilityResponseCheckJobBackendAvailability.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | CheckJobBackendAvailabilityResponseCheckJobBackendAvailability | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    concept_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | CheckJobBackendAvailabilityResponseCheckJobBackendAvailability | HTTPValidationError
]:
    """Check Job Backend Availability

     Check if job backend is available.

    Args:
        concept_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CheckJobBackendAvailabilityResponseCheckJobBackendAvailability | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        concept_id=concept_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    concept_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | CheckJobBackendAvailabilityResponseCheckJobBackendAvailability
    | HTTPValidationError
    | None
):
    """Check Job Backend Availability

     Check if job backend is available.

    Args:
        concept_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CheckJobBackendAvailabilityResponseCheckJobBackendAvailability | HTTPValidationError
    """

    return sync_detailed(
        concept_id=concept_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    concept_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | CheckJobBackendAvailabilityResponseCheckJobBackendAvailability | HTTPValidationError
]:
    """Check Job Backend Availability

     Check if job backend is available.

    Args:
        concept_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CheckJobBackendAvailabilityResponseCheckJobBackendAvailability | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        concept_id=concept_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    concept_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | CheckJobBackendAvailabilityResponseCheckJobBackendAvailability
    | HTTPValidationError
    | None
):
    """Check Job Backend Availability

     Check if job backend is available.

    Args:
        concept_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CheckJobBackendAvailabilityResponseCheckJobBackendAvailability | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            concept_id=concept_id,
            client=client,
        )
    ).parsed
