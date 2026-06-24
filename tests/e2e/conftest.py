# Copyright (C) 2023 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Pytest configuration for the local optiSLang e2e test.

This runs a single full-stack smoke test (``test_optislang_e2e.py``) that drives
an already-installed optiSLang with the ConceptEV integration plugin already
registered: it builds and runs the ConceptEV node against the live ConceptEV API.
There is no provisioning — pyconceptev and the integration plugin are expected to
be installed in optiSLang already.

The ``e2e_optislang`` fixture connects to a running optiSLang instance (or
launches one) and skips gracefully if neither is possible.

Both the pytest-side data setup and optiSLang run against the same ConceptEV
environment: PYCONCEPTEV_SETTINGS is set once here (per --cev-env) and inherited
by the optiSLang subprocess.

Options
-------
  --cev-env prod|test   ConceptEV environment (default: prod). 'prod' uses
                        pyconceptev's bundled config; 'test' uses
                        tests/integration/config.toml.
  --account-name NAME   ConceptEV account name.

optiSLang location is taken from OSL_HOST / OSL_PORT (connect) or OSL_EXECUTABLE
(launch) env vars; see the ``e2e_optislang`` fixture.

Example invocations
-------------------
# Production (default):
    pytest tests/e2e -vv

# Test environment:
    pytest tests/e2e -vv --cev-env test
