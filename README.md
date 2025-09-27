# Office Door Sign

A FastAPI-based service for controlling an office door light panel. The target deployment is a
Raspberry Pi Zero 2 attached to a Unicorn HAT Mini. During local development the hardware is
mocked so the API can be exercised without the Unicorn HAT library.

## Features

- FastAPI application with endpoints for toggling the light on and off.
- Hardware abstraction layer that allows swapping between a real Unicorn HAT Mini controller and a
  lightweight mock implementation.
- Testing scaffold using pytest and FastAPI's `TestClient`.
- Formatting guidance via YAPF configured for a two-space indentation style.
- Continuous integration workflow ready for GitHub Actions.

## Getting Started

### Local Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

### Running the API locally

```bash
uvicorn office_sign.api:create_app --factory --reload
```

By default the factory creates the application with the in-memory mock panel so it can run anywhere.

### Running with Docker

Build the image and run the API without installing Python on the host:

```bash
docker build -t office-door-sign .
docker run --rm -p 8000:8000 office-door-sign
```

For live-reload development and test execution you can use Docker Compose:

```bash
docker compose up
docker compose run --rm app pytest
```

The compose service mounts `src/` and `tests/` from the host so code changes trigger the reloadable
`uvicorn` server.

### Generating the OpenAPI specification

Produce a standalone OpenAPI schema that can be imported into client tooling:

```bash
python -m office_sign.openapi --output openapi.yaml
```

The exporter infers the format from the file extension, so `.json`, `.yaml`, and `.yml` targets are
all supported. The default output path is `openapi.json` in the project root if `--output` is
omitted.

### Testing

```bash
pytest
```

### Formatting

Run YAPF before committing to ensure the two-space style is enforced:

```bash
yapf -r --in-place src tests
```

## Deploying to Raspberry Pi

Install the runtime requirements on the Pi:

```bash
pip install -r requirements.txt
```

Swap the dependency wiring to use the real Unicorn HAT Mini controller. See
`office_sign.hardware.unicorn_hat` for details on enabling the hardware integration.

## Continuous Integration

The repository includes a GitHub Actions workflow that installs dependencies and runs formatting and
unit tests. Point the workflow to the Raspberry Pi self-hosted runner once it is registered with
GitHub.
