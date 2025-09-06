# AWS EC2 Deployment Guide - Free Tier

This guide will help you deploy your FastAPI backend to AWS EC2 using the free tier resources.

## Prerequisites

1. **AWS Account**: Create a free AWS account if you don't have one
2. **AWS CLI**: Install and configure AWS CLI
3. **EC2 Key Pair**: Create an EC2 key pair in your target AWS region

## Free Tier Resources Used

- **EC2**: t2.micro instance (750 hours/month free)
- **RDS**: db.t3.micro PostgreSQL (750 hours/month free, 20GB storage)
- **VPC**: Virtual Private Cloud (free)
- **Elastic IP**: 1 free static IP
- **Data Transfer**: 15GB outbound per month

## Step-by-Step Deployment

### 1. Install AWS CLI

```bash
# On Linux/Mac
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Verify installation
aws --version
```

### 2. Configure AWS CLI

```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter your preferred region (e.g., us-east-1)
# Enter output format (json)
```

### 3. Create EC2 Key Pair

1. Go to AWS EC2 Console
2. Navigate to "Key Pairs" in the left menu
3. Click "Create key pair"
4. Name it (e.g., "exam-center-key")
5. Choose .pem format
6. Download and save the .pem file securely
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
