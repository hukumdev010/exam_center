# Deployment script for Exam Center FastAPI Backend on AWS EC2
# PowerShell version for Windows
param(
    [string]$StackName = "exam-center-backend",
    [string]$Region = "us-east-1",
    [string]$KeyPairName = "",
    [string]$DBUsername = "examcenter",
    [string]$DBPassword = "",
    [switch]$Help
)

# Function to print colored output
function Write-Status {
    param([string]$Message)
    Write-Host "[INFO] $Message" -ForegroundColor Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "[WARNING] $Message" -ForegroundColor Yellow
}

function Write-Error {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor Red
}

if ($Help) {
    Write-Host "Usage: .\deploy.ps1 [OPTIONS]"
    Write-Host "Options:"
    Write-Host "  -StackName NAME        CloudFormation stack name (default: exam-center-backend)"
    Write-Host "  -Region REGION         AWS region (default: us-east-1)"
    Write-Host "  -KeyPairName NAME      EC2 Key Pair name (required)"
    Write-Host "  -DBUsername USER       Database username (default: examcenter)"
    Write-Host "  -DBPassword PASS       Database password (required)"
    Write-Host "  -Help                  Show this help message"
    exit 0
}

# Check if AWS CLI is installed
try {
    $null = Get-Command aws -ErrorAction Stop
} catch {
    Write-Error "AWS CLI is not installed. Please install it first:"
    Write-Error "Download from: https://aws.amazon.com/cli/"
    exit 1
}

# Check if user is logged in to AWS
try {
    $null = aws sts get-caller-identity 2>$null
} catch {
    Write-Error "You are not logged in to AWS. Please run 'aws configure' first."
    exit 1
}

# Get required parameters if not provided
if (-not $KeyPairName) {
    $KeyPairName = Read-Host "Enter your EC2 Key Pair name"
    if (-not $KeyPairName) {
        Write-Error "Key Pair name is required"
        exit 1
    }
}

if (-not $DBPassword) {
    $SecurePassword = Read-Host "Enter database password (min 8 characters)" -AsSecureString
    $DBPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($SecurePassword))
    if ($DBPassword.Length -lt 8) {
        Write-Error "Database password must be at least 8 characters"
        exit 1
    }
}

Write-Status "Starting deployment with the following configuration:"
Write-Host "  Stack Name: $StackName"
Write-Host "  Region: $Region"
Write-Host "  Key Pair: $KeyPairName"
Write-Host "  DB Username: $DBUsername"

# Check if stack already exists
try {
    $null = aws cloudformation describe-stacks --stack-name $StackName --region $Region 2>$null
    Write-Warning "Stack '$StackName' already exists. Updating..."
    $Operation = "update-stack"
} catch {
    Write-Status "Creating new stack '$StackName'..."
    $Operation = "create-stack"
}

# Deploy the CloudFormation stack
Write-Status "Deploying CloudFormation stack..."
$deployResult = aws cloudformation $Operation `
    --stack-name $StackName `
    --template-body file://cloudformation-template.yaml `
    --parameters `
        ParameterKey=KeyPairName,ParameterValue=$KeyPairName `
        ParameterKey=DBUsername,ParameterValue=$DBUsername `
        ParameterKey=DBPassword,ParameterValue=$DBPassword `
    --capabilities CAPABILITY_IAM `
    --region $Region

if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to deploy CloudFormation stack"
    exit 1
}

Write-Status "Waiting for stack operation to complete..."
$waitOperation = if ($Operation -eq "create-stack") { "stack-create-complete" } else { "stack-update-complete" }
aws cloudformation wait $waitOperation --stack-name $StackName --region $Region

if ($LASTEXITCODE -ne 0) {
    Write-Error "Stack operation failed or timed out"
    exit 1
}

# Get stack outputs
Write-Status "Retrieving stack outputs..."
$outputs = aws cloudformation describe-stacks `
    --stack-name $StackName `
    --region $Region `
    --query 'Stacks[0].Outputs' `
    --output table

Write-Host $outputs

# Get specific outputs for further instructions
$publicIP = aws cloudformation describe-stacks `
    --stack-name $StackName `
    --region $Region `
    --query 'Stacks[0].Outputs[?OutputKey==`WebServerPublicIP`].OutputValue' `
    --output text

$appURL = aws cloudformation describe-stacks `
    --stack-name $StackName `
    --region $Region `
    --query 'Stacks[0].Outputs[?OutputKey==`ApplicationURL`].OutputValue' `
    --output text

Write-Status "Deployment completed successfully!"
Write-Host ""
Write-Status "Next steps:"
Write-Host "1. SSH into your server: ssh -i your-key.pem ubuntu@$publicIP"
Write-Host "2. Deploy your application code by running: sudo /opt/exam-center/deploy-from-git.sh"
Write-Host "3. Your application will be available at: $appURL"
Write-Host ""
Write-Warning "Important: Make sure your GitHub repository is public or configure SSH keys for private repos!"
Write-Warning "The deployment script will clone from: https://github.com/hukumdev010/exam_center.git"

# Create a deployment summary file
$summaryFile = "deployment-summary.txt"
@"
Exam Center AWS Deployment Summary
==================================

Stack Name: $StackName
Region: $Region
Public IP: $publicIP
Application URL: $appURL

SSH Command: ssh -i your-key.pem ubuntu@$publicIP

Next Steps:
1. SSH into the server
2. Run: sudo /opt/exam-center/deploy-from-git.sh
3. Check status: sudo systemctl status exam-center
4. View logs: sudo journalctl -u exam-center -f

Deployment completed at: $(Get-Date)
"@ | Out-File -FilePath $summaryFile -Encoding UTF8

Write-Status "Deployment summary saved to: $summaryFile"
