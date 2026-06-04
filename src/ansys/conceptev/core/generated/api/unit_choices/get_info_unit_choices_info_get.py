from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_info_unit_choices_info_get_response_get_info_unit_choices_info_get import (
    GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/unit_choices/info",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet | None:
    if response.status_code == 200:
        response_200 = GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet]:
    """Get Info

     Get table of units for frontend generation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet | None:
    """Get Info

     Get table of units for frontend generation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet]:
    """Get Info

     Get table of units for frontend generation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet | None:
    """Get Info

     Get table of units for frontend generation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
