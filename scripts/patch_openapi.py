"""Patch a ConceptEV OpenAPI spec to fix known generator-incompatibilities.

This script is a CI safety-net that fixes issues in the spec before passing it
to openapi-python-client.  The root causes should be fixed in the server code;
this script exists so client generation doesn't break while those fixes land.

Known issues patched:
  1. discriminator.mapping values that are nested schemas (not $ref strings)
     — caused by LibraryItemTypes union with sub-discriminators.
  2. Path parameters typed as ``str | null`` (None | str)
     — invalid in OpenAPI 3.1 path params; generator rejects the endpoint.

Usage:
    python scripts/patch_openapi.py --input schema/openapi_v2.json
    python scripts/patch_openapi.py --input schema/openapi_v2.json --output schema/openapi_v2_patched.json
"""

import argparse
import copy
import json
import sys
from pathlib import Path


def fix_bad_discriminator_mappings(spec: dict) -> list[str]:
    """Remove discriminator.mapping entries whose values are dicts (not strings).

    The OpenAPI 3.x spec requires that discriminator.mapping values are strings
    ($ref paths or schema names).  FastAPI can emit dict values when a union
    type itself contains a discriminator — openapi-python-client rejects these.

    Returns a list of human-readable descriptions of changes made.
    """
    changes: list[str] = []

    def _fix(obj: object, path: str) -> None:
        if isinstance(obj, dict):
            if "discriminator" in obj:
                mapping: dict = obj["discriminator"].get("mapping", {})
                bad = [k for k, v in mapping.items() if isinstance(v, dict)]
                for k in bad:
                    del mapping[k]
                    changes.append(f"Removed non-string discriminator mapping key '{k}' at {path}")
                if not mapping:
                    del obj["discriminator"]
            for k, v in obj.items():
                _fix(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                _fix(v, f"{path}[{i}]")

    _fix(spec.get("paths", {}), "paths")
    return changes


def fix_nullable_path_params(spec: dict) -> list[str]:
    """Remove endpoints whose path parameters are typed as nullable (str | null).

    openapi-python-client does not support ``None | str`` path parameters.
    These are typically on deprecated endpoints; they are removed from the spec
    so the generator skips them cleanly rather than emitting a warning/error.

    Returns a list of human-readable descriptions of changes made.
    """
    changes: list[str] = []
    paths_to_remove: list[str] = []

    for path, path_item in spec.get("paths", {}).items():
        for method, op in path_item.items():
            if not isinstance(op, dict):
                continue
            for param in op.get("parameters", []):
                if param.get("in") != "path":
                    continue
                schema = param.get("param_schema") or param.get("schema", {})
                any_of = schema.get("anyOf", [])
                types = {s.get("type") for s in any_of}
                if "null" in types and len(any_of) > 1:
                    paths_to_remove.append(path)
                    changes.append(
                        f"Removed {method.upper()} {path}: "
                        f"path param '{param.get('name')}' is nullable (str|null)"
                    )

    for path in paths_to_remove:
        del spec["paths"][path]

    return changes


def prune_unused_schemas(spec: dict) -> list[str]:
    """Remove schemas not reachable from any path.  Returns removed schema names."""
    components = spec.get("components", {})
    all_schemas: dict = components.get("schemas", {})
    if not all_schemas:
        return []

    def _collect_refs(obj: object, refs: set[str]) -> None:
        if isinstance(obj, dict):
            if "$ref" in obj and isinstance(obj["$ref"], str):
                refs.add(obj["$ref"])
            for v in obj.values():
                _collect_refs(v, refs)
        elif isinstance(obj, list):
            for v in obj:
                _collect_refs(v, refs)

    reachable: set[str] = set()
    frontier: set[str] = set()
    _collect_refs(spec.get("paths", {}), frontier)

    while frontier:
        new_refs: set[str] = set()
        for ref in frontier:
            name = ref.split("/")[-1]
            if name in reachable:
                continue
            reachable.add(name)
            if name in all_schemas:
                _collect_refs(all_schemas[name], new_refs)
        frontier = new_refs - reachable

    removed = [k for k in all_schemas if k not in reachable]
    spec["components"]["schemas"] = {k: v for k, v in all_schemas.items() if k in reachable}
    return removed


def patch(spec: dict, *, prune_schemas: bool = False) -> tuple[dict, list[str]]:
    """Apply all patches to *spec* (in-place on a deep copy).

    Returns ``(patched_spec, list_of_change_descriptions)``.
    """
    patched = copy.deepcopy(spec)
    all_changes: list[str] = []

    changes = fix_bad_discriminator_mappings(patched)
    all_changes.extend(changes)

    changes = fix_nullable_path_params(patched)
    all_changes.extend(changes)

    if prune_schemas:
        removed = prune_unused_schemas(patched)
        if removed:
            all_changes.append(f"Pruned {len(removed)} unused schemas: {', '.join(removed[:5])}{'...' if len(removed) > 5 else ''}")

    return patched, all_changes


def main() -> None:
    """Parse args and patch the spec."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Input OpenAPI JSON file")
    parser.add_argument(
        "--output",
        help="Output path (defaults to overwriting input file)",
    )
    parser.add_argument(
        "--prune-schemas",
        action="store_true",
        help="Also remove schemas not reachable from any path",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit with code 1 if any patches were applied (for CI diff checks)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    spec = json.loads(input_path.read_text(encoding="utf-8"))
    patched, changes = patch(spec, prune_schemas=args.prune_schemas)

    output_path = Path(args.output) if args.output else input_path
    output_path.write_text(json.dumps(patched, indent=2), encoding="utf-8")

    if changes:
        print(f"Applied {len(changes)} patch(es) to {output_path}:")
        for c in changes:
            print(f"  - {c}")
    else:
        print(f"No patches needed — spec at {output_path} is already clean.")

    if args.check and changes:
        print("\nCI check failed: spec required patches. Fix the root causes in the server code.")
        sys.exit(1)


if __name__ == "__main__":
    main()
