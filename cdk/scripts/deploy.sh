#!/usr/bin/env bash
set -euo pipefail

if ! command -v aws >/dev/null 2>&1; then
  echo "AWS CLI is required."
  exit 1
fi

if ! command -v npm >/dev/null 2>&1; then
  echo "npm is required."
  exit 1
fi

if [ $# -lt 2 ]; then
  echo "Usage: $0 <repo-url> <key-pair-name-or-empty> [region] [instance-type] [branch]"
  echo "Example: $0 https://github.com/your-org/exam_center.git exam-key us-east-1 t2.micro main"
  exit 1
fi

REPO_URL="$1"
KEY_PAIR_NAME="$2"
REGION="${3:-us-east-1}"
INSTANCE_TYPE="${4:-t2.micro}"
BRANCH="${5:-main}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CDK_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$CDK_DIR"
npm install
npm run build

npx cdk deploy ExamCenterEc2Stack \
  --require-approval never \
  --region "$REGION" \
  --parameters RepoUrl="$REPO_URL" \
  --parameters KeyPairName="$KEY_PAIR_NAME" \
  --parameters RepoBranch="$BRANCH" \
  --parameters InstanceType="$INSTANCE_TYPE"
