from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    wheel_id: str,
    architecture_id: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["wheel_id"] = wheel_id

    params["architecture_id"] = architecture_id

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
        "method": "get",
        "url": "/architectures:max_speed",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | float | None:
    if response.status_code == 200:
        response_200 = cast(float, response.json())
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
) -> Response[Any | HTTPValidationError | float]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    wheel_id: str,
    architecture_id: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | float]:
    """Get Architecture Max Speed

     Get the max linear speed of the architecture from component bounds.

    Args:
        wheel_id (str):
        architecture_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | float]
    """

    kwargs = _get_kwargs(
        wheel_id=wheel_id,
        architecture_id=architecture_id,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    wheel_id: str,
    architecture_id: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | float | None:
    """Get Architecture Max Speed

     Get the max linear speed of the architecture from component bounds.

    Args:
        wheel_id (str):
        architecture_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | float
    """

    return sync_detailed(
        client=client,
        wheel_id=wheel_id,
        architecture_id=architecture_id,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    wheel_id: str,
    architecture_id: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | float]:
    """Get Architecture Max Speed

     Get the max linear speed of the architecture from component bounds.

    Args:
        wheel_id (str):
        architecture_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | float]
    """

    kwargs = _get_kwargs(
        wheel_id=wheel_id,
        architecture_id=architecture_id,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    wheel_id: str,
    architecture_id: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | float | None:
    """Get Architecture Max Speed

     Get the max linear speed of the architecture from component bounds.

    Args:
        wheel_id (str):
        architecture_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | float
    """

    return (
        await asyncio_detailed(
            client=client,
            wheel_id=wheel_id,
            architecture_id=architecture_id,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
