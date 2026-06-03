from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.battery_fixed_voltages import BatteryFixedVoltages
from ...models.battery_fixed_voltages_in_db import BatteryFixedVoltagesInDB
from ...models.battery_lookup_table import BatteryLookupTable
from ...models.battery_lookup_table_id import BatteryLookupTableID
from ...models.battery_lookup_table_in_db import BatteryLookupTableInDB
from ...models.disconnect_clutch_input import DisconnectClutchInput
from ...models.disconnect_clutch_input_in_db import DisconnectClutchInputInDB
from ...models.http_validation_error import HTTPValidationError
from ...models.inverter_analytical import InverterAnalytical
from ...models.inverter_analytical_in_db import InverterAnalyticalInDB
from ...models.inverter_loss_map_id import InverterLossMapID
from ...models.item_and_blobs import ItemAndBlobs
from ...models.motor_lab import MotorLab
from ...models.motor_lab_id import MotorLabID
from ...models.motor_lab_in_db import MotorLabInDB
from ...models.motor_loss_map import MotorLossMap
from ...models.motor_loss_map_id import MotorLossMapID
from ...models.motor_loss_map_in_db import MotorLossMapInDB
from ...models.motor_torque_curves import MotorTorqueCurves
from ...models.motor_torque_curves_id import MotorTorqueCurvesID
from ...models.motor_torque_curves_in_db import MotorTorqueCurvesInDB
from ...models.transmission_loss_coefficients import TransmissionLossCoefficients
from ...models.transmission_loss_coefficients_in_db import TransmissionLossCoefficientsInDB
from ...models.transmission_loss_map import TransmissionLossMap
from ...models.transmission_loss_map_id import TransmissionLossMapID
from ...models.transmission_loss_map_in_db import TransmissionLossMapInDB
from ...models.transmission_neglect import TransmissionNeglect
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BatteryFixedVoltages
    | BatteryLookupTable
    | BatteryLookupTableID
    | DisconnectClutchInput
    | InverterAnalytical
    | InverterLossMapID
    | ItemAndBlobs
    | MotorLab
    | MotorLabID
    | MotorLossMap
    | MotorLossMapID
    | MotorTorqueCurves
    | MotorTorqueCurvesID
    | TransmissionLossCoefficients
    | TransmissionLossMap
    | TransmissionLossMapID
    | TransmissionNeglect,
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
        "url": "/components",
        "params": params,
    }

    if isinstance(body, BatteryFixedVoltages):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, BatteryLookupTable):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MotorTorqueCurves):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MotorLossMap):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MotorLab):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, TransmissionLossCoefficients):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, TransmissionLossMap):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, TransmissionNeglect):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, InverterAnalytical):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DisconnectClutchInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MotorLossMapID):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MotorLabID):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MotorTorqueCurvesID):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, BatteryLookupTableID):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, TransmissionLossMapID):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, InverterLossMapID):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | BatteryFixedVoltagesInDB
    | BatteryLookupTableID
    | BatteryLookupTableInDB
    | DisconnectClutchInputInDB
    | InverterAnalyticalInDB
    | InverterLossMapID
    | MotorLabID
    | MotorLabInDB
    | MotorLossMapID
    | MotorLossMapInDB
    | MotorTorqueCurvesID
    | MotorTorqueCurvesInDB
    | TransmissionLossCoefficientsInDB
    | TransmissionLossMapID
    | TransmissionLossMapInDB
    | HTTPValidationError
    | None
):
    if response.status_code == 201:

        def _parse_response_201(
            data: object,
        ) -> (
            BatteryFixedVoltagesInDB
            | BatteryLookupTableID
            | BatteryLookupTableInDB
            | DisconnectClutchInputInDB
            | InverterAnalyticalInDB
            | InverterLossMapID
            | MotorLabID
            | MotorLabInDB
            | MotorLossMapID
            | MotorLossMapInDB
            | MotorTorqueCurvesID
            | MotorTorqueCurvesInDB
            | TransmissionLossCoefficientsInDB
            | TransmissionLossMapID
            | TransmissionLossMapInDB
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_0 = BatteryFixedVoltagesInDB.from_dict(data)

                return componentsschemas_component_in_db_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_1 = TransmissionLossCoefficientsInDB.from_dict(data)

                return componentsschemas_component_in_db_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_2 = DisconnectClutchInputInDB.from_dict(data)

                return componentsschemas_component_in_db_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_3 = InverterAnalyticalInDB.from_dict(data)

                return componentsschemas_component_in_db_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_4 = MotorLossMapID.from_dict(data)

                return componentsschemas_component_in_db_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_5 = MotorLabID.from_dict(data)

                return componentsschemas_component_in_db_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_6 = MotorTorqueCurvesID.from_dict(data)

                return componentsschemas_component_in_db_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_7 = BatteryLookupTableID.from_dict(data)

                return componentsschemas_component_in_db_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_8 = TransmissionLossMapID.from_dict(data)

                return componentsschemas_component_in_db_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_9 = InverterLossMapID.from_dict(data)

                return componentsschemas_component_in_db_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_10 = BatteryLookupTableInDB.from_dict(data)

                return componentsschemas_component_in_db_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_11 = MotorTorqueCurvesInDB.from_dict(data)

                return componentsschemas_component_in_db_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_12 = TransmissionLossMapInDB.from_dict(data)

                return componentsschemas_component_in_db_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_13 = MotorLabInDB.from_dict(data)

                return componentsschemas_component_in_db_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_component_in_db_type_14 = MotorLossMapInDB.from_dict(data)

            return componentsschemas_component_in_db_type_14

        response_201 = _parse_response_201(response.json())

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
    Any
    | BatteryFixedVoltagesInDB
    | BatteryLookupTableID
    | BatteryLookupTableInDB
    | DisconnectClutchInputInDB
    | InverterAnalyticalInDB
    | InverterLossMapID
    | MotorLabID
    | MotorLabInDB
    | MotorLossMapID
    | MotorLossMapInDB
    | MotorTorqueCurvesID
    | MotorTorqueCurvesInDB
    | TransmissionLossCoefficientsInDB
    | TransmissionLossMapID
    | TransmissionLossMapInDB
    | HTTPValidationError
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
    body: BatteryFixedVoltages
    | BatteryLookupTable
    | BatteryLookupTableID
    | DisconnectClutchInput
    | InverterAnalytical
    | InverterLossMapID
    | ItemAndBlobs
    | MotorLab
    | MotorLabID
    | MotorLossMap
    | MotorLossMapID
    | MotorTorqueCurves
    | MotorTorqueCurvesID
    | TransmissionLossCoefficients
    | TransmissionLossMap
    | TransmissionLossMapID
    | TransmissionNeglect,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[
    Any
    | BatteryFixedVoltagesInDB
    | BatteryLookupTableID
    | BatteryLookupTableInDB
    | DisconnectClutchInputInDB
    | InverterAnalyticalInDB
    | InverterLossMapID
    | MotorLabID
    | MotorLabInDB
    | MotorLossMapID
    | MotorLossMapInDB
    | MotorTorqueCurvesID
    | MotorTorqueCurvesInDB
    | TransmissionLossCoefficientsInDB
    | TransmissionLossMapID
    | TransmissionLossMapInDB
    | HTTPValidationError
]:
    """Create

     Create from parameters.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (BatteryFixedVoltages | BatteryLookupTable | BatteryLookupTableID |
            DisconnectClutchInput | InverterAnalytical | InverterLossMapID | ItemAndBlobs | MotorLab |
            MotorLabID | MotorLossMap | MotorLossMapID | MotorTorqueCurves | MotorTorqueCurvesID |
            TransmissionLossCoefficients | TransmissionLossMap | TransmissionLossMapID |
            TransmissionNeglect):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BatteryFixedVoltagesInDB | BatteryLookupTableID | BatteryLookupTableInDB | DisconnectClutchInputInDB | InverterAnalyticalInDB | InverterLossMapID | MotorLabID | MotorLabInDB | MotorLossMapID | MotorLossMapInDB | MotorTorqueCurvesID | MotorTorqueCurvesInDB | TransmissionLossCoefficientsInDB | TransmissionLossMapID | TransmissionLossMapInDB | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: BatteryFixedVoltages
    | BatteryLookupTable
    | BatteryLookupTableID
    | DisconnectClutchInput
    | InverterAnalytical
    | InverterLossMapID
    | ItemAndBlobs
    | MotorLab
    | MotorLabID
    | MotorLossMap
    | MotorLossMapID
    | MotorTorqueCurves
    | MotorTorqueCurvesID
    | TransmissionLossCoefficients
    | TransmissionLossMap
    | TransmissionLossMapID
    | TransmissionNeglect,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> (
    Any
    | BatteryFixedVoltagesInDB
    | BatteryLookupTableID
    | BatteryLookupTableInDB
    | DisconnectClutchInputInDB
    | InverterAnalyticalInDB
    | InverterLossMapID
    | MotorLabID
    | MotorLabInDB
    | MotorLossMapID
    | MotorLossMapInDB
    | MotorTorqueCurvesID
    | MotorTorqueCurvesInDB
    | TransmissionLossCoefficientsInDB
    | TransmissionLossMapID
    | TransmissionLossMapInDB
    | HTTPValidationError
    | None
):
    """Create

     Create from parameters.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (BatteryFixedVoltages | BatteryLookupTable | BatteryLookupTableID |
            DisconnectClutchInput | InverterAnalytical | InverterLossMapID | ItemAndBlobs | MotorLab |
            MotorLabID | MotorLossMap | MotorLossMapID | MotorTorqueCurves | MotorTorqueCurvesID |
            TransmissionLossCoefficients | TransmissionLossMap | TransmissionLossMapID |
            TransmissionNeglect):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BatteryFixedVoltagesInDB | BatteryLookupTableID | BatteryLookupTableInDB | DisconnectClutchInputInDB | InverterAnalyticalInDB | InverterLossMapID | MotorLabID | MotorLabInDB | MotorLossMapID | MotorLossMapInDB | MotorTorqueCurvesID | MotorTorqueCurvesInDB | TransmissionLossCoefficientsInDB | TransmissionLossMapID | TransmissionLossMapInDB | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BatteryFixedVoltages
    | BatteryLookupTable
    | BatteryLookupTableID
    | DisconnectClutchInput
    | InverterAnalytical
    | InverterLossMapID
    | ItemAndBlobs
    | MotorLab
    | MotorLabID
    | MotorLossMap
    | MotorLossMapID
    | MotorTorqueCurves
    | MotorTorqueCurvesID
    | TransmissionLossCoefficients
    | TransmissionLossMap
    | TransmissionLossMapID
    | TransmissionNeglect,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[
    Any
    | BatteryFixedVoltagesInDB
    | BatteryLookupTableID
    | BatteryLookupTableInDB
    | DisconnectClutchInputInDB
    | InverterAnalyticalInDB
    | InverterLossMapID
    | MotorLabID
    | MotorLabInDB
    | MotorLossMapID
    | MotorLossMapInDB
    | MotorTorqueCurvesID
    | MotorTorqueCurvesInDB
    | TransmissionLossCoefficientsInDB
    | TransmissionLossMapID
    | TransmissionLossMapInDB
    | HTTPValidationError
]:
    """Create

     Create from parameters.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (BatteryFixedVoltages | BatteryLookupTable | BatteryLookupTableID |
            DisconnectClutchInput | InverterAnalytical | InverterLossMapID | ItemAndBlobs | MotorLab |
            MotorLabID | MotorLossMap | MotorLossMapID | MotorTorqueCurves | MotorTorqueCurvesID |
            TransmissionLossCoefficients | TransmissionLossMap | TransmissionLossMapID |
            TransmissionNeglect):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BatteryFixedVoltagesInDB | BatteryLookupTableID | BatteryLookupTableInDB | DisconnectClutchInputInDB | InverterAnalyticalInDB | InverterLossMapID | MotorLabID | MotorLabInDB | MotorLossMapID | MotorLossMapInDB | MotorTorqueCurvesID | MotorTorqueCurvesInDB | TransmissionLossCoefficientsInDB | TransmissionLossMapID | TransmissionLossMapInDB | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BatteryFixedVoltages
    | BatteryLookupTable
    | BatteryLookupTableID
    | DisconnectClutchInput
    | InverterAnalytical
    | InverterLossMapID
    | ItemAndBlobs
    | MotorLab
    | MotorLabID
    | MotorLossMap
    | MotorLossMapID
    | MotorTorqueCurves
    | MotorTorqueCurvesID
    | TransmissionLossCoefficients
    | TransmissionLossMap
    | TransmissionLossMapID
    | TransmissionNeglect,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> (
    Any
    | BatteryFixedVoltagesInDB
    | BatteryLookupTableID
    | BatteryLookupTableInDB
    | DisconnectClutchInputInDB
    | InverterAnalyticalInDB
    | InverterLossMapID
    | MotorLabID
    | MotorLabInDB
    | MotorLossMapID
    | MotorLossMapInDB
    | MotorTorqueCurvesID
    | MotorTorqueCurvesInDB
    | TransmissionLossCoefficientsInDB
    | TransmissionLossMapID
    | TransmissionLossMapInDB
    | HTTPValidationError
    | None
):
    """Create

     Create from parameters.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (BatteryFixedVoltages | BatteryLookupTable | BatteryLookupTableID |
            DisconnectClutchInput | InverterAnalytical | InverterLossMapID | ItemAndBlobs | MotorLab |
            MotorLabID | MotorLossMap | MotorLossMapID | MotorTorqueCurves | MotorTorqueCurvesID |
            TransmissionLossCoefficients | TransmissionLossMap | TransmissionLossMapID |
            TransmissionNeglect):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BatteryFixedVoltagesInDB | BatteryLookupTableID | BatteryLookupTableInDB | DisconnectClutchInputInDB | InverterAnalyticalInDB | InverterLossMapID | MotorLabID | MotorLabInDB | MotorLossMapID | MotorLossMapInDB | MotorTorqueCurvesID | MotorTorqueCurvesInDB | TransmissionLossCoefficientsInDB | TransmissionLossMapID | TransmissionLossMapInDB | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
