# Exam Center CDK (Root-Level)

This CDK app is intentionally placed at the repository root in `./cdk` (not inside `backend` or `frontend`).

## What it deploys

- 1 VPC (public subnet only)
- 1 EC2 instance (`t2.micro` by default)
- 1 Elastic IP
- Backend runs in Docker container
- Frontend runs on Node.js (`next start`)
- Nginx reverse proxy on port 80:
  - `/` -> frontend
  - `/api/` -> backend container

## Prerequisites

- AWS CLI configured (`aws configure`)
- Node.js + npm installed
- Bootstrapped CDK environment (one-time):

```bash
cd cdk
npm install
npx cdk bootstrap aws://ACCOUNT_ID/REGION
```

## Deploy

```bash
cd cdk
./scripts/deploy.sh <repo-url> <key-pair-name-or-empty> [region] [instance-type] [branch]
```

Example:

```bash
cd cdk
./scripts/deploy.sh https://github.com/hukumdev010/exam_center.git exam-center-key us-east-1 t2.micro main
```

## Useful parameters

You can override additional parameters manually with `npx cdk deploy`:

- `DatabaseUrl` (default: local postgres URL placeholder)
- `SecretKey` (default: change-me-in-production)
- `BackendPort` (default: 8000)
- `FrontendPort` (default: 3000)

Example:

```bash
npx cdk deploy ExamCenterEc2Stack \
  --require-approval never \
  --parameters RepoUrl=https://github.com/hukumdev010/exam_center.git \
  --parameters KeyPairName=exam-center-key \
  --parameters DatabaseUrl='postgresql+asyncpg://user:pass@db-host:5432/exam_center' \
  --parameters SecretKey='super-secret-value'
```

## Outputs

- `PublicIp`
- `FrontendUrl` (http://PUBLIC_IP)
- `BackendHealthUrl` (http://PUBLIC_IP/api/docs)

## Notes

- This is a single-instance deployment for low-cost environments.
- Backend is Dockerized during EC2 user-data execution.
- Frontend and backend are both deployed from your git repository path structure (`/frontend`, `/backend`).
