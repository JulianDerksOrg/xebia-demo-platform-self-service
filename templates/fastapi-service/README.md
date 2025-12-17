# {{SERVICE_NAME}}

{{DESCRIPTION}}

## Development

### Prerequisites

- Python 3.11+
- Docker (for containerized builds)

### Local Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Run locally
uvicorn app.main:app --reload --port 8080
```

### Testing

```bash
pytest -v
```

### Linting

```bash
ruff check src/
ruff format src/
```

## Deployment

This service is deployed via GitOps using ArgoCD.

- **Source repo**: This repository
- **GitOps config**: [{{SERVICE_NAME}}-kube-live](https://github.com/JulianDerksOrg/{{SERVICE_NAME}}-kube-live)

### Environments

- `dev` - Development
- `tst` - Testing
- `acc` - Acceptance
- `prd` - Production

Push to `main` to trigger CI and deploy to dev. Tag with `vX.Y.Z` for releases.
