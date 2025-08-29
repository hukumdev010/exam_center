// Sample question data for different AWS certifications

export const certificationQuestions = {
  "solutions-architect-associate": [
    {
      id: 1,
      text: "Which AWS service is used for object storage?",
      explanation: "Amazon S3 (Simple Storage Service) is designed for object storage. It provides industry-leading scalability, data availability, security, and performance.",
      points: 1,
      answers: [
        { id: 1, text: "Amazon S3", isCorrect: true },
        { id: 2, text: "Amazon EBS", isCorrect: false },
        { id: 3, text: "Amazon EFS", isCorrect: false },
        { id: 4, text: "Amazon FSx", isCorrect: false },
      ],
    },
    {
      id: 2,
      text: "Which service provides serverless compute in AWS?",
      explanation: "AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume.",
      points: 1,
      answers: [
        { id: 5, text: "AWS Lambda", isCorrect: true },
        { id: 6, text: "Amazon EC2", isCorrect: false },
        { id: 7, text: "Amazon ECS", isCorrect: false },
        { id: 8, text: "AWS Batch", isCorrect: false },
      ],
    },
    {
      id: 3,
      text: "What is the purpose of Amazon VPC?",
      explanation: "Amazon VPC (Virtual Private Cloud) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.",
      points: 1,
      answers: [
        { id: 9, text: "To create an isolated network environment", isCorrect: true },
        { id: 10, text: "To store files and objects", isCorrect: false },
        { id: 11, text: "To run containerized applications", isCorrect: false },
        { id: 12, text: "To manage user permissions", isCorrect: false },
      ],
    },
    {
      id: 4,
      text: "Which AWS service is best for hosting a relational database?",
      explanation: "Amazon RDS (Relational Database Service) makes it easy to set up, operate, and scale a relational database in the cloud with support for MySQL, PostgreSQL, Oracle, SQL Server, and more.",
      points: 1,
      answers: [
        { id: 13, text: "Amazon RDS", isCorrect: true },
        { id: 14, text: "Amazon S3", isCorrect: false },
        { id: 15, text: "Amazon DynamoDB", isCorrect: false },
        { id: 16, text: "Amazon ElastiCache", isCorrect: false },
      ],
    },
    {
      id: 5,
      text: "What is the maximum size of an S3 object?",
      explanation: "The maximum size of an S3 object is 5TB. For objects larger than 100MB, AWS recommends using multipart upload.",
      points: 1,
      answers: [
        { id: 17, text: "5TB", isCorrect: true },
        { id: 18, text: "1TB", isCorrect: false },
        { id: 19, text: "100GB", isCorrect: false },
        { id: 20, text: "10TB", isCorrect: false },
      ],
    },
  ],
  
  "developer-associate": [
    {
      id: 1,
      text: "Which AWS service is primarily used for application deployment and management?",
      explanation: "AWS Elastic Beanstalk is designed for easy application deployment and management. It handles the deployment details while you focus on your application code.",
      points: 1,
      answers: [
        { id: 1, text: "AWS Elastic Beanstalk", isCorrect: true },
        { id: 2, text: "AWS CodePipeline", isCorrect: false },
        { id: 3, text: "Amazon ECS", isCorrect: false },
        { id: 4, text: "AWS Lambda", isCorrect: false },
      ],
    },
    {
      id: 2,
      text: "What is the best way to store user session data for a web application on AWS?",
      explanation: "Amazon DynamoDB provides fast, predictable performance and is ideal for storing user session data with automatic scaling.",
      points: 1,
      answers: [
        { id: 5, text: "Amazon DynamoDB", isCorrect: true },
        { id: 6, text: "Amazon S3", isCorrect: false },
        { id: 7, text: "Amazon RDS", isCorrect: false },
        { id: 8, text: "Amazon EFS", isCorrect: false },
      ],
    },
    {
      id: 3,
      text: "Which service helps in continuous integration and continuous deployment (CI/CD)?",
      explanation: "AWS CodePipeline is a continuous integration and continuous delivery service for fast and reliable application and infrastructure updates.",
      points: 1,
      answers: [
        { id: 9, text: "AWS CodePipeline", isCorrect: true },
        { id: 10, text: "AWS CodeCommit", isCorrect: false },
        { id: 11, text: "AWS CodeBuild", isCorrect: false },
        { id: 12, text: "AWS CodeDeploy", isCorrect: false },
      ],
    },
  ],
  
  "sysops-administrator-associate": [
    {
      id: 1,
      text: "Which service is used for monitoring AWS resources and applications?",
      explanation: "Amazon CloudWatch provides monitoring for AWS resources and applications, collecting and tracking metrics, collecting and monitoring log files, and setting alarms.",
      points: 1,
      answers: [
        { id: 1, text: "Amazon CloudWatch", isCorrect: true },
        { id: 2, text: "AWS CloudTrail", isCorrect: false },
        { id: 3, text: "AWS Config", isCorrect: false },
        { id: 4, text: "AWS Inspector", isCorrect: false },
      ],
    },
    {
      id: 2,
      text: "What service provides automated backup for EBS volumes?",
      explanation: "AWS Backup provides a centralized backup service that automates and centralizes backup across AWS services, including EBS volumes.",
      points: 1,
      answers: [
        { id: 5, text: "AWS Backup", isCorrect: true },
        { id: 6, text: "Amazon S3", isCorrect: false },
        { id: 7, text: "AWS Snapshot", isCorrect: false },
        { id: 8, text: "Amazon EBS Snapshots", isCorrect: false },
      ],
    },
  ],
  
  "solutions-architect-professional": [
    {
      id: 1,
      text: "In a multi-region architecture, which AWS service provides the lowest latency for global users accessing static content?",
      explanation: "Amazon CloudFront is a global content delivery network (CDN) that delivers content with the lowest latency by serving from edge locations closest to users.",
      points: 1,
      answers: [
        { id: 1, text: "Amazon CloudFront", isCorrect: true },
        { id: 2, text: "Amazon S3 Cross-Region Replication", isCorrect: false },
        { id: 3, text: "AWS Global Accelerator", isCorrect: false },
        { id: 4, text: "Amazon Route 53", isCorrect: false },
      ],
    },
    {
      id: 2,
      text: "Which pattern is best for implementing a microservices architecture on AWS?",
      explanation: "Amazon ECS with Application Load Balancer provides container orchestration with service discovery and load balancing, ideal for microservices.",
      points: 1,
      answers: [
        { id: 5, text: "Amazon ECS with Application Load Balancer", isCorrect: true },
        { id: 6, text: "Amazon EC2 with Classic Load Balancer", isCorrect: false },
        { id: 7, text: "AWS Lambda with API Gateway", isCorrect: false },
        { id: 8, text: "Amazon EKS with Network Load Balancer", isCorrect: false },
      ],
    },
  ],
  
  "devops-engineer-professional": [
    {
      id: 1,
      text: "Which AWS service is best for implementing Infrastructure as Code (IaC)?",
      explanation: "AWS CloudFormation provides infrastructure as code capabilities, allowing you to define AWS resources using templates.",
      points: 1,
      answers: [
        { id: 1, text: "AWS CloudFormation", isCorrect: true },
        { id: 2, text: "AWS Config", isCorrect: false },
        { id: 3, text: "AWS Systems Manager", isCorrect: false },
        { id: 4, text: "AWS OpsWorks", isCorrect: false },
      ],
    },
  ],
  
  "security-specialty": [
    {
      id: 1,
      text: "Which service provides centralized logging for security events across AWS services?",
      explanation: "AWS CloudTrail provides logging of API calls and events across AWS services, essential for security auditing and compliance.",
      points: 1,
      answers: [
        { id: 1, text: "AWS CloudTrail", isCorrect: true },
        { id: 2, text: "Amazon CloudWatch", isCorrect: false },
        { id: 3, text: "AWS Config", isCorrect: false },
        { id: 4, text: "Amazon GuardDuty", isCorrect: false },
      ],
    },
    {
      id: 2,
      text: "What is the best practice for managing secrets in AWS applications?",
      explanation: "AWS Secrets Manager provides secure storage and automatic rotation of secrets like passwords, API keys, and database credentials.",
      points: 1,
      answers: [
        { id: 5, text: "AWS Secrets Manager", isCorrect: true },
        { id: 6, text: "Amazon S3 with encryption", isCorrect: false },
        { id: 7, text: "AWS Systems Manager Parameter Store", isCorrect: false },
        { id: 8, text: "Hard-code in application", isCorrect: false },
      ],
    },
  ],
};

export const certificationNames = {
  "solutions-architect-associate": "AWS Certified Solutions Architect – Associate",
  "developer-associate": "AWS Certified Developer – Associate", 
  "sysops-administrator-associate": "AWS Certified SysOps Administrator – Associate",
  "solutions-architect-professional": "AWS Certified Solutions Architect – Professional",
  "devops-engineer-professional": "AWS Certified DevOps Engineer – Professional",
  "security-specialty": "AWS Certified Security – Specialty",
};
