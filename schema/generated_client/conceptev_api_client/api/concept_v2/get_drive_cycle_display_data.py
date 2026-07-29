from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.drive_cycle import DriveCycle
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    id: str,
    part_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/concept/{id}/drive_cycle/{part_id}:get_display_data".format(
            id=quote(str(id), safe=""),
            part_id=quote(str(part_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DriveCycle | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DriveCycle.from_dict(response.json())

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
) -> Response[Any | DriveCycle | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    part_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DriveCycle | HTTPValidationError]:
    """Get Drive Cycle Display Data Endpoint

     Get the full time-series point data for a drive cycle (for plotting).

    The stored drive cycle record keeps ``points`` in a separate file to avoid
    bloating the concept document.  This endpoint reads that file, hydrates the
    full :class:`~conceptev_solver.drive_cycle.DriveCycle` object (including all
    ``points``), converts each point to the caller's preferred units, and returns
    the result.

    Use this endpoint when you need to render a speed/distance/time chart for a
    drive cycle — the standard ``GET /v2/concept/{id}/drive_cycle/{part_id}``
    endpoint omits ``points`` by design.

    Args:
        id: The concept ID.
        part_id: The drive-cycle part ID.
        database: Injected database dependency.
        unit_choices: Injected unit-choice dependency.

    Returns:
        A :class:`~conceptev_solver.drive_cycle.DriveCycle` with ``points``
        converted to user units.

    Raises:
        HTTPException 404: If the concept, part, or associated file is not found.

    Args:
        id (str):
        part_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DriveCycle | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        part_id=part_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    part_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DriveCycle | HTTPValidationError | None:
    """Get Drive Cycle Display Data Endpoint

     Get the full time-series point data for a drive cycle (for plotting).

    The stored drive cycle record keeps ``points`` in a separate file to avoid
    bloating the concept document.  This endpoint reads that file, hydrates the
    full :class:`~conceptev_solver.drive_cycle.DriveCycle` object (including all
    ``points``), converts each point to the caller's preferred units, and returns
    the result.

    Use this endpoint when you need to render a speed/distance/time chart for a
    drive cycle — the standard ``GET /v2/concept/{id}/drive_cycle/{part_id}``
    endpoint omits ``points`` by design.

    Args:
        id: The concept ID.
        part_id: The drive-cycle part ID.
        database: Injected database dependency.
        unit_choices: Injected unit-choice dependency.

    Returns:
        A :class:`~conceptev_solver.drive_cycle.DriveCycle` with ``points``
        converted to user units.

    Raises:
        HTTPException 404: If the concept, part, or associated file is not found.

    Args:
        id (str):
        part_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DriveCycle | HTTPValidationError
    """

    return sync_detailed(
        id=id,
        part_id=part_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    part_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DriveCycle | HTTPValidationError]:
    """Get Drive Cycle Display Data Endpoint

     Get the full time-series point data for a drive cycle (for plotting).

    The stored drive cycle record keeps ``points`` in a separate file to avoid
    bloating the concept document.  This endpoint reads that file, hydrates the
    full :class:`~conceptev_solver.drive_cycle.DriveCycle` object (including all
    ``points``), converts each point to the caller's preferred units, and returns
    the result.

    Use this endpoint when you need to render a speed/distance/time chart for a
    drive cycle — the standard ``GET /v2/concept/{id}/drive_cycle/{part_id}``
    endpoint omits ``points`` by design.

    Args:
        id: The concept ID.
        part_id: The drive-cycle part ID.
        database: Injected database dependency.
        unit_choices: Injected unit-choice dependency.

    Returns:
        A :class:`~conceptev_solver.drive_cycle.DriveCycle` with ``points``
        converted to user units.

    Raises:
        HTTPException 404: If the concept, part, or associated file is not found.

    Args:
        id (str):
        part_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DriveCycle | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        part_id=part_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    part_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DriveCycle | HTTPValidationError | None:
    """Get Drive Cycle Display Data Endpoint

     Get the full time-series point data for a drive cycle (for plotting).

    The stored drive cycle record keeps ``points`` in a separate file to avoid
    bloating the concept document.  This endpoint reads that file, hydrates the
    full :class:`~conceptev_solver.drive_cycle.DriveCycle` object (including all
    ``points``), converts each point to the caller's preferred units, and returns
    the result.

    Use this endpoint when you need to render a speed/distance/time chart for a
    drive cycle — the standard ``GET /v2/concept/{id}/drive_cycle/{part_id}``
    endpoint omits ``points`` by design.

    Args:
        id: The concept ID.
        part_id: The drive-cycle part ID.
        database: Injected database dependency.
        unit_choices: Injected unit-choice dependency.

    Returns:
        A :class:`~conceptev_solver.drive_cycle.DriveCycle` with ``points``
        converted to user units.

    Raises:
        HTTPException 404: If the concept, part, or associated file is not found.

    Args:
        id (str):
        part_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DriveCycle | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            id=id,
            part_id=part_id,
            client=client,
        )
    ).parsed
