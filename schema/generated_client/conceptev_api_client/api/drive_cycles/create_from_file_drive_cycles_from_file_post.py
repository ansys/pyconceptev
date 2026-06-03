from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_create_from_file_drive_cycles_from_file_post import BodyCreateFromFileDriveCyclesFromFilePost
from ...models.drive_cycle_in_db import DriveCycleInDB
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyCreateFromFileDriveCyclesFromFilePost,
    drive_cycle_name: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["drive_cycle_name"] = drive_cycle_name

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
        "url": "/drive_cycles:from_file",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DriveCycleInDB | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = DriveCycleInDB.from_dict(response.json())

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
) -> Response[Any | DriveCycleInDB | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFromFileDriveCyclesFromFilePost,
    drive_cycle_name: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | DriveCycleInDB | HTTPValidationError]:
    """Create From File

     Create a requirement from file.

    It can be quite difficult to add anything else to this:
    https://stackoverflow.com/questions/65504438/how-to-add-both-file-and-json-body-in-a-fastapi-post-
    request

    Args:
        drive_cycle_name (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (BodyCreateFromFileDriveCyclesFromFilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DriveCycleInDB | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        drive_cycle_name=drive_cycle_name,
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
    body: BodyCreateFromFileDriveCyclesFromFilePost,
    drive_cycle_name: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | DriveCycleInDB | HTTPValidationError | None:
    """Create From File

     Create a requirement from file.

    It can be quite difficult to add anything else to this:
    https://stackoverflow.com/questions/65504438/how-to-add-both-file-and-json-body-in-a-fastapi-post-
    request

    Args:
        drive_cycle_name (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (BodyCreateFromFileDriveCyclesFromFilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DriveCycleInDB | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        drive_cycle_name=drive_cycle_name,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFromFileDriveCyclesFromFilePost,
    drive_cycle_name: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | DriveCycleInDB | HTTPValidationError]:
    """Create From File

     Create a requirement from file.

    It can be quite difficult to add anything else to this:
    https://stackoverflow.com/questions/65504438/how-to-add-both-file-and-json-body-in-a-fastapi-post-
    request

    Args:
        drive_cycle_name (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (BodyCreateFromFileDriveCyclesFromFilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DriveCycleInDB | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        drive_cycle_name=drive_cycle_name,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFromFileDriveCyclesFromFilePost,
    drive_cycle_name: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | DriveCycleInDB | HTTPValidationError | None:
    """Create From File

     Create a requirement from file.

    It can be quite difficult to add anything else to this:
    https://stackoverflow.com/questions/65504438/how-to-add-both-file-and-json-body-in-a-fastapi-post-
    request

    Args:
        drive_cycle_name (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (BodyCreateFromFileDriveCyclesFromFilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DriveCycleInDB | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            drive_cycle_name=drive_cycle_name,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
