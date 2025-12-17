# {{SERVICE_NAME}} GitOps Config

GitOps configuration for {{SERVICE_NAME}}.

## Structure

```
├── base/
│   └── values.yaml      # Base Helm values shared across environments
└── envs/
    ├── tst/
    │   ├── Chart.yaml   # Environment enabled
    │   └── values.yaml
    ├── acc/
    │   └── values.yaml  # Add Chart.yaml to enable
    └── prd/
        └── values.yaml  # Add Chart.yaml to enable
```

## Environment Readiness Pattern

ArgoCD only deploys environments that have a `Chart.yaml` file present.

- **To enable an environment**: Add `Chart.yaml` to the env folder
- **To disable an environment**: Remove `Chart.yaml` from the env folder

Example `Chart.yaml` to enable an environment:

```yaml
apiVersion: v2
name: {{SERVICE_NAME}}-<env>
version: 0.0.0

dependencies:
  - name: service-chart
    version: {{SERVICE_CHART_VERSION}}
    repository: oci://{{GAR_HELM_REGISTRY}}
```

## Deployment

This repo is managed by ArgoCD via ApplicationSet. Changes pushed here will automatically sync to the cluster.

### Environments

| Environment | Namespace    | Status         |
| ----------- | ------------ | -------------- |
| tst         | {{TEAM}}-tst | Enabled        |
| acc         | {{TEAM}}-acc | Add Chart.yaml |
| prd         | {{TEAM}}-prd | Add Chart.yaml |

## Promotion Flow

1. Develop and test in `tst`
2. When ready for `acc`, add `Chart.yaml` to `envs/acc/`
3. ArgoCD automatically creates the `acc` Application
4. Repeat for `prd`

## Updating Image Tag

To deploy a new version, update the `image.tag` in the appropriate environment's values file.
