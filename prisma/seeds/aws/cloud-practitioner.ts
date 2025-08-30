import { PrismaClient } from '../../../src/generated/prisma'

export async function seedAwsCloudPractitioner(prisma: PrismaClient, categoryId: number) {
  // AWS Cloud Practitioner Certification
  const awsCloudPractitioner = await prisma.certification.create({
    data: {
      name: 'AWS Certified Cloud Practitioner',
      description: 'Entry-level AWS certification covering cloud computing fundamentals, AWS core services, security, architecture, pricing, and support models. Perfect for individuals who want to demonstrate foundational knowledge of the AWS Cloud.',
      slug: 'aws-cloud-practitioner',
      level: 'Foundational',
      duration: 90,
      questionsCount: 65,
      categoryId,
      questions: {
        create: [
          {
            text: 'What are the six advantages of cloud computing according to AWS?',
            explanation: 'AWS identifies six key advantages of cloud computing: 1) Trade capital expense for variable expense - pay only for what you consume, 2) Benefit from massive economies of scale - lower variable costs due to AWS scale, 3) Stop guessing about capacity - eliminate guesswork about infrastructure needs, 4) Increase speed and agility - reduce time to make resources available, 5) Stop spending money running and maintaining data centers - focus on business differentiators, and 6) Go global in minutes - easily deploy globally. Reference: https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html',
            points: 1,
            answers: {
              create: [
                { text: 'Trade CapEx for OpEx, economies of scale, stop guessing capacity, increase agility, stop maintaining data centers, go global in minutes', isCorrect: true },
                { text: 'Security, compliance, performance, availability, durability, and cost optimization', isCorrect: false },
                { text: 'Infrastructure, platform, software, monitoring, backup, and networking services', isCorrect: false },
                { text: 'Compute, storage, database, networking, analytics, and machine learning capabilities', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the AWS Well-Architected Framework and what are its five pillars?',
            explanation: 'The AWS Well-Architected Framework helps you understand the pros and cons of decisions you make while building systems on AWS. It consists of five pillars: 1) Operational Excellence - run and monitor systems to deliver business value, 2) Security - protect information, systems, and assets, 3) Reliability - recover from failures and meet demand, 4) Performance Efficiency - use computing resources efficiently, and 5) Cost Optimization - avoid unnecessary costs. Reference: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'Operational Excellence, Security, Reliability, Performance Efficiency, and Cost Optimization', isCorrect: true },
                { text: 'Compute, Storage, Database, Networking, and Security', isCorrect: false },
                { text: 'Planning, Design, Implementation, Testing, and Deployment', isCorrect: false },
                { text: 'Infrastructure, Platform, Software, Monitoring, and Analytics', isCorrect: false },
              ],
            },
          },
          {
            text: 'Which AWS service provides a virtual private cloud (VPC) environment?',
            explanation: 'Amazon VPC (Virtual Private Cloud) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including selection of IP address range, creation of subnets, and configuration of route tables and network gateways. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html',
            points: 1,
            answers: {
              create: [
                { text: 'Amazon VPC (Virtual Private Cloud)', isCorrect: true },
                { text: 'Amazon EC2', isCorrect: false },
                { text: 'AWS Direct Connect', isCorrect: false },
                { text: 'Amazon Route 53', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Amazon S3 and what are its primary use cases?',
            explanation: 'Amazon S3 (Simple Storage Service) is an object storage service that offers industry-leading scalability, data availability, security, and performance. Primary use cases include: backup and restore, disaster recovery, archive, data lakes and big data analytics, hybrid cloud storage, and content distribution. S3 provides 99.999999999% (11 9s) of data durability. Reference: https://docs.aws.amazon.com/s3/latest/userguide/Welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'Object storage service for backup, archive, data lakes, and content distribution', isCorrect: true },
                { text: 'Relational database service for OLTP workloads', isCorrect: false },
                { text: 'Content delivery network for global content distribution', isCorrect: false },
                { text: 'Virtual server hosting service in the cloud', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between AWS Regions, Availability Zones, and Edge Locations?',
            explanation: 'AWS Regions are separate geographic areas with multiple isolated locations called Availability Zones (AZs). Each Region has at least 3 AZs, which are physically separate data centers with independent power, cooling, and networking. Edge Locations are endpoints for CloudFront (CDN) that are located in major cities worldwide for content caching. Currently, there are 31+ Regions, 99+ AZs, and 400+ Edge Locations globally. Reference: https://aws.amazon.com/about-aws/global-infrastructure/',
            points: 1,
            answers: {
              create: [
                { text: 'Regions are geographic areas, AZs are isolated data centers within regions, Edge Locations are CDN endpoints', isCorrect: true },
                { text: 'All three terms refer to the same AWS infrastructure concept', isCorrect: false },
                { text: 'Regions are for storage, AZs are for compute, Edge Locations are for networking', isCorrect: false },
                { text: 'Regions are virtual, AZs are physical, Edge Locations are hybrid environments', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is AWS IAM and what are its core components?',
            explanation: 'AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Core components include: Users (individual people or applications), Groups (collections of users), Roles (set of permissions that can be assumed), and Policies (documents that define permissions using JSON). IAM follows the principle of least privilege and provides fine-grained access control. Reference: https://docs.aws.amazon.com/iam/latest/userguide/introduction.html',
            points: 1,
            answers: {
              create: [
                { text: 'Identity and Access Management service with Users, Groups, Roles, and Policies', isCorrect: true },
                { text: 'Infrastructure monitoring service for AWS resources', isCorrect: false },
                { text: 'Instance management service for EC2 virtual machines', isCorrect: false },
                { text: 'Integration and automation service for DevOps workflows', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Amazon EC2 and what are the different instance families?',
            explanation: 'Amazon EC2 (Elastic Compute Cloud) provides scalable computing capacity in the AWS cloud. Instance families include: General Purpose (A, T, M series) for diverse workloads, Compute Optimized (C series) for CPU-intensive tasks, Memory Optimized (R, X, Z series) for memory-intensive applications, Storage Optimized (I, D, H series) for high sequential read/write, and Accelerated Computing (P, G, F series) for GPU/FPGA workloads. Reference: https://docs.aws.amazon.com/ec2/latest/userguide/instance-types.html',
            points: 1,
            answers: {
              create: [
                { text: 'Virtual server service with General Purpose, Compute, Memory, Storage, and Accelerated Computing instances', isCorrect: true },
                { text: 'Container orchestration service for microservices applications', isCorrect: false },
                { text: 'Database management service for relational databases', isCorrect: false },
                { text: 'Content delivery network for global web applications', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the different AWS pricing models?',
            explanation: 'AWS offers several pricing models: 1) Pay-as-you-go - pay only for what you use with no upfront costs, 2) Reserved Instances - commit to usage for 1-3 years for up to 75% savings, 3) Spot Instances - bid for unused capacity for up to 90% savings, 4) Dedicated Hosts - physical servers dedicated for your use, and 5) Savings Plans - flexible pricing model for compute services. AWS also offers Free Tier for new accounts. Reference: https://aws.amazon.com/pricing/',
            points: 1,
            answers: {
              create: [
                { text: 'Pay-as-you-go, Reserved Instances, Spot Instances, Dedicated Hosts, and Savings Plans', isCorrect: true },
                { text: 'Monthly subscription, annual contract, and enterprise licensing only', isCorrect: false },
                { text: 'Fixed pricing for all services with volume discounts', isCorrect: false },
                { text: 'Free tier only with paid premium features', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is AWS CloudFormation and how does it support Infrastructure as Code?',
            explanation: 'AWS CloudFormation is a service that gives developers and businesses an easy way to create a collection of related AWS and third-party resources and provision them in an orderly and predictable fashion. It uses templates written in JSON or YAML to describe resources and their dependencies. Benefits include version control, repeatability, rollback capabilities, and cost tracking. It supports Infrastructure as Code (IaC) principles. Reference: https://docs.aws.amazon.com/cloudformation/latest/userguide/Welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'Infrastructure as Code service that uses JSON/YAML templates to provision AWS resources', isCorrect: true },
                { text: 'Content delivery network for static website hosting', isCorrect: false },
                { text: 'Database migration service for legacy applications', isCorrect: false },
                { text: 'Monitoring and alerting service for cloud resources', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the AWS Shared Responsibility Model?',
            explanation: 'The AWS Shared Responsibility Model defines security and compliance responsibilities between AWS and the customer. AWS is responsible for "Security OF the Cloud" - protecting infrastructure, hardware, software, networking, and facilities. Customers are responsible for "Security IN the Cloud" - including customer data, identity and access management, application-level security, operating system updates, network traffic protection, and firewall configuration. Reference: https://aws.amazon.com/compliance/shared-responsibility-model/',
            points: 1,
            answers: {
              create: [
                { text: 'AWS secures the infrastructure (Security OF the Cloud), customers secure their data and applications (Security IN the Cloud)', isCorrect: true },
                { text: 'AWS is responsible for all security aspects of cloud computing', isCorrect: false },
                { text: 'Customers are fully responsible for all security in the cloud', isCorrect: false },
                { text: 'Security responsibilities are split 50/50 between AWS and customers', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Amazon RDS and what database engines does it support?',
            explanation: 'Amazon RDS (Relational Database Service) is a managed database service that makes it easy to set up, operate, and scale relational databases in the cloud. Supported engines include: Amazon Aurora (MySQL and PostgreSQL compatible), PostgreSQL, MySQL, MariaDB, Oracle Database, and Microsoft SQL Server. RDS handles routine database tasks like provisioning, patching, backup, recovery, failure detection, and repair. Reference: https://docs.aws.amazon.com/rds/latest/userguide/Welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'Managed relational database service supporting Aurora, PostgreSQL, MySQL, MariaDB, Oracle, and SQL Server', isCorrect: true },
                { text: 'NoSQL document database service for web applications', isCorrect: false },
                { text: 'Data warehousing service for analytics workloads', isCorrect: false },
                { text: 'In-memory caching service for application acceleration', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Amazon CloudFront and how does it improve performance?',
            explanation: 'Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds. It uses a global network of 400+ edge locations and regional edge caches. CloudFront improves performance by caching content closer to users, reducing origin server load, and providing DDoS protection through AWS Shield. Reference: https://docs.aws.amazon.com/cloudfront/latest/developerguide/Introduction.html',
            points: 1,
            answers: {
              create: [
                { text: 'Global CDN service that caches content at edge locations for faster delivery and lower latency', isCorrect: true },
                { text: 'Virtual private network service for secure remote access', isCorrect: false },
                { text: 'Load balancing service for distributing application traffic', isCorrect: false },
                { text: 'DNS service for domain name resolution', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the main benefits of using AWS Lambda?',
            explanation: 'AWS Lambda is a serverless compute service that runs code without provisioning or managing servers. Key benefits include: no server management, automatic scaling, pay-per-request pricing (you pay only for compute time consumed), built-in fault tolerance and high availability, integration with other AWS services, support for multiple programming languages, and fast deployment. Lambda automatically scales from a few requests per day to thousands per second. Reference: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'Serverless computing with no server management, automatic scaling, and pay-per-execution pricing', isCorrect: true },
                { text: 'Virtual machine hosting with full operating system control', isCorrect: false },
                { text: 'Container orchestration with Kubernetes compatibility', isCorrect: false },
                { text: 'Database hosting with automatic backup and recovery', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is AWS CloudWatch and what types of monitoring does it provide?',
            explanation: 'AWS CloudWatch is a monitoring and observability service that provides data and actionable insights for AWS resources and applications. It offers: Metrics (numerical data about your systems), Logs (centralized log management), Events (system events and schedule-based triggers), Alarms (notifications based on thresholds), Dashboards (customizable views), and Application Insights (automated monitoring for applications). CloudWatch helps with performance monitoring, troubleshooting, and resource optimization. Reference: https://docs.aws.amazon.com/cloudwatch/latest/monitoring/WhatIsCloudWatch.html',
            points: 1,
            answers: {
              create: [
                { text: 'Monitoring service providing metrics, logs, events, alarms, and dashboards for AWS resources', isCorrect: true },
                { text: 'Security service for threat detection and incident response', isCorrect: false },
                { text: 'Backup service for data protection and disaster recovery', isCorrect: false },
                { text: 'Networking service for VPC configuration and management', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the AWS Free Tier and what are its three types?',
            explanation: 'AWS Free Tier allows you to explore and try out AWS services free of charge. Three types: 1) Always Free - services that never expire (like 1 million AWS Lambda requests per month), 2) 12 Months Free - services free for 12 months from account creation date (like 750 hours of EC2 t2.micro instances), and 3) Trials - short-term free trials for specific services (like 30-day free trial for Amazon Inspector). The Free Tier helps new users learn AWS without incurring costs. Reference: https://aws.amazon.com/free/',
            points: 1,
            answers: {
              create: [
                { text: 'Always Free (never expire), 12 Months Free (from account creation), and Trials (short-term)', isCorrect: true },
                { text: 'Basic, Standard, and Premium tiers with different feature sets', isCorrect: false },
                { text: 'Developer, Business, and Enterprise support levels', isCorrect: false },
                { text: 'Regional, Global, and Edge location access tiers', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Amazon DynamoDB and when should you use it?',
            explanation: 'Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. It supports both document and key-value data models. Use DynamoDB for: mobile, web, gaming, ad tech, and IoT applications requiring single-digit millisecond latency, applications with unpredictable traffic patterns, serverless applications, and when you need automatic scaling without downtime. It offers features like Global Tables, Point-in-time Recovery, and DynamoDB Accelerator (DAX). Reference: https://docs.aws.amazon.com/dynamodb/latest/developerguide/Introduction.html',
            points: 1,
            answers: {
              create: [
                { text: 'Fully managed NoSQL database for applications requiring fast, predictable performance and seamless scaling', isCorrect: true },
                { text: 'Relational database service optimized for complex SQL queries and transactions', isCorrect: false },
                { text: 'Data warehousing service for business intelligence and analytics', isCorrect: false },
                { text: 'File storage service for network-attached storage requirements', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is AWS Support and what are the different support plans?',
            explanation: 'AWS Support offers four support plans: 1) Basic (free) - customer service and communities, basic documentation, whitepapers, and support center, 2) Developer ($29/month) - business hours email support, general guidance, 3) Business ($100/month) - 24x7 phone/email/chat support, infrastructure guidance, use-case guidance, 4) Enterprise ($15,000/month) - dedicated Technical Account Manager, concierge support, infrastructure event management, and business reviews. Each plan offers different response times and support levels. Reference: https://aws.amazon.com/support/plans/',
            points: 1,
            answers: {
              create: [
                { text: 'Basic (free), Developer ($29/month), Business ($100/month), and Enterprise ($15,000/month)', isCorrect: true },
                { text: 'Free, Standard, Premium, and Ultimate support tiers', isCorrect: false },
                { text: 'Community, Professional, Business, and Enterprise editions', isCorrect: false },
                { text: 'Regional, National, Global, and Worldwide support levels', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is AWS Elastic Load Balancer (ELB) and what types are available?',
            explanation: 'AWS Elastic Load Balancer (ELB) automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, and IP addresses. Three types: 1) Application Load Balancer (ALB) - operates at layer 7 (HTTP/HTTPS), best for modern applications, 2) Network Load Balancer (NLB) - operates at layer 4 (TCP/UDP), ultra-high performance and static IP, 3) Classic Load Balancer - legacy option for applications built within EC2-Classic network. ELB provides high availability and fault tolerance. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html',
            points: 1,
            answers: {
              create: [
                { text: 'Traffic distribution service with Application (Layer 7), Network (Layer 4), and Classic load balancers', isCorrect: true },
                { text: 'Auto scaling service for automatically adjusting EC2 instance capacity', isCorrect: false },
                { text: 'Content delivery service for global content distribution', isCorrect: false },
                { text: 'DNS service for routing internet traffic to AWS resources', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is AWS Auto Scaling and how does it work?',
            explanation: 'AWS Auto Scaling monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost. It provides a unified scaling experience across multiple services including EC2, ECS, DynamoDB, and Aurora. Auto Scaling uses scaling policies based on metrics like CPU utilization, network I/O, or custom metrics. It can scale out (add instances) during demand spikes and scale in (remove instances) during low demand, ensuring you only pay for what you need. Reference: https://docs.aws.amazon.com/autoscaling/latest/userguide/what-is-aws-auto-scaling.html',
            points: 1,
            answers: {
              create: [
                { text: 'Service that automatically adjusts capacity across multiple AWS services based on demand and policies', isCorrect: true },
                { text: 'Load balancing service that distributes traffic across multiple instances', isCorrect: false },
                { text: 'Monitoring service that tracks performance metrics and generates alerts', isCorrect: false },
                { text: 'Backup service that automatically creates snapshots of your data', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between horizontal and vertical scaling in AWS?',
            explanation: 'Horizontal scaling (scale out/in) involves adding or removing instances to handle changes in demand. Examples include Auto Scaling Groups adding EC2 instances or Lambda automatically spawning more function executions. Vertical scaling (scale up/down) involves changing the size or capacity of existing resources. Examples include changing EC2 instance types or increasing EBS volume size. Horizontal scaling provides better fault tolerance and is generally preferred in cloud architectures, while vertical scaling has limits and potential downtime. Reference: AWS Architecture Center - Scaling patterns',
            points: 1,
            answers: {
              create: [
                { text: 'Horizontal scaling adds/removes instances, vertical scaling changes instance size/capacity', isCorrect: true },
                { text: 'Horizontal scaling changes CPU/memory, vertical scaling adds storage capacity', isCorrect: false },
                { text: 'Horizontal scaling is for databases, vertical scaling is for web servers', isCorrect: false },
                { text: 'Horizontal scaling is automatic, vertical scaling requires manual intervention', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  console.log(`✅ Seeded AWS Cloud Practitioner certification with ${awsCloudPractitioner.questionsCount} questions`)
  return awsCloudPractitioner
}
