from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.architecture_input_ids import ArchitectureInputIds
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    *,
    body: ArchitectureInputIds,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_design_id: None | str | Unset
    if isinstance(design_id, Unset):
        json_design_id = UNSET
    else:
        json_design_id = design_id
    params["design_id"] = json_design_id

    json_design_instance_id: None | str | Unset
    if isinstance(design_instance_id, Unset):
        json_design_instance_id = UNSET
    else:
        json_design_instance_id = design_instance_id
    params["design_instance_id"] = json_design_instance_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/architectures/{item_id}".format(
            item_id=quote(str(item_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ArchitectureInputIds | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ArchitectureInputIds.from_dict(response.json())

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
) -> Response[Any | ArchitectureInputIds | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: ArchitectureInputIds,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | ArchitectureInputIds | HTTPValidationError]:
    """Update Architecture

     Update Architecture with new Architecture.

    Args:
        item_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (ArchitectureInputIds): Base class for architecture ID classes.

            Mutable so we can calculate component masses and costs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ArchitectureInputIds | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: ArchitectureInputIds,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | ArchitectureInputIds | HTTPValidationError | None:
    """Update Architecture

     Update Architecture with new Architecture.

    Args:
        item_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (ArchitectureInputIds): Base class for architecture ID classes.

            Mutable so we can calculate component masses and costs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ArchitectureInputIds | HTTPValidationError
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: ArchitectureInputIds,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | ArchitectureInputIds | HTTPValidationError]:
    """Update Architecture

     Update Architecture with new Architecture.

    Args:
        item_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (ArchitectureInputIds): Base class for architecture ID classes.

            Mutable so we can calculate component masses and costs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ArchitectureInputIds | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: ArchitectureInputIds,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | ArchitectureInputIds | HTTPValidationError | None:
    """Update Architecture

     Update Architecture with new Architecture.

    Args:
        item_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (ArchitectureInputIds): Base class for architecture ID classes.

            Mutable so we can calculate component masses and costs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ArchitectureInputIds | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            body=body,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
