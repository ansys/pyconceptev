from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.job_output import JobOutput
from ...types import Response


def _get_kwargs(
    concept_id: str,
    job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/concept/{concept_id}/job/{job_id}".format(
            concept_id=quote(str(concept_id), safe=""),
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | JobOutput | None:
    if response.status_code == 200:
        response_200 = JobOutput.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | JobOutput]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    concept_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HTTPValidationError | JobOutput]:
    """Get Job

     Retrieve job status.

    Args:
        concept_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | JobOutput]
    """

    kwargs = _get_kwargs(
        concept_id=concept_id,
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    concept_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HTTPValidationError | JobOutput | None:
    """Get Job

     Retrieve job status.

    Args:
        concept_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | JobOutput
    """

    return sync_detailed(
        concept_id=concept_id,
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    concept_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HTTPValidationError | JobOutput]:
    """Get Job

     Retrieve job status.

    Args:
        concept_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | JobOutput]
    """

    kwargs = _get_kwargs(
        concept_id=concept_id,
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    concept_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HTTPValidationError | JobOutput | None:
    """Get Job

     Retrieve job status.

    Args:
        concept_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | JobOutput
    """

    return (
        await asyncio_detailed(
            concept_id=concept_id,
            job_id=job_id,
            client=client,
        )
    ).parsed
