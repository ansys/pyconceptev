from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.aero import Aero
from ...models.ancillary_load import AncillaryLoad
from ...models.battery_fixed_voltages import BatteryFixedVoltages
from ...models.battery_lookup_table import BatteryLookupTable
from ...models.battery_lookup_table_id import BatteryLookupTableID
from ...models.deceleration_limit import DecelerationLimit
from ...models.disconnect_clutch_input import DisconnectClutchInput
from ...models.drive_cycle import DriveCycle
from ...models.http_validation_error import HTTPValidationError
from ...models.inverter_analytical import InverterAnalytical
from ...models.inverter_loss_map_id import InverterLossMapID
from ...models.item_and_blobs import ItemAndBlobs
from ...models.mass import Mass
from ...models.motor_lab import MotorLab
from ...models.motor_lab_id import MotorLabID
from ...models.motor_loss_map import MotorLossMap
from ...models.motor_loss_map_id import MotorLossMapID
from ...models.motor_torque_curves import MotorTorqueCurves
from ...models.motor_torque_curves_id import MotorTorqueCurvesID
from ...models.transmission_loss_coefficients import TransmissionLossCoefficients
from ...models.transmission_loss_map import TransmissionLossMap
from ...models.transmission_loss_map_id import TransmissionLossMapID
from ...models.transmission_neglect import TransmissionNeglect
from ...models.wheel_input import WheelInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Aero
    | AncillaryLoad
    | BatteryFixedVoltages
    | BatteryLookupTable
    | BatteryLookupTableID
    | DecelerationLimit
    | DisconnectClutchInput
    | DriveCycle
    | InverterAnalytical
    | InverterLossMapID
    | ItemAndBlobs
    | Mass
    | MotorLab
    | MotorLabID
    | MotorLossMap
    | MotorLossMapID
    | MotorTorqueCurves
    | MotorTorqueCurvesID
    | TransmissionLossCoefficients
    | TransmissionLossMap
    | TransmissionLossMapID
    | TransmissionNeglect
    | WheelInput,
    account_id: str,
    product_id: str,
    description: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params["product_id"] = product_id

    params["description"] = description

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
        "url": "/library:direct_upload",
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
    elif isinstance(body, Aero):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, Mass):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, WheelInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DecelerationLimit):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, AncillaryLoad):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DriveCycle):
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
    | HTTPValidationError
    | list[
        Aero
        | AncillaryLoad
        | BatteryFixedVoltages
        | BatteryLookupTable
        | BatteryLookupTableID
        | DecelerationLimit
        | DisconnectClutchInput
        | DriveCycle
        | InverterAnalytical
        | InverterLossMapID
        | ItemAndBlobs
        | Mass
        | MotorLab
        | MotorLabID
        | MotorLossMap
        | MotorLossMapID
        | MotorTorqueCurves
        | MotorTorqueCurvesID
        | str
        | TransmissionLossCoefficients
        | TransmissionLossMap
        | TransmissionLossMapID
        | TransmissionNeglect
        | WheelInput
    ]
    | None
):
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:

            def _parse_response_201_item(
                data: object,
            ) -> (
                Aero
                | AncillaryLoad
                | BatteryFixedVoltages
                | BatteryLookupTable
                | BatteryLookupTableID
                | DecelerationLimit
                | DisconnectClutchInput
                | DriveCycle
                | InverterAnalytical
                | InverterLossMapID
                | ItemAndBlobs
                | Mass
                | MotorLab
                | MotorLabID
                | MotorLossMap
                | MotorLossMapID
                | MotorTorqueCurves
                | MotorTorqueCurvesID
                | str
                | TransmissionLossCoefficients
                | TransmissionLossMap
                | TransmissionLossMapID
                | TransmissionNeglect
                | WheelInput
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_0 = BatteryFixedVoltages.from_dict(data)

                    return response_201_item_type_1_type_0_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_1 = BatteryLookupTable.from_dict(data)

                    return response_201_item_type_1_type_0_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_2 = MotorTorqueCurves.from_dict(data)

                    return response_201_item_type_1_type_0_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_3 = MotorLossMap.from_dict(data)

                    return response_201_item_type_1_type_0_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_4 = MotorLab.from_dict(data)

                    return response_201_item_type_1_type_0_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_5 = TransmissionLossCoefficients.from_dict(data)

                    return response_201_item_type_1_type_0_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_6 = TransmissionLossMap.from_dict(data)

                    return response_201_item_type_1_type_0_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_7 = TransmissionNeglect.from_dict(data)

                    return response_201_item_type_1_type_0_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_8 = InverterAnalytical.from_dict(data)

                    return response_201_item_type_1_type_0_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_9 = DisconnectClutchInput.from_dict(data)

                    return response_201_item_type_1_type_0_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_10 = MotorLossMapID.from_dict(data)

                    return response_201_item_type_1_type_0_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_11 = MotorLabID.from_dict(data)

                    return response_201_item_type_1_type_0_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_12 = MotorTorqueCurvesID.from_dict(data)

                    return response_201_item_type_1_type_0_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_13 = BatteryLookupTableID.from_dict(data)

                    return response_201_item_type_1_type_0_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_14 = TransmissionLossMapID.from_dict(data)

                    return response_201_item_type_1_type_0_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_0_type_15 = InverterLossMapID.from_dict(data)

                    return response_201_item_type_1_type_0_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_1_type_0 = Aero.from_dict(data)

                    return response_201_item_type_1_type_1_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_1_type_1 = Mass.from_dict(data)

                    return response_201_item_type_1_type_1_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_1_type_2 = WheelInput.from_dict(data)

                    return response_201_item_type_1_type_1_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_1_type_3 = DecelerationLimit.from_dict(data)

                    return response_201_item_type_1_type_1_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_1_type_4 = AncillaryLoad.from_dict(data)

                    return response_201_item_type_1_type_1_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_2 = DriveCycle.from_dict(data)

                    return response_201_item_type_1_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1_type_3 = ItemAndBlobs.from_dict(data)

                    return response_201_item_type_1_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(
                    Aero
                    | AncillaryLoad
                    | BatteryFixedVoltages
                    | BatteryLookupTable
                    | BatteryLookupTableID
                    | DecelerationLimit
                    | DisconnectClutchInput
                    | DriveCycle
                    | InverterAnalytical
                    | InverterLossMapID
                    | ItemAndBlobs
                    | Mass
                    | MotorLab
                    | MotorLabID
                    | MotorLossMap
                    | MotorLossMapID
                    | MotorTorqueCurves
                    | MotorTorqueCurvesID
                    | str
                    | TransmissionLossCoefficients
                    | TransmissionLossMap
                    | TransmissionLossMapID
                    | TransmissionNeglect
                    | WheelInput,
                    data,
                )

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
    Any
    | HTTPValidationError
    | list[
        Aero
        | AncillaryLoad
        | BatteryFixedVoltages
        | BatteryLookupTable
        | BatteryLookupTableID
        | DecelerationLimit
        | DisconnectClutchInput
        | DriveCycle
        | InverterAnalytical
        | InverterLossMapID
        | ItemAndBlobs
        | Mass
        | MotorLab
        | MotorLabID
        | MotorLossMap
        | MotorLossMapID
        | MotorTorqueCurves
        | MotorTorqueCurvesID
        | str
        | TransmissionLossCoefficients
        | TransmissionLossMap
        | TransmissionLossMapID
        | TransmissionNeglect
        | WheelInput
    ]
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
    body: Aero
    | AncillaryLoad
    | BatteryFixedVoltages
    | BatteryLookupTable
    | BatteryLookupTableID
    | DecelerationLimit
    | DisconnectClutchInput
    | DriveCycle
    | InverterAnalytical
    | InverterLossMapID
    | ItemAndBlobs
    | Mass
    | MotorLab
    | MotorLabID
    | MotorLossMap
    | MotorLossMapID
    | MotorTorqueCurves
    | MotorTorqueCurvesID
    | TransmissionLossCoefficients
    | TransmissionLossMap
    | TransmissionLossMapID
    | TransmissionNeglect
    | WheelInput,
    account_id: str,
    product_id: str,
    description: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[
    Any
    | HTTPValidationError
    | list[
        Aero
        | AncillaryLoad
        | BatteryFixedVoltages
        | BatteryLookupTable
        | BatteryLookupTableID
        | DecelerationLimit
        | DisconnectClutchInput
        | DriveCycle
        | InverterAnalytical
        | InverterLossMapID
        | ItemAndBlobs
        | Mass
        | MotorLab
        | MotorLabID
        | MotorLossMap
        | MotorLossMapID
        | MotorTorqueCurves
        | MotorTorqueCurvesID
        | str
        | TransmissionLossCoefficients
        | TransmissionLossMap
        | TransmissionLossMapID
        | TransmissionNeglect
        | WheelInput
    ]
]:
    """Add To Library Direct

     Upload a config or component directly to the library.

    Args:
        account_id (str):
        product_id (str):
        description (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (Aero | AncillaryLoad | BatteryFixedVoltages | BatteryLookupTable |
            BatteryLookupTableID | DecelerationLimit | DisconnectClutchInput | DriveCycle |
            InverterAnalytical | InverterLossMapID | ItemAndBlobs | Mass | MotorLab | MotorLabID |
            MotorLossMap | MotorLossMapID | MotorTorqueCurves | MotorTorqueCurvesID |
            TransmissionLossCoefficients | TransmissionLossMap | TransmissionLossMapID |
            TransmissionNeglect | WheelInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[Aero | AncillaryLoad | BatteryFixedVoltages | BatteryLookupTable | BatteryLookupTableID | DecelerationLimit | DisconnectClutchInput | DriveCycle | InverterAnalytical | InverterLossMapID | ItemAndBlobs | Mass | MotorLab | MotorLabID | MotorLossMap | MotorLossMapID | MotorTorqueCurves | MotorTorqueCurvesID | str | TransmissionLossCoefficients | TransmissionLossMap | TransmissionLossMapID | TransmissionNeglect | WheelInput]]
    """

    kwargs = _get_kwargs(
        body=body,
        account_id=account_id,
        product_id=product_id,
        description=description,
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
    body: Aero
    | AncillaryLoad
    | BatteryFixedVoltages
    | BatteryLookupTable
    | BatteryLookupTableID
    | DecelerationLimit
    | DisconnectClutchInput
    | DriveCycle
    | InverterAnalytical
    | InverterLossMapID
    | ItemAndBlobs
    | Mass
    | MotorLab
    | MotorLabID
    | MotorLossMap
    | MotorLossMapID
    | MotorTorqueCurves
    | MotorTorqueCurvesID
    | TransmissionLossCoefficients
    | TransmissionLossMap
    | TransmissionLossMapID
    | TransmissionNeglect
    | WheelInput,
    account_id: str,
    product_id: str,
    description: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> (
    Any
    | HTTPValidationError
    | list[
        Aero
        | AncillaryLoad
        | BatteryFixedVoltages
        | BatteryLookupTable
        | BatteryLookupTableID
        | DecelerationLimit
        | DisconnectClutchInput
        | DriveCycle
        | InverterAnalytical
        | InverterLossMapID
        | ItemAndBlobs
        | Mass
        | MotorLab
        | MotorLabID
        | MotorLossMap
        | MotorLossMapID
        | MotorTorqueCurves
        | MotorTorqueCurvesID
        | str
        | TransmissionLossCoefficients
        | TransmissionLossMap
        | TransmissionLossMapID
        | TransmissionNeglect
        | WheelInput
    ]
    | None
):
    """Add To Library Direct

     Upload a config or component directly to the library.

    Args:
        account_id (str):
        product_id (str):
        description (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (Aero | AncillaryLoad | BatteryFixedVoltages | BatteryLookupTable |
            BatteryLookupTableID | DecelerationLimit | DisconnectClutchInput | DriveCycle |
            InverterAnalytical | InverterLossMapID | ItemAndBlobs | Mass | MotorLab | MotorLabID |
            MotorLossMap | MotorLossMapID | MotorTorqueCurves | MotorTorqueCurvesID |
            TransmissionLossCoefficients | TransmissionLossMap | TransmissionLossMapID |
            TransmissionNeglect | WheelInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[Aero | AncillaryLoad | BatteryFixedVoltages | BatteryLookupTable | BatteryLookupTableID | DecelerationLimit | DisconnectClutchInput | DriveCycle | InverterAnalytical | InverterLossMapID | ItemAndBlobs | Mass | MotorLab | MotorLabID | MotorLossMap | MotorLossMapID | MotorTorqueCurves | MotorTorqueCurvesID | str | TransmissionLossCoefficients | TransmissionLossMap | TransmissionLossMapID | TransmissionNeglect | WheelInput]
    """

    return sync_detailed(
        client=client,
        body=body,
        account_id=account_id,
        product_id=product_id,
        description=description,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Aero
    | AncillaryLoad
    | BatteryFixedVoltages
    | BatteryLookupTable
    | BatteryLookupTableID
    | DecelerationLimit
    | DisconnectClutchInput
    | DriveCycle
    | InverterAnalytical
    | InverterLossMapID
    | ItemAndBlobs
    | Mass
    | MotorLab
    | MotorLabID
    | MotorLossMap
    | MotorLossMapID
    | MotorTorqueCurves
    | MotorTorqueCurvesID
    | TransmissionLossCoefficients
    | TransmissionLossMap
    | TransmissionLossMapID
    | TransmissionNeglect
    | WheelInput,
    account_id: str,
    product_id: str,
    description: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[
    Any
    | HTTPValidationError
    | list[
        Aero
        | AncillaryLoad
        | BatteryFixedVoltages
        | BatteryLookupTable
        | BatteryLookupTableID
        | DecelerationLimit
        | DisconnectClutchInput
        | DriveCycle
        | InverterAnalytical
        | InverterLossMapID
        | ItemAndBlobs
        | Mass
        | MotorLab
        | MotorLabID
        | MotorLossMap
        | MotorLossMapID
        | MotorTorqueCurves
        | MotorTorqueCurvesID
        | str
        | TransmissionLossCoefficients
        | TransmissionLossMap
        | TransmissionLossMapID
        | TransmissionNeglect
        | WheelInput
    ]
]:
    """Add To Library Direct

     Upload a config or component directly to the library.

    Args:
        account_id (str):
        product_id (str):
        description (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (Aero | AncillaryLoad | BatteryFixedVoltages | BatteryLookupTable |
            BatteryLookupTableID | DecelerationLimit | DisconnectClutchInput | DriveCycle |
            InverterAnalytical | InverterLossMapID | ItemAndBlobs | Mass | MotorLab | MotorLabID |
            MotorLossMap | MotorLossMapID | MotorTorqueCurves | MotorTorqueCurvesID |
            TransmissionLossCoefficients | TransmissionLossMap | TransmissionLossMapID |
            TransmissionNeglect | WheelInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[Aero | AncillaryLoad | BatteryFixedVoltages | BatteryLookupTable | BatteryLookupTableID | DecelerationLimit | DisconnectClutchInput | DriveCycle | InverterAnalytical | InverterLossMapID | ItemAndBlobs | Mass | MotorLab | MotorLabID | MotorLossMap | MotorLossMapID | MotorTorqueCurves | MotorTorqueCurvesID | str | TransmissionLossCoefficients | TransmissionLossMap | TransmissionLossMapID | TransmissionNeglect | WheelInput]]
    """

    kwargs = _get_kwargs(
        body=body,
        account_id=account_id,
        product_id=product_id,
        description=description,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Aero
    | AncillaryLoad
    | BatteryFixedVoltages
    | BatteryLookupTable
    | BatteryLookupTableID
    | DecelerationLimit
    | DisconnectClutchInput
    | DriveCycle
    | InverterAnalytical
    | InverterLossMapID
    | ItemAndBlobs
    | Mass
    | MotorLab
    | MotorLabID
    | MotorLossMap
    | MotorLossMapID
    | MotorTorqueCurves
    | MotorTorqueCurvesID
    | TransmissionLossCoefficients
    | TransmissionLossMap
    | TransmissionLossMapID
    | TransmissionNeglect
    | WheelInput,
    account_id: str,
    product_id: str,
    description: str,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> (
    Any
    | HTTPValidationError
    | list[
        Aero
        | AncillaryLoad
        | BatteryFixedVoltages
        | BatteryLookupTable
        | BatteryLookupTableID
        | DecelerationLimit
        | DisconnectClutchInput
        | DriveCycle
        | InverterAnalytical
        | InverterLossMapID
        | ItemAndBlobs
        | Mass
        | MotorLab
        | MotorLabID
        | MotorLossMap
        | MotorLossMapID
        | MotorTorqueCurves
        | MotorTorqueCurvesID
        | str
        | TransmissionLossCoefficients
        | TransmissionLossMap
        | TransmissionLossMapID
        | TransmissionNeglect
        | WheelInput
    ]
    | None
):
    """Add To Library Direct

     Upload a config or component directly to the library.

    Args:
        account_id (str):
        product_id (str):
        description (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (Aero | AncillaryLoad | BatteryFixedVoltages | BatteryLookupTable |
            BatteryLookupTableID | DecelerationLimit | DisconnectClutchInput | DriveCycle |
            InverterAnalytical | InverterLossMapID | ItemAndBlobs | Mass | MotorLab | MotorLabID |
            MotorLossMap | MotorLossMapID | MotorTorqueCurves | MotorTorqueCurvesID |
            TransmissionLossCoefficients | TransmissionLossMap | TransmissionLossMapID |
            TransmissionNeglect | WheelInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[Aero | AncillaryLoad | BatteryFixedVoltages | BatteryLookupTable | BatteryLookupTableID | DecelerationLimit | DisconnectClutchInput | DriveCycle | InverterAnalytical | InverterLossMapID | ItemAndBlobs | Mass | MotorLab | MotorLabID | MotorLossMap | MotorLossMapID | MotorTorqueCurves | MotorTorqueCurvesID | str | TransmissionLossCoefficients | TransmissionLossMap | TransmissionLossMapID | TransmissionNeglect | WheelInput]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_id=account_id,
            product_id=product_id,
            description=description,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
