from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.total_tractive_torque_graph_input import TotalTractiveTorqueGraphInput
from ...models.total_tractive_torque_graph_output import TotalTractiveTorqueGraphOutput
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: TotalTractiveTorqueGraphInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/concept/{id}:calculate_forces".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TotalTractiveTorqueGraphOutput | None:
    if response.status_code == 200:
        response_200 = TotalTractiveTorqueGraphOutput.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | TotalTractiveTorqueGraphOutput]:
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
    body: TotalTractiveTorqueGraphInput,
) -> Response[Any | TotalTractiveTorqueGraphOutput]:
    """Calculate Total Forces

     Calculate the total tractive torque.

    Args:
        id (str):
        body (TotalTractiveTorqueGraphInput): Total Tractive Torque Graph Input.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TotalTractiveTorqueGraphOutput]
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
    body: TotalTractiveTorqueGraphInput,
) -> Any | TotalTractiveTorqueGraphOutput | None:
    """Calculate Total Forces

     Calculate the total tractive torque.

    Args:
        id (str):
        body (TotalTractiveTorqueGraphInput): Total Tractive Torque Graph Input.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TotalTractiveTorqueGraphOutput
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
    body: TotalTractiveTorqueGraphInput,
) -> Response[Any | TotalTractiveTorqueGraphOutput]:
    """Calculate Total Forces

     Calculate the total tractive torque.

    Args:
        id (str):
        body (TotalTractiveTorqueGraphInput): Total Tractive Torque Graph Input.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TotalTractiveTorqueGraphOutput]
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
    body: TotalTractiveTorqueGraphInput,
) -> Any | TotalTractiveTorqueGraphOutput | None:
    """Calculate Total Forces

     Calculate the total tractive torque.

    Args:
        id (str):
        body (TotalTractiveTorqueGraphInput): Total Tractive Torque Graph Input.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TotalTractiveTorqueGraphOutput
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
