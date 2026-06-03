from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.concept_settings import ConceptSettings
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    design_identifier: str,
    *,
    body: ConceptSettings,
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
        "method": "post",
        "url": "/concepts/{design_identifier}/settings".format(
            design_identifier=quote(str(design_identifier), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ConceptSettings | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = ConceptSettings.from_dict(response.json())

        return response_201

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
) -> Response[Any | ConceptSettings | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    design_identifier: str,
    *,
    client: AuthenticatedClient,
    body: ConceptSettings,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | ConceptSettings | HTTPValidationError]:
    """Create Or Update Design Instance Settings

     Create or update Concept settings.

    Args:
        design_identifier (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (ConceptSettings): Concept Settings Base Model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConceptSettings | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        design_identifier=design_identifier,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    design_identifier: str,
    *,
    client: AuthenticatedClient,
    body: ConceptSettings,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | ConceptSettings | HTTPValidationError | None:
    """Create Or Update Design Instance Settings

     Create or update Concept settings.

    Args:
        design_identifier (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (ConceptSettings): Concept Settings Base Model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConceptSettings | HTTPValidationError
    """

    return sync_detailed(
        design_identifier=design_identifier,
        client=client,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    design_identifier: str,
    *,
    client: AuthenticatedClient,
    body: ConceptSettings,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | ConceptSettings | HTTPValidationError]:
    """Create Or Update Design Instance Settings

     Create or update Concept settings.

    Args:
        design_identifier (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (ConceptSettings): Concept Settings Base Model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConceptSettings | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        design_identifier=design_identifier,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    design_identifier: str,
    *,
    client: AuthenticatedClient,
    body: ConceptSettings,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | ConceptSettings | HTTPValidationError | None:
    """Create Or Update Design Instance Settings

     Create or update Concept settings.

    Args:
        design_identifier (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (ConceptSettings): Concept Settings Base Model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConceptSettings | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            design_identifier=design_identifier,
            client=client,
            body=body,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
