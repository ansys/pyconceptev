# Copyright (C) 2023 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

Settings are loaded from ``tests/e2e/config.toml`` (``PYCONCEPTEV_SETTINGS`` is
set to that file before any pyconceptev import).  Edit that file to change the
target environment, credentials, or account name.

optiSLang location is taken from OSL_HOST / OSL_PORT (connect) or OSL_EXECUTABLE
(launch) env vars; see the ``e2e_optislang`` fixture.

Example invocation
------------------
    pytest tests/e2e -vv
"""

from contextlib import closing
import os
from pathlib import Path
import shutil
import socket
import subprocess

_E2E_DIR = Path(__file__).resolve().parent
_TESTS_DIR = _E2E_DIR.parent
E2E_CONFIG = _E2E_DIR / "config.toml"
DATA_DIR = _TESTS_DIR / "integration"

# ---------------------------------------------------------------------------
# OptiSLang integration injection
# ---------------------------------------------------------------------------

_OSL_INTEGRATIONS_DIR = Path(
    os.environ.get(
        "OSL_INTEGRATIONS_DIR",
        "C:/Program Files/ANSYS Inc/v271/optiSLang/scripting/integrations",
    )
)
# Python interpreter bundled with optiSLang — used to upgrade packages in-place.
_OSL_PYTHON = Path(
    os.environ.get(
        "OSL_PYTHON",
        "C:/Program Files/ANSYS Inc/v271/optiSLang/lib/python3.10/python.exe",
    )
)

# Point PYCONCEPTEV_SETTINGS at tests/e2e/config.toml before any pyconceptev
# import so that Settings() loads the right values from the start.
os.environ["PYCONCEPTEV_SETTINGS"] = str(E2E_CONFIG)
os.environ.setdefault("PYOPTISLANG_DISABLE_OPTISLANG_OUTPUT", "true")
# Forward websocket progress messages from the optiSLang subprocess to a log
# file in the test artifacts directory (subprocess stdout is suppressed above).
os.environ.setdefault(
    "CONCEPTEV_PROGRESS_LOG",
    str(_TESTS_DIR.parent / "test_working_dir" / "debug" / "progress.log"),
)

import pytest  # noqa: E402

from ansys.conceptev.core import app, auth  # noqa: E402
from ansys.conceptev.core.settings import settings as _loaded_settings  # noqa: E402

DEFAULT_OSL_HOST = "127.0.0.1"
DEFAULT_OSL_PORT = 5310


def pytest_addoption(parser: pytest.Parser) -> None:
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
    """Return the pyconceptev settings loaded from tests/e2e/config.toml.

    Also exports CONCEPTEV_PASSWORD to the process environment so optiSLang's
    bundled Python subprocess can pick it up regardless of its working directory
    (pydantic-settings secret-file lookup is CWD-relative).
    """
    if _loaded_settings.conceptev_password and not os.environ.get("CONCEPTEV_PASSWORD"):
        os.environ["CONCEPTEV_PASSWORD"] = _loaded_settings.conceptev_password

    password_set = bool(_loaded_settings.conceptev_password or os.environ.get("CONCEPTEV_PASSWORD"))
    print(
        f"\n[e2e-settings] config={E2E_CONFIG}\n"
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
def account_name(e2e_settings) -> str:
    """The ConceptEV account name from tests/e2e/config.toml.

    Set ``account_name = \"<your account>\"`` in that file.  The session is
    skipped when the value is absent or empty.
    """
    name = e2e_settings.account_name
    if not name:
        pytest.skip(
            "account_name is not set in tests/e2e/config.toml. "
            "Add 'account_name = \"<your account>\"' to that file."
        )
    return name


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
    """Create a fully-populated e2e concept and delete it on session teardown.

    The optiSLang ConceptEV plugin's ``sanitize_result_data`` requires
    ``data['requirements']`` and a valid architecture.  This fixture creates a
    known-good concept with:

    - MotorLabID rear motor (from the bundled ``e9.lab`` file)
    - BatteryFixedVoltages, TransmissionLossCoefficients
    - Rear-motor architecture
    - Aero / mass / wheel configurations
    - Two static-acceleration requirements (so summary outputs land at _02__summary__)

    Yields the ``design_instance_id``.
    """
    with app.get_http_client(session_token) as client:
        project = app.create_new_project(
            client,
            session_account_id,
            session_hpc_id,
            "E2E Tests – optiSLang connection",
        )
        concept = app.create_new_concept(
            client,
            project["projectId"],
            title="E2E optiSLang test concept",
        )

    design_instance_id = concept["design_instance_id"]

    with app.get_http_client(session_token, design_instance_id) as client:
        motor_file_result = app.post_component_file(client, DATA_DIR / "e9.lab", "motor_lab_file")
        motor = app.post(
            client,
            "/components",
            data={
                "component_type": "MotorLabID",
                "name": "E2E Test Rear Motor",
                "data_id": motor_file_result[0],
                "max_speed": motor_file_result[1],
                "inverter_losses_included": False,
            },
        )
        battery = app.post(client, "/components", data={"component_type": "BatteryFixedVoltages"})
        transmission = app.post(
            client, "/components", data={"component_type": "TransmissionLossCoefficients"}
        )
        app.post(
            client,
            "/architectures",
            data={
                "number_of_front_motors": 0,
                "number_of_front_wheels": 2,
                "number_of_rear_motors": 1,
                "number_of_rear_wheels": 2,
                "rear_transmission_id": transmission["id"],
                "rear_motor_id": motor["id"],
                "battery_id": battery["id"],
            },
        )
        aero = app.post(client, "/configurations", data={"config_type": "aero"})
        mass = app.post(client, "/configurations", data={"config_type": "mass"})
        wheel = app.post(client, "/configurations", data={"config_type": "wheel"})
        for speed, accel in ((10, 0.5), (20, 0.3)):
            app.post(
                client,
                "/requirements",
                data={
                    "requirement_type": "static_acceleration",
                    "speed": speed,
                    "mass_id": mass["id"],
                    "aero_id": aero["id"],
                    "wheel_id": wheel["id"],
                    "state_of_charge": 0.75,
                    "acceleration": accel,
                },
            )

    print(f"[e2e-setup] created concept: design_instance_id={design_instance_id}")
    yield design_instance_id
    app.delete_project(project["projectId"], session_token)
    print(f"[e2e-setup] deleted project {project['projectId']}")


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


@pytest.fixture(scope="session")
def inject_integration(request, install_pyconceptev):  # noqa: ARG001
    """Replace the installed OptiSLang conceptev integration with files from a source folder.

    Activated by the ``--integration-dir PATH`` CLI option.  Each ``.py`` source
    file under PATH is copied over its ``.pye`` counterpart in the optiSLang
    scripting/integrations directory.  Original bytes are held in memory and
    written back on session teardown, even when the test fails.

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

    # Collect: top-level conceptev_ci.py + every .py under conceptev/ subfolder.
    src_files = [src_dir / "conceptev_ci.py"] + [
        p for p in (src_dir / "conceptev").rglob("*.py") if not p.name.startswith("_")
    ]
    # Also include __init__.py files.
    src_files += [p for p in (src_dir / "conceptev").rglob("__init__.py")]
    # Deduplicate while preserving order.
    seen: set[Path] = set()
    unique_src: list[Path] = []
    for p in src_files:
        if p not in seen:
            seen.add(p)
            unique_src.append(p)

    mapping: dict[Path, Path] = {}
    for src in unique_src:
        rel = src.relative_to(src_dir)
        dst = _OSL_INTEGRATIONS_DIR / rel.with_suffix(".pye")
        mapping[src] = dst

    # Backup existing .pye content (keyed by destination path).
    backups: dict[Path, bytes] = {}
    for dst in mapping.values():
        if dst.exists():
            backups[dst] = dst.read_bytes()

    # Copy source files over installed .pye files.
    copied: list[Path] = []
    try:
        for src, dst in mapping.items():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            copied.append(dst)
            print(f"[inject-integration] {src.name} -> {dst}")
    except PermissionError as exc:
        pytest.fail(
            f"Cannot write to optiSLang integration directory — run pytest as admin "
            f"or adjust permissions on {_OSL_INTEGRATIONS_DIR}.\n  Error: {exc}"
        )

    print(f"[inject-integration] injected {len(copied)} file(s) from {src_dir}")
    yield src_dir

    # Restore originals.
    for dst, data in backups.items():
        dst.write_bytes(data)
    # Remove any destination files that had no pre-existing backup (new files added).
    for dst in mapping.values():
        if dst not in backups and dst.exists():
            dst.unlink()
    print(f"[inject-integration] restored {len(backups)} original file(s)")
