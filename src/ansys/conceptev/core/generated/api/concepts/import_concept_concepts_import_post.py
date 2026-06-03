from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_import_concept_concepts_import_post import BodyImportConceptConceptsImportPost
from ...models.concept import Concept
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyImportConceptConceptsImportPost,
    design_id: str,
    project_id: str,
    design_instance_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["design_id"] = design_id

    params["project_id"] = project_id

    json_design_instance_id: None | str | Unset
    if isinstance(design_instance_id, Unset):
        json_design_instance_id = UNSET
    else:
        json_design_instance_id = design_instance_id
    params["design_instance_id"] = json_design_instance_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/concepts:import",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Concept | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = Concept.from_dict(response.json())

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
) -> Response[Any | Concept | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyImportConceptConceptsImportPost,
    design_id: str,
    project_id: str,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | Concept | HTTPValidationError]:
    """Import Concept

     Import Concept from Exchange File.

    Args:
        design_id (str):
        project_id (str):
        design_instance_id (None | str | Unset):
        body (BodyImportConceptConceptsImportPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Concept | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        design_id=design_id,
        project_id=project_id,
        design_instance_id=design_instance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyImportConceptConceptsImportPost,
    design_id: str,
    project_id: str,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | Concept | HTTPValidationError | None:
    """Import Concept

     Import Concept from Exchange File.

    Args:
        design_id (str):
        project_id (str):
        design_instance_id (None | str | Unset):
        body (BodyImportConceptConceptsImportPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Concept | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        design_id=design_id,
        project_id=project_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyImportConceptConceptsImportPost,
    design_id: str,
    project_id: str,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | Concept | HTTPValidationError]:
    """Import Concept

     Import Concept from Exchange File.

    Args:
        design_id (str):
        project_id (str):
        design_instance_id (None | str | Unset):
        body (BodyImportConceptConceptsImportPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Concept | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        design_id=design_id,
        project_id=project_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyImportConceptConceptsImportPost,
    design_id: str,
    project_id: str,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | Concept | HTTPValidationError | None:
    """Import Concept

     Import Concept from Exchange File.

    Args:
        design_id (str):
        project_id (str):
        design_instance_id (None | str | Unset):
        body (BodyImportConceptConceptsImportPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Concept | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            design_id=design_id,
            project_id=project_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
