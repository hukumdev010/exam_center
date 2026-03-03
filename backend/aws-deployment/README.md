# AWS Deployment Guide for Exam Center

This directory contains the AWS CloudFormation template and deployment scripts for deploying the Exam Center FastAPI backend to AWS using free tier resources.

## Prerequisites

1. **AWS Account**: You need an AWS account with appropriate permissions
2. **AWS CLI**: Install and configure AWS CLI
3. **SSH Key Pair**: Create an EC2 Key Pair in your AWS region
4. **Git Repository**: Your code should be pushed to GitHub (public repo or configure SSH keys)

## Architecture

The deployment creates:
- **VPC** with public and private subnets
- **EC2 instance** (t2.micro) running Ubuntu 24.04 with Python 3.10
- **RDS PostgreSQL** database (db.t3.micro)
- **Security Groups** for web server and database
- **Elastic IP** for consistent public IP address

## Deployment Steps

### Step 1: Infrastructure Deployment

1. **Open PowerShell** and navigate to the aws-deployment directory:
   ```powershell
   cd "C:\Users\bhabana basnet\Documents\personal\exam_center\aws-deployment"
   ```

2. **Deploy the CloudFormation stack**:
   ```powershell
   .\deploy.ps1 -KeyPairName "your-key-pair-name"
   ```
   
   You'll be prompted for:
   - Database password (minimum 8 characters)
   
   Optional parameters:
   ```powershell
   .\deploy.ps1 -StackName "exam-center-backend" -Region "us-east-1" -KeyPairName "your-key-pair" -DBUsername "examcenter" -DBPassword "yourpassword"
   ```

3. **Wait for deployment** (typically 10-15 minutes). The script will:
   - Create all AWS resources
   - Install Python 3.10 on the EC2 instance
   - Set up the environment for your application
   - Create deployment scripts

### Step 2: Code Deployment

After infrastructure deployment completes:

1. **Note the public IP** from the deployment output
2. **Deploy your code**:
   ```powershell
   .\deploy-code.ps1 -PublicIP "your-ec2-public-ip" -KeyFile "path\to\your-key.pem"
   ```

3. **The deployment script will**:
   - Connect to your EC2 instance
   - Clone the latest code from GitHub
   - Install Python dependencies
   - Run database migrations
   - Start the FastAPI application

### Step 3: Verify Deployment

1. **Check application status**:
   ```
   http://your-public-ip:8000
   http://your-public-ip:8000/docs  (API documentation)
   ```

2. **SSH to monitor** (if needed):
   ```bash
   ssh -i your-key.pem ubuntu@your-public-ip
   sudo systemctl status exam-center
   sudo journalctl -u exam-center -f
   ```

## Manual Code Updates

To update your application code after initial deployment:

1. **SSH to the instance**:
   ```bash
   ssh -i your-key.pem ubuntu@your-public-ip
   ```

2. **Run the deployment script**:
   ```bash
   sudo /opt/exam-center/deploy-from-git.sh
   ```

This will pull the latest changes from GitHub and restart the application.

## Configuration Files

- **CloudFormation Template**: `cloudformation-template.yaml`
- **PowerShell Deployment Script**: `deploy.ps1`
- **Code Deployment Script**: `deploy-code.ps1`

## Environment Variables

The following environment variables are automatically configured:
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Auto-generated JWT secret
- `ALGORITHM`: HS256
- `ACCESS_TOKEN_EXPIRE_MINUTES`: 30
- `DEBUG`: false
- `ENVIRONMENT`: production

## Monitoring and Troubleshooting

### Check Application Status
```bash
sudo systemctl status exam-center
```

### View Application Logs
```bash
sudo journalctl -u exam-center -f
```

### Restart Application
```bash
sudo systemctl restart exam-center
```

### Check Database Connection
```bash
cd /opt/exam-center
python3 -c "from database import engine; print('Database connection OK')"
```

## Security Considerations

1. **Database Password**: Use a strong password with at least 8 characters
2. **SSH Key**: Keep your SSH private key secure
3. **Security Groups**: The template opens ports 22, 80, 443, and 8000
4. **Secret Key**: A random secret key is generated automatically

## Cost Optimization

This deployment uses AWS Free Tier resources:
- **EC2**: t2.micro instance (750 hours/month free)
- **RDS**: db.t3.micro PostgreSQL (750 hours/month free)
- **Storage**: 20GB EBS storage (free tier included)

## Cleanup

To delete all resources and stop charges:

```powershell
aws cloudformation delete-stack --stack-name exam-center-backend --region us-east-1
```

## Troubleshooting

### Common Issues

1. **KeyPair not found**: Ensure you've created an EC2 Key Pair in the correct region
2. **GitHub access**: Make sure your repository is public or configure SSH keys
3. **Port issues**: Check security group settings if you can't access the application
4. **Database connection**: Verify the database is running and environment variables are correct

### Getting Help

1. Check CloudFormation events in AWS Console
2. SSH to the instance and check logs
3. Verify all environment variables are set correctly

