from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.concept_output import ConceptOutput
from ...models.concept_save_request import ConceptSaveRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: ConceptSaveRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/concept/{id}/save".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ConceptOutput | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ConceptOutput.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
) -> Response[Any | ConceptOutput | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConceptSaveRequest,
) -> Response[Any | ConceptOutput | HTTPValidationError]:
    """Save Concept

     Save a concept to a specified file path (filesystem backend only).

    Copies the ``.cev`` archive to the given path, re-registers the concept
    at that location, and sets ``save_state`` to ``SaveState.SAVED``.

    Args:
        id (str):
        body (ConceptSaveRequest): Request body for the save-concept endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConceptOutput | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConceptSaveRequest,
) -> Any | ConceptOutput | HTTPValidationError | None:
    """Save Concept

     Save a concept to a specified file path (filesystem backend only).

    Copies the ``.cev`` archive to the given path, re-registers the concept
    at that location, and sets ``save_state`` to ``SaveState.SAVED``.

    Args:
        id (str):
        body (ConceptSaveRequest): Request body for the save-concept endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConceptOutput | HTTPValidationError
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConceptSaveRequest,
) -> Response[Any | ConceptOutput | HTTPValidationError]:
    """Save Concept

     Save a concept to a specified file path (filesystem backend only).

    Copies the ``.cev`` archive to the given path, re-registers the concept
    at that location, and sets ``save_state`` to ``SaveState.SAVED``.

    Args:
        id (str):
        body (ConceptSaveRequest): Request body for the save-concept endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConceptOutput | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConceptSaveRequest,
) -> Any | ConceptOutput | HTTPValidationError | None:
    """Save Concept

     Save a concept to a specified file path (filesystem backend only).

    Copies the ``.cev`` archive to the given path, re-registers the concept
    at that location, and sets ``save_state`` to ``SaveState.SAVED``.

    Args:
        id (str):
        body (ConceptSaveRequest): Request body for the save-concept endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConceptOutput | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