"""

from contextlib import closing
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys

_TESTS_DIR = Path(__file__).resolve().parent.parent
_E2E_DIR = Path(__file__).resolve().parent
E2E_CONFIG = _E2E_DIR / "config.toml"
DATA_DIR = _TESTS_DIR / "integration"


def _read_cev_env_early() -> str:
    """Resolve the target ConceptEV environment before pytest parses argv.

    Must run before any ansys.conceptev.core import because settings.py reads
    PYCONCEPTEV_SETTINGS at class-definition (module import) time.  Regular
    pytest CLI options are only available in fixtures/hooks — too late.

    Resolution order:
      1. --cev-env <value> on the command line
      2. CEV_E2E_ENV environment variable
      3. "prod" (default)
    """
    for i, arg in enumerate(sys.argv):
        if arg == "--cev-env" and i + 1 < len(sys.argv):
            return sys.argv[i + 1].lower()
        if arg.startswith("--cev-env="):
            return arg.split("=", 1)[1].lower()
    return os.environ.get("CEV_E2E_ENV", "test").lower()


CEV_ENV = _read_cev_env_early()

# ---------------------------------------------------------------------------
# OptiSLang integration injection
# ---------------------------------------------------------------------------

_OSL_INTEGRATIONS_DIR = Path("C:/Program Files/ANSYS Inc/v271/optiSLang/scripting/integrations")
# Python interpreter bundled with optiSLang — used to upgrade packages in-place.
_OSL_PYTHON = Path("C:/Program Files/ANSYS Inc/v271/optiSLang/lib/python3.10/python.exe")

# Configure PYCONCEPTEV_SETTINGS before any ansys.conceptev.core import.
# In prod mode we deliberately leave it unset so pyconceptev uses its bundled
# default production config — exactly what a real user gets.
# In test mode we point it at the shared integration config.toml.
if CEV_ENV == "test":
    os.environ["PYCONCEPTEV_SETTINGS"] = str(E2E_CONFIG)
else:
    os.environ.pop("PYCONCEPTEV_SETTINGS", None)

os.environ.setdefault("PYOPTISLANG_DISABLE_OPTISLANG_OUTPUT", "true")

import pytest  # noqa: E402

from ansys.conceptev.core import app, auth  # noqa: E402
from ansys.conceptev.core.settings import settings as _loaded_settings  # noqa: E402

DEFAULT_OSL_HOST = "127.0.0.1"
DEFAULT_OSL_PORT = 5310


def pytest_configure(config) -> None:
    """Re-affirm env setup in case another plugin imported settings first."""
    if CEV_ENV == "test":
        os.environ["PYCONCEPTEV_SETTINGS"] = str(E2E_CONFIG)
    os.environ.setdefault("PYOPTISLANG_DISABLE_OPTISLANG_OUTPUT", "true")


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--cev-env",
        default="test",
        choices=["prod", "test"],
        help=(
            "ConceptEV environment for both the pytest-side data setup and optiSLang. "
            "'test' uses tests/integration/config.toml (default — v2 API). "
            "'prod' uses pyconceptev's bundled production config. "
            "NOTE: this is read from sys.argv at import time — the value here is "
            "informational and used for validation only."
        ),
    )
    parser.addoption(
        "--account-name",
        default="USEAST2 DEV",
        metavar="NAME",
        help=(
            "ConceptEV account name used for project creation and the optiSLang node. "
            "Overrides the account_name from the active settings. "
            "(default: 'USEAST 2 DEV')"
        ),
    )
    parser.addoption(
        "--integration-dir",
        default=None,
        metavar="PATH",
        help=(
            "Folder containing conceptev_ci.py and the conceptev/ subpackage to inject "
            "into the optiSLang installation for this test session. "
            "Each .py file is copied over its .pye counterpart in the optiSLang "
            "scripting/integrations directory, with the originals restored on teardown. "
            "When omitted, the already-installed integration is used unchanged."
        ),
    )
    parser.addoption(
        "--pyconceptev-source",
        default=None,
        metavar="SRC",
        help=(
            "pip-installable source for ansys-conceptev-core to install into optiSLang's "
            "bundled Python before the test runs. Accepts a local folder path "
            "(e.g. C:/path/to/pyconceptev) or any pip-compatible specifier "
            "(e.g. git+https://github.com/ansys/pyconceptev@branch or a wheel path). "
            "Installed into optiSLang's own Python interpreter "
            f"({_OSL_PYTHON}) so the injected integration can import it. "
            "When omitted, the already-installed version is used unchanged."
        ),
    )


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def e2e_settings():
    """Return the active pyconceptev settings for this session.

    The settings object was loaded at import time from PYCONCEPTEV_SETTINGS (test
    env) or from pyconceptev's bundled default (prod). Both this fixture and the
    optiSLang plugin subprocess inherit the same environment, so they always target
    the same ConceptEV API.

    Also exports CONCEPTEV_PASSWORD to the process environment so optiSLang's
    bundled Python subprocess can pick it up regardless of its working directory
    (pydantic-settings secret-file lookup is CWD-relative).
    """
    if _loaded_settings.conceptev_password and not os.environ.get("CONCEPTEV_PASSWORD"):
        os.environ["CONCEPTEV_PASSWORD"] = _loaded_settings.conceptev_password

    pycv_settings = os.environ.get("PYCONCEPTEV_SETTINGS", "<pyconceptev default>")
    password_set = bool(_loaded_settings.conceptev_password or os.environ.get("CONCEPTEV_PASSWORD"))
    print(
        f"\n[e2e-settings] env={CEV_ENV!r}\n"
        f"  PYCONCEPTEV_SETTINGS={pycv_settings}\n"
        f"  CONCEPTEV_URL={_loaded_settings.conceptev_url}\n"
        f"  ACCOUNT_NAME={_loaded_settings.account_name}\n"
        f"  USERNAME={_loaded_settings.conceptev_username}\n"
        f"  PASSWORD set: {password_set}"
    )
    return _loaded_settings


# ---------------------------------------------------------------------------
# Auth (session-scoped to avoid repeated MSAL round-trips)
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def session_token():
    """Acquire an AnsysID token once per test session."""
    msal = auth.create_msal_app()
    return auth.get_ansyId_token(msal)


@pytest.fixture(scope="session")
def account_name(request: pytest.FixtureRequest) -> str:
    """The ConceptEV account name used for project creation and the optiSLang node."""
    return request.config.getoption("--account-name")


@pytest.fixture(scope="session")
def session_account_id(session_token, account_name):
    accounts = app.get_account_ids(session_token)
    return accounts[account_name]


@pytest.fixture(scope="session")
def session_hpc_id(session_token, session_account_id):
    return app.get_default_hpc(session_token, session_account_id)


# ---------------------------------------------------------------------------
# Fresh e2e concept
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def e2e_concept(session_token, session_account_id, session_hpc_id):
    """Create a fully-populated e2e concept via the v2 API and delete it on teardown.

    The integration's ``get_concept`` call uses ``GET /v2/concept/{id}``, so the
    concept must exist in the v2 registry.  All parts are created through the v2
    ``create_concept_part`` endpoint to guarantee the concept is fully populated
    from the v2 perspective.

    The fixture creates a known-good concept with:

    - MotorLabID rear motor (from the bundled ``e9.lab`` file)
    - BatteryFixedVoltages, TransmissionLossCoefficients
    - Rear-motor architecture
    - Aero / mass / wheel configurations
    - Two static-acceleration requirements (so summary outputs land at _02__summary__)

    Yields the v2 concept ``id`` (the path parameter for ``GET /v2/concept/{id}``).
    """
    from ansys.conceptev.core import ocm as _ocm
    from ansys.conceptev.core.generated.api.concept_v2 import (
        create_concept_part as _create_concept_part,
    )
    from ansys.conceptev.core.generated.api.concept_v2 import create_concept as _create_concept_v2
    from ansys.conceptev.core.generated.api.concept_v2 import create_file_item as _create_file_item
    from ansys.conceptev.core.generated.models.aero_input import AeroInput
    from ansys.conceptev.core.generated.models.architecture_input import ArchitectureInput
    from ansys.conceptev.core.generated.models.battery_fixed_voltages_input import (
        BatteryFixedVoltagesInput,
    )
    from ansys.conceptev.core.generated.models.body_create_file_item import BodyCreateFileItem
    from ansys.conceptev.core.generated.models.concept_input import ConceptInput
    from ansys.conceptev.core.generated.models.mass_input import MassInput
    from ansys.conceptev.core.generated.models.motor_lab_input import MotorLabInput
    from ansys.conceptev.core.generated.models.static_requirement_input import (
        StaticRequirementInput,
    )
    from ansys.conceptev.core.generated.models.transmission_loss_coefficients_input import (
        TransmissionLossCoefficientsInput,
    )
    from ansys.conceptev.core.generated.models.wheel_input import WheelInput
    from ansys.conceptev.core.generated.types import UNSET

    with app.get_http_client(session_token) as v1_client:
        project = app.create_new_project(
            v1_client,
            session_account_id,
            session_hpc_id,
            "E2E Tests – optiSLang connection",
        )
    project_id = project["projectId"]

    product_id = app.get_product_id(session_token)
    design_instance_id, design_id = _ocm.create_design_instance(
        project_id,
        "E2E optiSLang test concept",
        session_token,
        product_id,
        return_design_id=True,
    )

    with app.get_conceptev_client(token=session_token) as opc_client:
        _v2_concept_resp = _create_concept_v2.sync_detailed(
            client=opc_client,
            body=ConceptInput(
                name="E2E optiSLang test concept",
                project_id=project_id,
                design_id=design_id,
                design_instance_id=design_instance_id,
            ),
        )
        print(
            f"[e2e-setup] POST /v2/concept status={_v2_concept_resp.status_code} "
            f"body={_v2_concept_resp.content[:500]!r}"
        )
        v2_concept = _v2_concept_resp.parsed
        if v2_concept is None or not hasattr(v2_concept, "id"):
            pytest.fail(
                f"Failed to create v2 concept via POST /v2/concept "
                f"(status={_v2_concept_resp.status_code}): {_v2_concept_resp.content!r}"
            )
        concept_id = v2_concept.id

        with open(DATA_DIR / "e9.lab", "rb") as fh:
            lab_content = fh.read().decode("latin-1")
        file_resp = _create_file_item.sync(
            id=concept_id,
            client=opc_client,
            body=BodyCreateFileItem(file=lab_content),
            name="e9.lab",
            component_file_type="motor_lab_file",
        )
        if file_resp is None:
            pytest.fail("Failed to upload motor lab file")
        lab_data_id = file_resp.id
        calc = file_resp.calculated_values
        max_speed = 800.0
        if calc is not None and calc is not UNSET:
            calc_dict = calc.to_dict() if hasattr(calc, "to_dict") else {}
            max_speed = calc_dict.get("max_speed", max_speed)

        motor_resp = _create_concept_part.sync(
            id=concept_id,
            part_type="component",
            client=opc_client,
            body=MotorLabInput(
                name="E2E Test Rear Motor",
                max_speed=max_speed,
                lab_data_id=lab_data_id,
            ),
        )
        if motor_resp is None:
            pytest.fail("Failed to create motor component")
        motor_id = motor_resp.id

        battery_resp = _create_concept_part.sync(
            id=concept_id,
            part_type="component",
            client=opc_client,
            body=BatteryFixedVoltagesInput(),
        )
        if battery_resp is None:
            pytest.fail("Failed to create battery component")
        battery_id = battery_resp.id

        transmission_resp = _create_concept_part.sync(
            id=concept_id,
            part_type="component",
            client=opc_client,
            body=TransmissionLossCoefficientsInput(),
        )
        if transmission_resp is None:
            pytest.fail("Failed to create transmission component")
        transmission_id = transmission_resp.id

        _create_concept_part.sync(
            id=concept_id,
            part_type="architecture",
            client=opc_client,
            body=ArchitectureInput(
                battery_id=battery_id,
                number_of_rear_motors=1,
                rear_motor_id=motor_id,
                rear_transmission_id=transmission_id,
            ),
        )

        aero_resp = _create_concept_part.sync(
            id=concept_id, part_type="configuration", client=opc_client, body=AeroInput()
        )
        mass_resp = _create_concept_part.sync(
            id=concept_id, part_type="configuration", client=opc_client, body=MassInput()
        )
        wheel_resp = _create_concept_part.sync(
            id=concept_id, part_type="configuration", client=opc_client, body=WheelInput()
        )
        aero_id = aero_resp.id
        mass_id = mass_resp.id
        wheel_id = wheel_resp.id

        for speed, accel in ((10, 0.5), (20, 0.3)):
            _create_concept_part.sync(
                id=concept_id,
                part_type="requirement",
                client=opc_client,
                body=StaticRequirementInput(
                    aero_id=aero_id,
                    mass_id=mass_id,
                    wheel_id=wheel_id,
                    speed=float(speed),
                    acceleration=accel,
                    state_of_charge=0.75,
                ),
            )

    print(f"[e2e-setup] created concept: design_instance_id={concept_id}")
    yield concept_id
    app.delete_project(project_id, session_token)
    print(f"[e2e-setup] deleted project {project_id}")


# ---------------------------------------------------------------------------
# optiSLang session (connect-then-launch)
# ---------------------------------------------------------------------------


def _port_is_open(host: str, port: int, timeout: float = 1.0) -> bool:
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((host, int(port))) == 0


@pytest.fixture
def e2e_optislang():
    """Provide an optiSLang session factory using a connect-then-launch strategy.

    Resolution order (per ``acquire`` call):

    1. If ``OSL_HOST`` + ``OSL_PORT`` are set, or a server is already listening on
       ``127.0.0.1:5310``, connect to that instance and open/create the project.
       The running instance is left alive on teardown.
    2. Otherwise launch a fresh local optiSLang (honoring ``OSL_EXECUTABLE`` or
       auto-detecting the install). Launched instances are disposed on teardown.
    3. If neither works, ``pytest.skip`` with guidance.

    Yields a callable ``acquire(project_path: str) -> Optislang``.
    """
    from ansys.optislang.core import Optislang

    sessions: list[tuple[object, bool]] = []

    def acquire(project_path: str) -> "Optislang":
        host = os.environ.get("OSL_HOST")
        port = os.environ.get("OSL_PORT")
        executable = os.environ.get("OSL_EXECUTABLE") or None

        connect_host = host or DEFAULT_OSL_HOST
        connect_port = int(port) if port else DEFAULT_OSL_PORT
        should_connect = bool(host and port) or _port_is_open(connect_host, connect_port)

        osl = None
        launched = False

        if should_connect:
            try:
                print(f"[e2e-osl] connecting to {connect_host}:{connect_port}")
                osl = Optislang(host=connect_host, port=connect_port)
                if os.path.exists(project_path):
                    osl.application.open(project_path)
                else:
                    osl.application.new()
                    osl.application.save_as(project_path)
            except Exception as exc:
                print(f"[e2e-osl] connect failed: {exc!r}")
                osl = None

        if osl is None:
            try:
                print("[e2e-osl] launching local optiSLang")
                osl = Optislang(project_path=project_path, executable=executable)
                launched = True
            except Exception as exc:
                pytest.skip(
                    "optiSLang is not available (could not connect or launch). "
                    "Install optiSLang with the ConceptEV plugin, or set "
                    f"OSL_HOST/OSL_PORT to point at a running instance. Error: {exc!r}"
                )

        osl.osl_server.timeouts_register.default_value = 180
        sessions.append((osl, launched))
        return osl

    yield acquire

    for osl, launched in sessions:
        if not launched:
            print("[e2e-osl] leaving externally-managed optiSLang running")
            continue
        try:
            osl.dispose()
        except Exception as exc:
            print(f"[e2e-osl] failed to dispose session: {exc!r}")


# ---------------------------------------------------------------------------
# pyconceptev upgrade in optiSLang's Python
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def install_pyconceptev(request):
    """Install or upgrade ansys-conceptev-core in optiSLang's bundled Python.

    Activated by the ``--pyconceptev-source SRC`` CLI option.  Runs
    ``python -m pip install <SRC>`` using optiSLang's own Python interpreter so
    the injected integration can import the version under test.

    When ``--pyconceptev-source`` is not given the fixture is a no-op and yields
    ``None``, leaving whatever version is already installed untouched.

    Requires write access to the optiSLang install directory (run pytest as
    admin on Windows, or adjust folder permissions).
    """
    src = request.config.getoption("--pyconceptev-source")
    if not src:
        yield None
        return

    if not _OSL_PYTHON.exists():
        pytest.fail(
            f"optiSLang Python not found at {_OSL_PYTHON}. "
            "Update _OSL_PYTHON in conftest.py to match your installation."
        )

    print(f"\n[install-pyconceptev] installing '{src}' into {_OSL_PYTHON}")
    result = subprocess.run(
        [str(_OSL_PYTHON), "-m", "pip", "install", src],
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(f"[install-pyconceptev] pip stdout:\n{result.stdout}")
    if result.stderr:
        print(f"[install-pyconceptev] pip stderr:\n{result.stderr}")
    if result.returncode != 0:
        pytest.fail(
            f"pip install '{src}' failed (exit {result.returncode}).\n" f"stderr: {result.stderr}"
        )

    print("[install-pyconceptev] installation succeeded")
    yield src


# ---------------------------------------------------------------------------
# Integration injection
# ---------------------------------------------------------------------------


def _get_osl_user_site_packages() -> Path | None:
    """Return optiSLang's user site-packages directory, or None if not found.

    optiSLang's bundled Python adds the user site-packages directory to
    sys.path (e.g. AppData/Roaming/Python/Python310/site-packages on Windows).
    Packages installed there are found by the standard Python import machinery
    *before* the PYE import hook resolves .pye files from the integrations
    directory, which lets us shadow the encrypted sub-modules with plain .py
    files during test injection.
    """
    result = subprocess.run(
        [str(_OSL_PYTHON), "-c", "import site; print(site.getusersitepackages())"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0 or not result.stdout.strip():
        return None
    return Path(result.stdout.strip())


@pytest.fixture(scope="session")
def inject_integration(request, install_pyconceptev):  # noqa: ARG001
    """Replace the installed OptiSLang conceptev integration with files from a source folder.

    Activated by the ``--integration-dir PATH`` CLI option.

    Two-pronged injection strategy
    --------------------------------
    1. ``conceptev_ci.pye`` (the top-level integration script) is replaced with
       the plain ``.py`` source file.  optiSLang executes this file as a script,
       not through its PYE import hook, so plain Python works here.

    2. The ``conceptev/`` sub-package is installed as plain ``.py`` files into
       optiSLang's *user* site-packages directory (e.g.
       ``AppData/Roaming/Python/Python310/site-packages/conceptev/``).  This
       directory sits earlier in ``sys.path`` than the integrations directory, so
       Python's standard import machinery finds the plain ``.py`` modules before
       optiSLang's PYE hook can intercept and reject them due to checksum
       mismatch.

    All changes are reverted on session teardown.

    When ``--integration-dir`` is not given the fixture yields ``None`` and the
    already-installed integration is used unchanged.
    """
    src_dir_arg = request.config.getoption("--integration-dir")
    if not src_dir_arg:
        yield None
        return

    src_dir = Path(src_dir_arg)
    if not src_dir.is_dir():
        pytest.fail(f"--integration-dir does not exist or is not a directory: {src_dir}")

    # ------------------------------------------------------------------
    # 1. Replace conceptev_ci.pye with the plain .py source (script mode)
    # ------------------------------------------------------------------
    ci_src = src_dir / "conceptev_ci.py"
    ci_dst = _OSL_INTEGRATIONS_DIR / "conceptev_ci.pye"
    ci_backup: bytes | None = ci_dst.read_bytes() if ci_dst.exists() else None
    try:
        shutil.copy2(ci_src, ci_dst)
        print(f"[inject-integration] {ci_src.name} -> {ci_dst}")
    except PermissionError as exc:
        pytest.fail(
            f"Cannot write to optiSLang integration directory — run pytest as admin "
            f"or adjust permissions on {_OSL_INTEGRATIONS_DIR}.\n  Error: {exc}"
        )

    # ------------------------------------------------------------------
    # 2. Install conceptev/ sub-package into optiSLang user site-packages
    #    so plain .py files are found before the PYE import hook.
    # ------------------------------------------------------------------
    user_site = _get_osl_user_site_packages()
    if user_site is None:
        pytest.fail(
            "Cannot determine optiSLang's user site-packages directory. "
            f"Check that {_OSL_PYTHON} is accessible."
        )

    conceptev_src = src_dir / "conceptev"
    conceptev_dst = user_site / "conceptev"

    # Back up any existing conceptev package at that location.
    conceptev_dst_backup: Path | None = None
    if conceptev_dst.exists():
        conceptev_dst_backup = conceptev_dst.parent / f"_conceptev_backup_{os.getpid()}"
        shutil.move(str(conceptev_dst), str(conceptev_dst_backup))
        print(f"[inject-integration] backed up existing {conceptev_dst} -> {conceptev_dst_backup}")

    shutil.copytree(conceptev_src, conceptev_dst)
    print(f"[inject-integration] installed conceptev/ package -> {conceptev_dst}")
    print(f"[inject-integration] injected integration from {src_dir}")

    yield src_dir

    # ------------------------------------------------------------------
    # Teardown: restore everything
    # ------------------------------------------------------------------
    # Restore conceptev_ci.pye
    if ci_backup is not None:
        ci_dst.write_bytes(ci_backup)
    elif ci_dst.exists():
        ci_dst.unlink()
    print(f"[inject-integration] restored {ci_dst.name}")

    # Remove injected conceptev/ from user site-packages
    if conceptev_dst.exists():
        shutil.rmtree(conceptev_dst)
    # Restore previous conceptev/ if there was one
    if conceptev_dst_backup is not None and conceptev_dst_backup.exists():
        shutil.move(str(conceptev_dst_backup), str(conceptev_dst))
        print(f"[inject-integration] restored {conceptev_dst} from backup")
    print("[inject-integration] teardown complete")
