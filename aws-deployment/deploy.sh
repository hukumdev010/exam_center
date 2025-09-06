#!/bin/bash

# Deployment script for Exam Center FastAPI Backend on AWS EC2
# This script helps deploy your application using CloudFormation

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    print_error "AWS CLI is not installed. Please install it first:"
    print_error "curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip'"
    print_error "unzip awscliv2.zip"
    print_error "sudo ./aws/install"
    exit 1
fi

# Check if user is logged in to AWS
if ! aws sts get-caller-identity &> /dev/null; then
    print_error "You are not logged in to AWS. Please run 'aws configure' first."
    exit 1
fi

# Default values
STACK_NAME="exam-center-backend"
REGION="us-east-1"
KEY_PAIR_NAME=""
DB_USERNAME="examcenter"
DB_PASSWORD=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --stack-name)
            STACK_NAME="$2"
            shift 2
            ;;
        --region)
            REGION="$2"
            shift 2
            ;;
        --key-pair)
            KEY_PAIR_NAME="$2"
            shift 2
            ;;
        --db-username)
            DB_USERNAME="$2"
            shift 2
            ;;
        --db-password)
            DB_PASSWORD="$2"
            shift 2
            ;;
        --help)
            echo "Usage: $0 [OPTIONS]"
            echo "Options:"
            echo "  --stack-name NAME      CloudFormation stack name (default: exam-center-backend)"
            echo "  --region REGION        AWS region (default: us-east-1)"
            echo "  --key-pair NAME        EC2 Key Pair name (required)"
            echo "  --db-username USER     Database username (default: examcenter)"
            echo "  --db-password PASS     Database password (required)"
            echo "  --help                 Show this help message"
            exit 0
            ;;
        *)
            print_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Validate required parameters
if [ -z "$KEY_PAIR_NAME" ]; then
    read -p "Enter your EC2 Key Pair name: " KEY_PAIR_NAME
    if [ -z "$KEY_PAIR_NAME" ]; then
        print_error "Key Pair name is required"
        exit 1
    fi
fi

if [ -z "$DB_PASSWORD" ]; then
    read -s -p "Enter database password (min 8 characters): " DB_PASSWORD
    echo
    if [ ${#DB_PASSWORD} -lt 8 ]; then
        print_error "Database password must be at least 8 characters"
        exit 1
    fi
fi

print_status "Starting deployment with the following configuration:"
echo "  Stack Name: $STACK_NAME"
echo "  Region: $REGION"
echo "  Key Pair: $KEY_PAIR_NAME"
echo "  DB Username: $DB_USERNAME"

# Check if stack already exists
if aws cloudformation describe-stacks --stack-name "$STACK_NAME" --region "$REGION" &> /dev/null; then
    print_warning "Stack '$STACK_NAME' already exists. Updating..."
    OPERATION="update-stack"
else
    print_status "Creating new stack '$STACK_NAME'..."
    OPERATION="create-stack"
fi

# Deploy the CloudFormation stack
print_status "Deploying CloudFormation stack..."
aws cloudformation $OPERATION \
    --stack-name "$STACK_NAME" \
    --template-body file://cloudformation-template.yaml \
    --parameters \
        ParameterKey=KeyPairName,ParameterValue="$KEY_PAIR_NAME" \
        ParameterKey=DBUsername,ParameterValue="$DB_USERNAME" \
        ParameterKey=DBPassword,ParameterValue="$DB_PASSWORD" \
    --capabilities CAPABILITY_IAM \
    --region "$REGION"

print_status "Waiting for stack operation to complete..."
aws cloudformation wait stack-${OPERATION//-stack/}-complete \
    --stack-name "$STACK_NAME" \
    --region "$REGION"

# Get stack outputs
print_status "Retrieving stack outputs..."
OUTPUTS=$(aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --region "$REGION" \
    --query 'Stacks[0].Outputs' \
    --output table)

echo "$OUTPUTS"

# Get specific outputs for further instructions
PUBLIC_IP=$(aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --region "$REGION" \
    --query 'Stacks[0].Outputs[?OutputKey==`WebServerPublicIP`].OutputValue' \
    --output text)

APP_URL=$(aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --region "$REGION" \
    --query 'Stacks[0].Outputs[?OutputKey==`ApplicationURL`].OutputValue' \
    --output text)

print_status "Deployment completed successfully!"
print_status "Next steps:"
echo "1. SSH into your server: ssh -i your-key.pem ec2-user@$PUBLIC_IP"
echo "2. Deploy your application code (see deploy-code.sh)"
echo "3. Your application will be available at: $APP_URL"

print_warning "Important: Make sure to update the AMI ID in the CloudFormation template for your specific region!"
print_warning "Current template uses us-east-1 AMI. Check AWS documentation for region-specific AMIs."
