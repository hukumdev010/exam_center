"""AWS SysOps Administrator Associate Certification"""

CERTIFICATION = {
    "name": "AWS Certified SysOps Administrator - Associate",
    "description": "Deploy, manage, and operate scalable, highly available, and fault tolerant systems on AWS",
    "slug": "aws-sysops-administrator-associate",
    "level": "Associate",
    "duration": 130,
    "questions_count": 65,
    "category_slug": "aws",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which AWS service should you use to monitor and troubleshoot application performance?",
        "explanation": "AWS X-Ray is a service that collects data about requests that your application serves, and provides tools you can use to view, filter, and gain insights into that data to identify issues and opportunities for optimization.",
        "reference": "https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html",
        "points": 1,
        "answers": [
            {"text": "AWS X-Ray", "is_correct": True},
            {"text": "AWS Config", "is_correct": False},
            {"text": "AWS CloudTrail", "is_correct": False},
            {"text": "AWS Inspector", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of AWS Systems Manager?",
        "explanation": "AWS Systems Manager is a collection of capabilities that helps you automate management tasks such as collecting system inventory, applying OS patches, automating the creation of Amazon Machine Images (AMIs), and configuring operating systems (OSs) and applications at scale.",
        "reference": "https://docs.aws.amazon.com/systems-manager/",
        "points": 1,
        "answers": [
            {"text": "Automate management tasks for AWS resources", "is_correct": True},
            {"text": "Monitor network traffic", "is_correct": False},
            {"text": "Manage DNS records", "is_correct": False},
            {"text": "Create load balancers", "is_correct": False}
        ]
    },
    {
        "text": "Which AWS service provides automated backup for EC2 instances?",
        "explanation": "AWS Backup is a centralized backup service that makes it easy and cost-effective for you to backup your application data across AWS services in the AWS cloud, including Amazon EBS volumes, Amazon EC2 instances, Amazon RDS databases, Amazon DynamoDB tables, Amazon EFS file systems, Amazon FSx file systems, and AWS Storage Gateway volumes.",
        "reference": "https://docs.aws.amazon.com/aws-backup/",
        "points": 1,
        "answers": [
            {"text": "AWS Backup", "is_correct": True},
            {"text": "Amazon S3", "is_correct": False},
            {"text": "AWS CloudFormation", "is_correct": False},
            {"text": "Amazon EBS Snapshots only", "is_correct": False}
        ]
    },
    {
        "text": "What is AWS CloudWatch used for?",
        "explanation": "Amazon CloudWatch is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers. CloudWatch provides you with data and actionable insights to monitor your applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health.",
        "reference": "https://docs.aws.amazon.com/cloudwatch/",
        "points": 1,
        "answers": [
            {"text": "Monitoring and observability of AWS resources", "is_correct": True},
            {"text": "Source code version control", "is_correct": False},
            {"text": "Database administration", "is_correct": False},
            {"text": "Network security", "is_correct": False}
        ]
    },
    {
        "text": "Which service helps you analyze and optimize AWS costs?",
        "explanation": "AWS Cost Explorer is a tool that enables you to view and analyze your costs and usage. You can explore your usage and costs using the main graph, the Cost Explorer cost and usage reports, or the Cost Explorer RI reports.",
        "reference": "https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html",
        "points": 1,
        "answers": [
            {"text": "AWS Cost Explorer", "is_correct": True},
            {"text": "AWS CloudFormation", "is_correct": False},
            {"text": "AWS Config", "is_correct": False},
            {"text": "AWS CloudTrail", "is_correct": False}
        ]
    }
]