## Repository Configuration

The deployment assumes your GitHub repository structure:
```
exam_center/
├── backend/          # FastAPI application
│   ├── main.py
│   ├── requirements.txt
│   ├── alembic.ini
│   └── ...
└── frontend/         # Optional frontend build
    └── out/          # Built static files
```

Make sure your repository is accessible and the backend directory contains all necessary files.

## Quick Start Commands

```powershell
# 1. Deploy infrastructure
.\deploy.ps1 -KeyPairName "exam-center-key"

# 2. Deploy code (replace with your actual IP and key file)
.\deploy-code.ps1 -PublicIP "54.123.45.67" -KeyFile ".\exam-center-key.pem"

# 3. Check application
# Open browser to: http://54.123.45.67:8000
```
7. Set correct permissions: `chmod 400 your-key.pem`

### 4. Update AMI ID for Your Region

Before deploying, update the AMI ID in `cloudformation-template.yaml`:

```yaml
# Line ~200 in cloudformation-template.yaml
ImageId: ami-xxxxxxxxx  # Update this for your region
```

**Find the right AMI ID for your region:**
- Go to AWS EC2 Console
- Click "Launch Instance"
- Select "Amazon Linux 2 AMI"
- Copy the AMI ID (starts with ami-)

### 5. Deploy Infrastructure

```bash
cd aws-deployment

# Deploy with interactive prompts
./deploy.sh

# Or deploy with parameters
./deploy.sh \
  --stack-name "exam-center-backend" \
  --region "us-east-1" \
  --key-pair "exam-center-key" \
  --db-username "examcenter" \
  --db-password "YourSecurePassword123"
```

This will create:
- VPC with public and private subnets
- Security groups
- RDS PostgreSQL database
- EC2 instance
- Elastic IP

### 6. Deploy Application Code

```bash
# Deploy your application code
./deploy-code.sh --key-file /path/to/your-key.pem

# Or with custom parameters
./deploy-code.sh \
  --stack-name "exam-center-backend" \
  --region "us-east-1" \
  --key-file "/path/to/exam-center-key.pem"
```

### 7. Access Your Application

After deployment, you'll get:
- **API Documentation**: `http://YOUR_IP:8000/docs`
- **API Base URL**: `http://YOUR_IP:8000/api`
- **SSH Access**: `ssh -i your-key.pem ec2-user@YOUR_IP`

## Configuration

### Environment Variables

The application uses these environment variables (automatically configured):

```env
DATABASE_URL=postgresql+asyncpg://username:password@db-endpoint:5432/examcenter
SECRET_KEY=your-secret-key-here-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Security Groups

- **Web Server**: Allows HTTP (80), HTTPS (443), SSH (22), and FastAPI (8000)
- **Database**: Only allows PostgreSQL (5432) from web server

## Management Commands

### Check Application Status
```bash
ssh -i your-key.pem ec2-user@YOUR_IP 'sudo systemctl status exam-center'
```

### View Application Logs
```bash
ssh -i your-key.pem ec2-user@YOUR_IP 'sudo journalctl -u exam-center -f'
```

### Restart Application
```bash
ssh -i your-key.pem ec2-user@YOUR_IP 'sudo systemctl restart exam-center'
```

### Update Application Code
Simply run the deploy-code.sh script again with your updated code.

## Monitoring and Costs

### Free Tier Limits
- **EC2**: 750 hours/month (run one t2.micro 24/7)
- **RDS**: 750 hours/month (run one db.t3.micro 24/7)
- **Storage**: 30GB EBS, 20GB RDS
- **Data Transfer**: 15GB outbound/month

### Cost Optimization
- Stop instances when not needed
- Use CloudWatch for monitoring
- Set up billing alerts

## Troubleshooting

### Application Won't Start
1. Check logs: `sudo journalctl -u exam-center -f`
2. Verify database connection
3. Check if all dependencies are installed

### Can't Connect to Database
1. Verify security group rules
2. Check RDS instance status
3. Verify DATABASE_URL in .env file

### SSH Connection Issues
1. Verify security group allows SSH (port 22)
2. Check key file permissions: `chmod 400 your-key.pem`
3. Use correct username: `ec2-user`

## Cleanup

To avoid ongoing charges, delete the CloudFormation stack when done:

```bash
aws cloudformation delete-stack \
  --stack-name "exam-center-backend" \
  --region "us-east-1"
```

## Security Considerations

1. **Change default SECRET_KEY** in production
2. **Use HTTPS** with SSL certificate (Let's Encrypt)
3. **Restrict SSH access** to your IP only
4. **Regular security updates** on EC2 instance
5. **Database backups** (consider enabling for production)

## Next Steps

1. Set up CI/CD pipeline with GitHub Actions
2. Configure custom domain with Route 53
3. Add SSL certificate with ACM
4. Set up CloudWatch monitoring and alerts
5. Configure auto-scaling (paid feature)
