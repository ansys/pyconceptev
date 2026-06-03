from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exchange_file import ExchangeFile
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    get_jobs: bool | Unset = False,
    get_s3_files: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["get_jobs"] = get_jobs

    params["get_s3_files"] = get_s3_files

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
        "url": "/concepts:export",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ExchangeFile | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ExchangeFile.from_dict(response.json())

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
) -> Response[Any | ExchangeFile | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    get_jobs: bool | Unset = False,
    get_s3_files: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | ExchangeFile | HTTPValidationError]:
    """Export Concept

     Export Concept to Exchange File.

    Args:
        get_jobs (bool | Unset):  Default: False.
        get_s3_files (bool | Unset):  Default: True.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExchangeFile | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        get_jobs=get_jobs,
        get_s3_files=get_s3_files,
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
    get_jobs: bool | Unset = False,
    get_s3_files: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | ExchangeFile | HTTPValidationError | None:
    """Export Concept

     Export Concept to Exchange File.

    Args:
        get_jobs (bool | Unset):  Default: False.
        get_s3_files (bool | Unset):  Default: True.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExchangeFile | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        get_jobs=get_jobs,
        get_s3_files=get_s3_files,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    get_jobs: bool | Unset = False,
    get_s3_files: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | ExchangeFile | HTTPValidationError]:
    """Export Concept

     Export Concept to Exchange File.

    Args:
        get_jobs (bool | Unset):  Default: False.
        get_s3_files (bool | Unset):  Default: True.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExchangeFile | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        get_jobs=get_jobs,
        get_s3_files=get_s3_files,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    get_jobs: bool | Unset = False,
    get_s3_files: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | ExchangeFile | HTTPValidationError | None:
    """Export Concept

     Export Concept to Exchange File.

    Args:
        get_jobs (bool | Unset):  Default: False.
        get_s3_files (bool | Unset):  Default: True.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExchangeFile | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            get_jobs=get_jobs,
            get_s3_files=get_s3_files,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
