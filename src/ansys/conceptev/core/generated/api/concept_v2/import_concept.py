from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_import_concept import BodyImportConcept
from ...models.concept_output import ConceptOutput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyImportConcept,
    name: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_name: None | str | Unset
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/concept:import",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ConceptOutput | None:
    if response.status_code == 201:
        response_201 = ConceptOutput.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ConceptOutput]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyImportConcept,
    name: None | str | Unset = UNSET,
) -> Response[Any | ConceptOutput]:
    """Import Concept

     Import a legacy v1 ExchangeFile JSON export into a v2 .cev concept.

    Converts the v1 schema to v2, extracts all embedded blobs into file items,
    strips cloud-specific fields (user_id, project_id, design_id, etc.),
    and writes the result as a new unsaved .cev archive.

    The imported concept will have ``save_state=UNSAVED`` — use the
    `/v2/concept/{id}/save` endpoint to persist it to a user-specified path.

    Args:
        file: The uploaded ExchangeFile JSON export from a v1 concept.
        name: Optional override for the concept name.
        database: Filesystem database (this endpoint is filesystem-backend only).

    Returns:
        ConceptOutput with save_state=UNSAVED, ready for saving or modification.

    Args:
        name (None | str | Unset):
        body (BodyImportConcept):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConceptOutput]
    """

    kwargs = _get_kwargs(
        body=body,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BodyImportConcept,
    name: None | str | Unset = UNSET,
) -> Any | ConceptOutput | None:
    """Import Concept

     Import a legacy v1 ExchangeFile JSON export into a v2 .cev concept.

    Converts the v1 schema to v2, extracts all embedded blobs into file items,
    strips cloud-specific fields (user_id, project_id, design_id, etc.),
    and writes the result as a new unsaved .cev archive.

    The imported concept will have ``save_state=UNSAVED`` — use the
    `/v2/concept/{id}/save` endpoint to persist it to a user-specified path.

    Args:
        file: The uploaded ExchangeFile JSON export from a v1 concept.
        name: Optional override for the concept name.
        database: Filesystem database (this endpoint is filesystem-backend only).

    Returns:
        ConceptOutput with save_state=UNSAVED, ready for saving or modification.

    Args:
        name (None | str | Unset):
        body (BodyImportConcept):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConceptOutput
    """

    return sync_detailed(
        client=client,
        body=body,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyImportConcept,
    name: None | str | Unset = UNSET,
) -> Response[Any | ConceptOutput]:
    """Import Concept

     Import a legacy v1 ExchangeFile JSON export into a v2 .cev concept.

    Converts the v1 schema to v2, extracts all embedded blobs into file items,
    strips cloud-specific fields (user_id, project_id, design_id, etc.),
    and writes the result as a new unsaved .cev archive.

    The imported concept will have ``save_state=UNSAVED`` — use the
    `/v2/concept/{id}/save` endpoint to persist it to a user-specified path.

    Args:
        file: The uploaded ExchangeFile JSON export from a v1 concept.
        name: Optional override for the concept name.
        database: Filesystem database (this endpoint is filesystem-backend only).

    Returns:
        ConceptOutput with save_state=UNSAVED, ready for saving or modification.

    Args:
        name (None | str | Unset):
        body (BodyImportConcept):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConceptOutput]
    """

    kwargs = _get_kwargs(
        body=body,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BodyImportConcept,
    name: None | str | Unset = UNSET,
) -> Any | ConceptOutput | None:
    """Import Concept

     Import a legacy v1 ExchangeFile JSON export into a v2 .cev concept.

    Converts the v1 schema to v2, extracts all embedded blobs into file items,
    strips cloud-specific fields (user_id, project_id, design_id, etc.),
    and writes the result as a new unsaved .cev archive.

    The imported concept will have ``save_state=UNSAVED`` — use the
    `/v2/concept/{id}/save` endpoint to persist it to a user-specified path.

    Args:
        file: The uploaded ExchangeFile JSON export from a v1 concept.
        name: Optional override for the concept name.
        database: Filesystem database (this endpoint is filesystem-backend only).

    Returns:
        ConceptOutput with save_state=UNSAVED, ready for saving or modification.

    Args:
        name (None | str | Unset):
        body (BodyImportConcept):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConceptOutput
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            name=name,
        )
    ).parsed
