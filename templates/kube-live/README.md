# {{SERVICE_NAME}} GitOps Config

GitOps configuration for {{SERVICE_NAME}}.

## Structure

```
├── base/
│   └── values.yaml      # Base Helm values shared across environments
└── envs/
    ├── dev/
    │   ├── Chart.yaml   # Environment enabled
    │   └── values.yaml
    ├── tst/
    │   └── values.yaml  # Add Chart.yaml to enable
    ├── acc/
    │   └── values.yaml  # Add Chart.yaml to enable
    └── prd/
        └── values.yaml  # Add Chart.yaml to enable
```

## Environment Readiness Pattern

ArgoCD only deploys environments that have a `Chart.yaml` file present.

- **To enable an environment**: Add `Chart.yaml` to the env folder
- **To disable an environment**: Remove `Chart.yaml` from the env folder

Example `Chart.yaml`:

```yaml
apiVersion: v2
name: {{SERVICE_NAME}}-tst
version: 0.0.0
```

## Deployment

This repo is managed by ArgoCD via ApplicationSet. Changes pushed here will automatically sync to the cluster.

### Environments

| Environment | Namespace         | Status         |
| ----------- | ----------------- | -------------- |
| dev         | team-{{TEAM}}-dev | Enabled        |
| tst         | team-{{TEAM}}-tst | Add Chart.yaml |
| acc         | team-{{TEAM}}-acc | Add Chart.yaml |
| prd         | team-{{TEAM}}-prd | Add Chart.yaml |

## Promotion Flow

1. Develop and test in `dev`
2. When ready for `tst`, add `Chart.yaml` to `envs/tst/`
3. ArgoCD automatically creates the `tst` Application
4. Repeat for `acc` and `prd`

## Updating Image Tag

To deploy a new version, update the `image.tag` in the appropriate environment's values file.
