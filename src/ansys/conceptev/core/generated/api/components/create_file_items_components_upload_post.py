from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_create_file_items_components_upload_post import BodyCreateFileItemsComponentsUploadPost
from ...models.component_file_type import ComponentFileType
from ...models.create_file_items_components_upload_post_response_201_item_type_1_type_0 import (
    CreateFileItemsComponentsUploadPostResponse201ItemType1Type0,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyCreateFileItemsComponentsUploadPost,
    component_file_type: ComponentFileType,
    return_speed_only: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_component_file_type: str = component_file_type
    params["component_file_type"] = json_component_file_type

    params["return_speed_only"] = return_speed_only

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
        "url": "/components:upload",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any | HTTPValidationError | list[CreateFileItemsComponentsUploadPostResponse201ItemType1Type0 | float | str] | None
):
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:

            def _parse_response_201_item(
                data: object,
            ) -> CreateFileItemsComponentsUploadPostResponse201ItemType1Type0 | float | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0 = (
                        CreateFileItemsComponentsUploadPostResponse201ItemType1Type0.from_dict(data)
                    )

                    return response_201_item_type_1_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(CreateFileItemsComponentsUploadPostResponse201ItemType1Type0 | float | str, data)

            response_201_item = _parse_response_201_item(response_201_item_data)

            response_201.append(response_201_item)

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
) -> Response[
    Any | HTTPValidationError | list[CreateFileItemsComponentsUploadPostResponse201ItemType1Type0 | float | str]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFileItemsComponentsUploadPost,
    component_file_type: ComponentFileType,
    return_speed_only: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[
    Any | HTTPValidationError | list[CreateFileItemsComponentsUploadPostResponse201ItemType1Type0 | float | str]
]:
    """Create File Items

     Create component from uploaded file.

    Returns the created file item ID and any extracted data needed by the UI in a dict.

    Args:
        component_file_type (ComponentFileType): Types of files.
        return_speed_only (bool | Unset):  Default: True.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (BodyCreateFileItemsComponentsUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[CreateFileItemsComponentsUploadPostResponse201ItemType1Type0 | float | str]]
    """

    kwargs = _get_kwargs(
        body=body,
        component_file_type=component_file_type,
        return_speed_only=return_speed_only,
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
    body: BodyCreateFileItemsComponentsUploadPost,
    component_file_type: ComponentFileType,
    return_speed_only: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> (
    Any | HTTPValidationError | list[CreateFileItemsComponentsUploadPostResponse201ItemType1Type0 | float | str] | None
):
    """Create File Items

     Create component from uploaded file.

    Returns the created file item ID and any extracted data needed by the UI in a dict.

    Args:
        component_file_type (ComponentFileType): Types of files.
        return_speed_only (bool | Unset):  Default: True.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (BodyCreateFileItemsComponentsUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[CreateFileItemsComponentsUploadPostResponse201ItemType1Type0 | float | str]
    """

    return sync_detailed(
        client=client,
        body=body,
        component_file_type=component_file_type,
        return_speed_only=return_speed_only,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFileItemsComponentsUploadPost,
    component_file_type: ComponentFileType,
    return_speed_only: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[
    Any | HTTPValidationError | list[CreateFileItemsComponentsUploadPostResponse201ItemType1Type0 | float | str]
]:
    """Create File Items

     Create component from uploaded file.

    Returns the created file item ID and any extracted data needed by the UI in a dict.

    Args:
        component_file_type (ComponentFileType): Types of files.
        return_speed_only (bool | Unset):  Default: True.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (BodyCreateFileItemsComponentsUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[CreateFileItemsComponentsUploadPostResponse201ItemType1Type0 | float | str]]
    """

    kwargs = _get_kwargs(
        body=body,
        component_file_type=component_file_type,
        return_speed_only=return_speed_only,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFileItemsComponentsUploadPost,
    component_file_type: ComponentFileType,
    return_speed_only: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> (
    Any | HTTPValidationError | list[CreateFileItemsComponentsUploadPostResponse201ItemType1Type0 | float | str] | None
):
    """Create File Items

     Create component from uploaded file.

    Returns the created file item ID and any extracted data needed by the UI in a dict.

    Args:
        component_file_type (ComponentFileType): Types of files.
        return_speed_only (bool | Unset):  Default: True.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (BodyCreateFileItemsComponentsUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[CreateFileItemsComponentsUploadPostResponse201ItemType1Type0 | float | str]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            component_file_type=component_file_type,
            return_speed_only=return_speed_only,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
