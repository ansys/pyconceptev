from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_job_file_converted_response_200_item import GetJobFileConvertedResponse200Item
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    concept_id: str,
    job_id: str,
    file_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/concept/{concept_id}/job/{job_id}/files/{file_id}:converted".format(
            concept_id=quote(str(concept_id), safe=""),
            job_id=quote(str(job_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[GetJobFileConvertedResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetJobFileConvertedResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | list[GetJobFileConvertedResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    concept_id: str,
    job_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError | list[GetJobFileConvertedResponse200Item]]:
    """Get Job File Converted

     Retrieve a job output file with values converted to the caller's units.

    Reads the raw (SI-unit) solver output and converts every solved
    requirement to the caller's preferred display units server-side, so
    clients don't need their own copy of the unit-conversion logic.

    Args:
        concept_id (str):
        job_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[GetJobFileConvertedResponse200Item]]
    """

    kwargs = _get_kwargs(
        concept_id=concept_id,
        job_id=job_id,
        file_id=file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    concept_id: str,
    job_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | HTTPValidationError | list[GetJobFileConvertedResponse200Item] | None:
    """Get Job File Converted

     Retrieve a job output file with values converted to the caller's units.

    Reads the raw (SI-unit) solver output and converts every solved
    requirement to the caller's preferred display units server-side, so
    clients don't need their own copy of the unit-conversion logic.

    Args:
        concept_id (str):
        job_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[GetJobFileConvertedResponse200Item]
    """

    return sync_detailed(
        concept_id=concept_id,
        job_id=job_id,
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    concept_id: str,
    job_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError | list[GetJobFileConvertedResponse200Item]]:
    """Get Job File Converted

     Retrieve a job output file with values converted to the caller's units.

    Reads the raw (SI-unit) solver output and converts every solved
    requirement to the caller's preferred display units server-side, so
    clients don't need their own copy of the unit-conversion logic.

    Args:
        concept_id (str):
        job_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[GetJobFileConvertedResponse200Item]]
    """

    kwargs = _get_kwargs(
        concept_id=concept_id,
        job_id=job_id,
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    concept_id: str,
    job_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | HTTPValidationError | list[GetJobFileConvertedResponse200Item] | None:
    """Get Job File Converted

     Retrieve a job output file with values converted to the caller's units.

    Reads the raw (SI-unit) solver output and converts every solved
    requirement to the caller's preferred display units server-side, so
    clients don't need their own copy of the unit-conversion logic.

    Args:
        concept_id (str):
        job_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[GetJobFileConvertedResponse200Item]
    """

    return (
        await asyncio_detailed(
            concept_id=concept_id,
            job_id=job_id,
            file_id=file_id,
            client=client,
        )
    ).parsed
