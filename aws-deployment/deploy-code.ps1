# Code deployment script for Exam Center
# This script connects to the EC2 instance and deploys the latest code from GitHub
param(
    [string]$PublicIP = "",
    [string]$KeyFile = "",
    [switch]$Help
)

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
    Write-Host "Usage: .\deploy-code.ps1 [OPTIONS]"
    Write-Host "Options:"
    Write-Host "  -PublicIP IP          Public IP address of the EC2 instance"
    Write-Host "  -KeyFile PATH         Path to the SSH private key file (.pem)"
    Write-Host "  -Help                 Show this help message"
    Write-Host ""
    Write-Host "Example:"
    Write-Host "  .\deploy-code.ps1 -PublicIP 54.123.45.67 -KeyFile .\exam-center-key.pem"
    exit 0
}

# Get required parameters if not provided
if (-not $PublicIP) {
    $PublicIP = Read-Host "Enter the EC2 instance public IP address"
    if (-not $PublicIP) {
        Write-Error "Public IP is required"
        exit 1
    }
}

if (-not $KeyFile) {
    $KeyFile = Read-Host "Enter the path to your SSH private key file (.pem)"
    if (-not $KeyFile) {
        Write-Error "SSH key file is required"
        exit 1
    }
}

# Check if key file exists
if (-not (Test-Path $KeyFile)) {
    Write-Error "SSH key file not found: $KeyFile"
    exit 1
}

# Check if SSH is available (OpenSSH or PuTTY)
$sshCommand = $null
try {
    $null = Get-Command ssh -ErrorAction Stop
    $sshCommand = "ssh"
    Write-Status "Using OpenSSH"
} catch {
    try {
        $null = Get-Command plink -ErrorAction Stop
        $sshCommand = "plink"
        Write-Status "Using PuTTY plink"
    } catch {
        Write-Error "SSH client not found. Please install OpenSSH or PuTTY"
        exit 1
    }
}

Write-Status "Connecting to EC2 instance: $PublicIP"
Write-Status "Using SSH key: $KeyFile"

# Create deployment commands
$deployCommands = @(
    "echo 'Starting application deployment...'",
    "sudo /opt/exam-center/deploy-from-git.sh",
    "echo 'Checking application status...'",
    "sudo systemctl status exam-center --no-pager",
    "echo 'Application logs (last 20 lines):'",
    "sudo journalctl -u exam-center -n 20 --no-pager"
)

$commandString = $deployCommands -join " && "

if ($sshCommand -eq "ssh") {
    # Using OpenSSH
    Write-Status "Deploying code to EC2 instance..."
    ssh -i $KeyFile -o StrictHostKeyChecking=no ubuntu@$PublicIP $commandString
} else {
    # Using PuTTY plink
    Write-Status "Deploying code to EC2 instance..."
    plink -i $KeyFile -batch ubuntu@$PublicIP $commandString
}

if ($LASTEXITCODE -eq 0) {
    Write-Status "Code deployment completed successfully!"
    Write-Host ""
    Write-Status "Your application should now be running on:"
    Write-Host "  http://$PublicIP:8000"
    Write-Host ""
    Write-Status "To monitor the application:"
    Write-Host "  SSH: ssh -i $KeyFile ubuntu@$PublicIP"
    Write-Host "  Status: sudo systemctl status exam-center"
    Write-Host "  Logs: sudo journalctl -u exam-center -f"
} else {
    Write-Error "Code deployment failed. Please check the logs."
    Write-Host ""
    Write-Status "To troubleshoot:"
    Write-Host "  1. SSH to the instance: ssh -i $KeyFile ubuntu@$PublicIP"
    Write-Host "  2. Check deployment logs: sudo journalctl -u exam-center -f"
    Write-Host "  3. Manually run deployment: sudo /opt/exam-center/deploy-from-git.sh"
}
