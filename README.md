# Platform Self-Service

Internal Developer Platform self-service portal using GitHub Actions.

## Golden Paths

### 🚀 Create FastAPI Service

Creates a new FastAPI microservice with:

- Source code repository with CI pipeline
- GitOps config repository (kube-live)
- ArgoCD ApplicationSet for multi-environment deployment

**Usage:**

1. Go to [Actions](../../actions) tab
2. Select "🚀 Create FastAPI Service"
3. Click "Run workflow"
4. Fill in:
   - **Service name**: lowercase with hyphens (e.g., `my-service`)
   - **Team**: Select your team
   - **Description**: Short description

**What gets created:**

- `{service-name}-src` - Source code repo with FastAPI template
- `{service-name}-kube-live` - GitOps config repo
- ApplicationSet in `appsets-kube-live` for ArgoCD

## Prerequisites

### GitHub Secrets Required

| Secret   | Description                                                 |
| -------- | ----------------------------------------------------------- |
| `GH_PAT` | GitHub Personal Access Token with `repo`, `workflow` scopes |

### GitHub Variables Required

Set these at org level for all repos to inherit:

| Variable              | Description                           |
| --------------------- | ------------------------------------- |
| `WIF_PROVIDER`        | Workload Identity Federation provider |
| `WIF_SERVICE_ACCOUNT` | GCP service account for WIF           |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Platform Self-Service                         │
│                    (This Repository)                             │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  workflow_dispatch: Create FastAPI Service               │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────────┐
│ {name}-src    │   │ {name}-kube-  │   │ appsets-kube-live │
│               │   │ live          │   │                   │
│ - FastAPI     │   │ - base/       │   │ + {name}.yaml     │
│ - Dockerfile  │   │ - envs/       │   │   (ApplicationSet)│
│ - CI pipeline │   │   dev/tst/    │   │                   │
│               │   │   acc/prd     │   │                   │
└───────────────┘   └───────────────┘   └───────────────────┘
        │                     │                     │
        │ push to main        │                     │
        ▼                     │                     │
┌───────────────┐             │                     │
│ GAR           │◄────────────┼─────────────────────┘
│ (Docker imgs) │             │
└───────────────┘             │
                              ▼
                    ┌───────────────┐
                    │   ArgoCD      │
                    │               │
                    │ Syncs to K8s  │
                    └───────────────┘
```
