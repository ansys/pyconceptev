from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.concept_id_response import ConceptIdResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    design_identifier: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/concept/{design_identifier}/id".format(
            design_identifier=quote(str(design_identifier), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConceptIdResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ConceptIdResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConceptIdResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    design_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ConceptIdResponse | HTTPValidationError]:
    """Get Concept Id

     Get the concept id for a given design_id or design_instance_id.

    Args:
        design_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConceptIdResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        design_identifier=design_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    design_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> ConceptIdResponse | HTTPValidationError | None:
    """Get Concept Id

     Get the concept id for a given design_id or design_instance_id.

    Args:
        design_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConceptIdResponse | HTTPValidationError
    """

    return sync_detailed(
        design_identifier=design_identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    design_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ConceptIdResponse | HTTPValidationError]:
    """Get Concept Id

     Get the concept id for a given design_id or design_instance_id.

    Args:
        design_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConceptIdResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        design_identifier=design_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    design_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> ConceptIdResponse | HTTPValidationError | None:
    """Get Concept Id

     Get the concept id for a given design_id or design_instance_id.

    Args:
        design_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConceptIdResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            design_identifier=design_identifier,
            client=client,
        )
    ).parsed
