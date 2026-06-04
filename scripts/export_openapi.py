"""Export the ConceptEV OpenAPI spec from the service URL to a JSON file.

Run from the repo root inside the poetry/venv environment:

    python scripts/export_openapi.py [--output schema/openapi_v2.json]
    python scripts/export_openapi.py --url https://dev-conceptev.awsansys3np.onscale.com/api/openapi.json

The script fetches the OpenAPI document from the configured service URL and
writes it to disk.
"""

import argparse
import json
from pathlib import Path

import httpx

#DEFAULT_OPENAPI_URL = "https://dev-conceptev.awsansys3np.onscale.com/api/openapi.json"
DEFAULT_OPENAPI_URL = "http://127.0.0.1:8080/api/openapi.json"

def fetch_spec(url: str) -> dict:
    """Fetch and return the OpenAPI spec from the given URL."""
    with httpx.Client(follow_redirects=True, timeout=60.0) as client:
        response = client.get(url)
        response.raise_for_status()

    spec = response.json()
    if not isinstance(spec, dict):
        raise ValueError(f"Expected a JSON object from {url}, got {type(spec).__name__}")

    return spec


def main() -> None:
    """Parse args and export the spec."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--url",
        default=DEFAULT_OPENAPI_URL,
        help=f"OpenAPI URL to fetch (default: {DEFAULT_OPENAPI_URL})",
    )
    parser.add_argument(
        "--output",
        default="schema/openapi_v2.json",
        help="Output path for the OpenAPI JSON file (default: schema/openapi_v2.json)",
    )
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Fetching OpenAPI spec from {args.url}...")
    spec = fetch_spec(args.url)

    path_count = len(spec.get("paths", {}))
    schema_count = len(spec.get("components", {}).get("schemas", {}))

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2)

    print(f"Exported {path_count} paths, {schema_count} schemas -> {output_path}")


if __name__ == "__main__":
    main()
