from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.concept_output import ConceptOutput
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    path_to_file: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["path_to_file"] = path_to_file

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/concept:open",
        "params": params,
    }

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
    *,
    client: AuthenticatedClient | Client,
    path_to_file: str,
) -> Response[Any | ConceptOutput | HTTPValidationError]:
    """Open Concept

     Open a .cev concept file and load it into the file-system database.

    Reads the concept ID from inside the file so the filename can be any
    human-readable name rather than the UUID.  Registers the path so all
    subsequent operations resolve the correct location without requiring
    another open call.  Multiple files in different directories can be
    registered independently.

    Note: This endpoint is only meaningful when the file-system backend is
    active.  It is registered unconditionally so the route exists regardless
    of which backend was configured at import time (important for tests that
    swap configs via fixtures).

    Args:
        path_to_file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConceptOutput | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        path_to_file=path_to_file,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    path_to_file: str,
) -> Any | ConceptOutput | HTTPValidationError | None:
    """Open Concept

     Open a .cev concept file and load it into the file-system database.

    Reads the concept ID from inside the file so the filename can be any
    human-readable name rather than the UUID.  Registers the path so all
    subsequent operations resolve the correct location without requiring
    another open call.  Multiple files in different directories can be
    registered independently.

    Note: This endpoint is only meaningful when the file-system backend is
    active.  It is registered unconditionally so the route exists regardless
    of which backend was configured at import time (important for tests that
    swap configs via fixtures).

    Args:
        path_to_file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConceptOutput | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        path_to_file=path_to_file,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    path_to_file: str,
) -> Response[Any | ConceptOutput | HTTPValidationError]:
    """Open Concept

     Open a .cev concept file and load it into the file-system database.

    Reads the concept ID from inside the file so the filename can be any
    human-readable name rather than the UUID.  Registers the path so all
    subsequent operations resolve the correct location without requiring
    another open call.  Multiple files in different directories can be
    registered independently.

    Note: This endpoint is only meaningful when the file-system backend is
    active.  It is registered unconditionally so the route exists regardless
    of which backend was configured at import time (important for tests that
    swap configs via fixtures).

    Args:
        path_to_file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConceptOutput | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        path_to_file=path_to_file,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    path_to_file: str,
) -> Any | ConceptOutput | HTTPValidationError | None:
    """Open Concept

     Open a .cev concept file and load it into the file-system database.

    Reads the concept ID from inside the file so the filename can be any
    human-readable name rather than the UUID.  Registers the path so all
    subsequent operations resolve the correct location without requiring
    another open call.  Multiple files in different directories can be
    registered independently.

    Note: This endpoint is only meaningful when the file-system backend is
    active.  It is registered unconditionally so the route exists regardless
    of which backend was configured at import time (important for tests that
    swap configs via fixtures).

    Args:
        path_to_file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConceptOutput | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            path_to_file=path_to_file,
        )
    ).parsed
