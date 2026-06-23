"""Generate the pyconceptev Python client from the ConceptEV v2 OpenAPI spec.

Pipeline (all steps run automatically unless flags are used):
    1. Export the spec from the configured OpenAPI URL -> schema/openapi_v2.json
  2. Patch the spec to fix any generator-incompatibilities (safety-net)
  3. Run openapi-python-client to generate the typed client

Usage (from repo root, inside poetry/venv environment):

    # Full pipeline:
    python scripts/generate_client.py

    # Skip export, use existing spec file:
    python scripts/generate_client.py --no-export

    # Use a custom spec file (also skips export):
    python scripts/generate_client.py --spec path/to/openapi.json --no-export

The generated client is written to schema/generated_client/.
"""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import subprocess
import sys

REPO_ROOT = Path(__file__).parents[1]
DEFAULT_SPEC = REPO_ROOT / "schema" / "openapi_v2.json"
DEFAULT_OUTPUT = REPO_ROOT / "schema" / "generated_client"
OPC_CONFIG = REPO_ROOT / "schema" / "opc_config.yaml"
GENERATED_PKG_NAME = "conceptev_api_client"
SRC_DEST = REPO_ROOT / "src" / "ansys" / "conceptev" / "core" / "generated"


def export_spec(output: Path) -> None:
    """Run the spec-export script."""
    print("==> Exporting OpenAPI v2 spec...")
    subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "export_openapi.py"), "--output", str(output)],
        check=True,
    )


def patch_spec(spec: Path) -> None:
    """Run the spec-patch script (fixes generator-incompatibilities)."""
    print("==> Patching spec...")
    subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "patch_openapi.py"), "--input", str(spec)],
        check=True,
    )


def generate_client(spec: Path, output: Path, config: Path) -> None:
    """Run openapi-python-client generator."""
    print(f"==> Generating client from {spec}...")
    cmd = [
        sys.executable,
        "-m",
        "openapi_python_client",
        "generate",
        "--path",
        str(spec),
        "--output-path",
        str(output),
        "--config",
        str(config),
        "--overwrite",
    ]
    subprocess.run(cmd, check=True)

    print(f"==> Client generated at {output}")


def copy_to_src(generated_output: Path, dest: Path, spec: Path) -> None:
    """Copy the generated package into the src tree so it is part of the installed package."""
    src = generated_output / GENERATED_PKG_NAME
    if not src.is_dir():
        print(f"ERROR: Generated package not found at {src}", file=sys.stderr)
        sys.exit(1)
    print(f"==> Copying {src.name} -> {dest}...")
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)

    # Write a stamp file recording which spec version produced this code.
    spec_version = "unknown"
    try:
        spec_version = json.loads(spec.read_text(encoding="utf-8"))["info"]["version"]
    except Exception:
        pass
    stamp = dest / "_codegen_stamp.py"
    stamp.write_text(
        f'"""Auto-generated marker — do not edit manually.\n\n'
        f"Regenerate with: python scripts/generate_client.py\n"
        f'"""\n\n'
        f'SPEC_VERSION = "{spec_version}"\n'
        f'GENERATED_AT = "{datetime.now(timezone.utc).isoformat(timespec="seconds")}"\n',
        encoding="utf-8",
    )


def main() -> None:
    """Parse args and run the generation pipeline."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--spec",
        default=str(DEFAULT_SPEC),
        help=f"Path to OpenAPI spec JSON (default: {DEFAULT_SPEC})",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help=f"Output directory for generated client (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--no-export",
        action="store_true",
        help="Skip spec export step and use the existing spec file",
    )
    parser.add_argument(
        "--no-patch",
        action="store_true",
        help="Skip the spec-patch step (use only if spec is already clean)",
    )
    parser.add_argument(
        "--no-copy",
        action="store_true",
        help="Skip copying the generated package into src/ansys/conceptev/core/generated/",
    )
    args = parser.parse_args()

    spec_path = Path(args.spec)
    output_path = Path(args.output)

    if not args.no_export:
        export_spec(spec_path)
    elif not spec_path.exists():
        print(f"ERROR: Spec file not found: {spec_path}", file=sys.stderr)
        sys.exit(1)

    if not args.no_patch:
        patch_spec(spec_path)

    if not OPC_CONFIG.exists():
        print(f"ERROR: Generator config not found: {OPC_CONFIG}", file=sys.stderr)
        sys.exit(1)

    generate_client(spec_path, output_path, OPC_CONFIG)

    if not args.no_copy:
        copy_to_src(output_path, SRC_DEST, spec_path)


if __name__ == "__main__":
    main()
