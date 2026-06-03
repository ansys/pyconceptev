from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.job import Job
from ...models.job_input import JobInput
from ...models.uploaded_file import UploadedFile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: JobInput,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    account_id: str,
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

    params["account_id"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/jobs",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[Job | UploadedFile] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(data: object) -> Job | UploadedFile:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_0 = Job.from_dict(data)

                    return response_200_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_1 = UploadedFile.from_dict(data)

                return response_200_item_type_1

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | HTTPValidationError | list[Job | UploadedFile]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: JobInput,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    account_id: str,
) -> Response[Any | HTTPValidationError | list[Job | UploadedFile]]:
    """Create Requirement Job

     Create job for a requirement and architecture.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        account_id (str):
        body (JobInput): Job Input.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[Job | UploadedFile]]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: JobInput,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    account_id: str,
) -> Any | HTTPValidationError | list[Job | UploadedFile] | None:
    """Create Requirement Job

     Create job for a requirement and architecture.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        account_id (str):
        body (JobInput): Job Input.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[Job | UploadedFile]
    """

    return sync_detailed(
        client=client,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: JobInput,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    account_id: str,
) -> Response[Any | HTTPValidationError | list[Job | UploadedFile]]:
    """Create Requirement Job

     Create job for a requirement and architecture.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        account_id (str):
        body (JobInput): Job Input.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[Job | UploadedFile]]
    """

    kwargs = _get_kwargs(
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: JobInput,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    account_id: str,
) -> Any | HTTPValidationError | list[Job | UploadedFile] | None:
    """Create Requirement Job

     Create job for a requirement and architecture.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        account_id (str):
        body (JobInput): Job Input.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[Job | UploadedFile]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            design_id=design_id,
            design_instance_id=design_instance_id,
            account_id=account_id,
        )
    ).parsed
