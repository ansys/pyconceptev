from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_create_component_data_from_file_components_upload_file_post import (
    BodyCreateComponentDataFromFileComponentsUploadFilePost,
)
from ...models.file_parameters import FileParameters
from ...models.http_validation_error import HTTPValidationError
from ...models.submitted_job import SubmittedJob
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyCreateComponentDataFromFileComponentsUploadFilePost,
    file_parameters: FileParameters,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    account_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_file_parameters = file_parameters.to_dict()
    params.update(json_file_parameters)

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

    params["account_id"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/components:upload_file",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | SubmittedJob | None:
    if response.status_code == 201:
        response_201 = SubmittedJob.from_dict(response.json())

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
) -> Response[Any | HTTPValidationError | SubmittedJob]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCreateComponentDataFromFileComponentsUploadFilePost,
    file_parameters: FileParameters,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    account_id: str,
) -> Response[Any | HTTPValidationError | SubmittedJob]:
    """Create Component Data From File

     Create component part from uploaded file.

    Args:
        file_parameters (FileParameters): File Parameters.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        account_id (str):
        body (BodyCreateComponentDataFromFileComponentsUploadFilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | SubmittedJob]
    """

    kwargs = _get_kwargs(
        body=body,
        file_parameters=file_parameters,
        design_id=design_id,
        design_instance_id=design_instance_id,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyCreateComponentDataFromFileComponentsUploadFilePost,
    file_parameters: FileParameters,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    account_id: str,
) -> Any | HTTPValidationError | SubmittedJob | None:
    """Create Component Data From File

     Create component part from uploaded file.

    Args:
        file_parameters (FileParameters): File Parameters.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        account_id (str):
        body (BodyCreateComponentDataFromFileComponentsUploadFilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | SubmittedJob
    """

    return sync_detailed(
        client=client,
        body=body,
        file_parameters=file_parameters,
        design_id=design_id,
        design_instance_id=design_instance_id,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCreateComponentDataFromFileComponentsUploadFilePost,
    file_parameters: FileParameters,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    account_id: str,
) -> Response[Any | HTTPValidationError | SubmittedJob]:
    """Create Component Data From File

     Create component part from uploaded file.

    Args:
        file_parameters (FileParameters): File Parameters.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        account_id (str):
        body (BodyCreateComponentDataFromFileComponentsUploadFilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | SubmittedJob]
    """

    kwargs = _get_kwargs(
        body=body,
        file_parameters=file_parameters,
        design_id=design_id,
        design_instance_id=design_instance_id,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyCreateComponentDataFromFileComponentsUploadFilePost,
    file_parameters: FileParameters,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    account_id: str,
) -> Any | HTTPValidationError | SubmittedJob | None:
    """Create Component Data From File

     Create component part from uploaded file.

    Args:
        file_parameters (FileParameters): File Parameters.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        account_id (str):
        body (BodyCreateComponentDataFromFileComponentsUploadFilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | SubmittedJob
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            file_parameters=file_parameters,
            design_id=design_id,
            design_instance_id=design_instance_id,
            account_id=account_id,
        )
    ).parsed
