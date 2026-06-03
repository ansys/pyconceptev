from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.component_loss_map_args import ComponentLossMapArgs
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ComponentLossMapArgs | None | Unset = UNSET,
    component_id: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["component_id"] = component_id

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
        "method": "post",
        "url": "/components:get_display_data",
        "params": params,
    }

    if isinstance(body, ComponentLossMapArgs):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ComponentLossMapArgs | None | Unset = UNSET,
    component_id: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Calc Display Data

     Calculate component data from an ID.

    Args:
        component_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (ComponentLossMapArgs | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        component_id=component_id,
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
    body: ComponentLossMapArgs | None | Unset = UNSET,
    component_id: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Calc Display Data

     Calculate component data from an ID.

    Args:
        component_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (ComponentLossMapArgs | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        component_id=component_id,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ComponentLossMapArgs | None | Unset = UNSET,
    component_id: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Calc Display Data

     Calculate component data from an ID.

    Args:
        component_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (ComponentLossMapArgs | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        component_id=component_id,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ComponentLossMapArgs | None | Unset = UNSET,
    component_id: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Calc Display Data

     Calculate component data from an ID.

    Args:
        component_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (ComponentLossMapArgs | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            component_id=component_id,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
