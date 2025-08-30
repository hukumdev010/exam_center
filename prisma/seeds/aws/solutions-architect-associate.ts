import { PrismaClient } from '../../../src/generated/prisma'

export async function seedAwsSolutionsArchitectAssociate(prisma: PrismaClient, categoryId: number) {
  // AWS Solutions Architect Associate Certification
  const awsSolutionsArchitectAssociate = await prisma.certification.create({
    data: {
      name: 'AWS Certified Solutions Architect – Associate',
      description: 'Design and deploy scalable, highly available, and fault-tolerant systems on AWS. This certification validates expertise in designing distributed applications and systems on AWS platform, implementing cost control strategies, and selecting appropriate AWS services based on requirements.',
      slug: 'aws-solutions-architect-associate',
      level: 'Associate',
      duration: 130,
      questionsCount: 65,
      categoryId,
      questions: {
        create: [
          {
            text: 'Which AWS service is used for object storage and what are its main storage classes?',
            explanation: 'Amazon S3 (Simple Storage Service) is designed for object storage with multiple storage classes: S3 Standard (frequently accessed), S3 Intelligent-Tiering (automatic cost optimization), S3 Standard-IA (infrequent access), S3 One Zone-IA (single AZ), S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive (long-term archival). Each class offers different cost and access patterns. Reference: https://docs.aws.amazon.com/s3/latest/userguide/storage-class-intro.html',
            points: 1,
            answers: {
              create: [
                { text: 'Amazon S3 with storage classes including Standard, IA, Glacier, and Deep Archive', isCorrect: true },
                { text: 'Amazon EBS with different volume types for various performance needs', isCorrect: false },
                { text: 'Amazon EFS providing shared file system for multiple EC2 instances', isCorrect: false },
                { text: 'Amazon FSx offering high-performance file systems for compute workloads', isCorrect: false },
              ],
            },
          },
          {
            text: 'Which service provides serverless compute in AWS and what are its key limitations?',
            explanation: 'AWS Lambda lets you run code without provisioning or managing servers with a pay-per-request model. Key limitations include: 15-minute maximum execution time, 10GB memory limit, 512MB to 10GB temporary disk space (/tmp), 1000 concurrent executions by default (can be increased), 6MB synchronous request/response payload limit, and language runtime restrictions. Lambda is ideal for event-driven applications and microservices. Reference: https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html',
            points: 1,
            answers: {
              create: [
                { text: 'AWS Lambda with 15-minute execution limit, 10GB memory, and concurrent execution limits', isCorrect: true },
                { text: 'Amazon EC2 with various instance types and unlimited execution time', isCorrect: false },
                { text: 'Amazon ECS providing containerized applications with Docker support', isCorrect: false },
                { text: 'AWS Batch for large-scale parallel and high-performance computing jobs', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Amazon VPC and how do you design a multi-tier architecture?',
            explanation: 'Amazon VPC (Virtual Private Cloud) lets you provision a logically isolated section of AWS Cloud. A typical multi-tier architecture includes: Public subnets for web servers with internet gateway access, private subnets for application servers accessible only from public subnet, database subnets (often private) for data tier with no direct internet access, and NAT gateways/instances for outbound internet access from private subnets. Use security groups and NACLs for layered security. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html',
            points: 1,
            answers: {
              create: [
                { text: 'Isolated network with public subnets (web tier), private subnets (app tier), and database subnets', isCorrect: true },
                { text: 'Simple network configuration with all resources in public subnets for easy access', isCorrect: false },
                { text: 'Content delivery network for caching and accelerating web applications globally', isCorrect: false },
                { text: 'Load balancing service for distributing traffic across multiple availability zones', isCorrect: false },
              ],
            },
          },
          {
            text: 'Which AWS service provides managed relational databases and what engines are supported?',
            explanation: 'Amazon RDS (Relational Database Service) makes it easy to set up, operate, and scale relational databases. Supported engines: Amazon Aurora (MySQL/PostgreSQL compatible with up to 5x MySQL performance), MySQL, PostgreSQL, MariaDB, Oracle Database, and Microsoft SQL Server. RDS provides automated backups, software patching, automatic failure detection and recovery, read replicas for scalability, and Multi-AZ deployments for high availability. Reference: https://docs.aws.amazon.com/rds/latest/userguide/Welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'Amazon RDS supporting Aurora, MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server', isCorrect: true },
                { text: 'Amazon DynamoDB providing NoSQL document and key-value database services', isCorrect: false },
                { text: 'Amazon ElastiCache offering in-memory caching with Redis and Memcached', isCorrect: false },
                { text: 'Amazon Redshift providing petabyte-scale data warehousing and analytics', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Amazon CloudFront and how does it integrate with other AWS services?',
            explanation: 'Amazon CloudFront is a global CDN service that delivers content with low latency using edge locations worldwide. Integration includes: S3 as origin for static content, EC2/ALB as custom origins for dynamic content, Lambda@Edge for edge computing, AWS Certificate Manager for SSL/TLS certificates, AWS WAF for web application firewall protection, and Route 53 for DNS routing. CloudFront also provides real-time logs, detailed analytics, and DDoS protection via AWS Shield. Reference: https://docs.aws.amazon.com/cloudfront/latest/developerguide/Introduction.html',
            points: 1,
            answers: {
              create: [
                { text: 'Global CDN service integrating with S3, EC2, Lambda@Edge, WAF, and Shield for content delivery', isCorrect: true },
                { text: 'Regional file storage service for mounting shared file systems across EC2 instances', isCorrect: false },
                { text: 'Database service for storing and querying time-series data from IoT devices', isCorrect: false },
                { text: 'Container orchestration service for managing Docker containers at scale', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement high availability for EC2 instances across multiple Availability Zones?',
            explanation: 'High availability across AZs involves: Auto Scaling Groups spanning multiple AZs with desired capacity, minimum, and maximum instances; Application Load Balancer (ALB) or Network Load Balancer distributing traffic across AZs; RDS Multi-AZ deployments for database failover; EBS snapshots stored across multiple AZs; S3 cross-region replication for data durability; and Route 53 health checks for DNS failover. This ensures fault tolerance against individual AZ failures. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html',
            points: 1,
            answers: {
              create: [
                { text: 'Auto Scaling Groups across multiple AZs with load balancers and multi-AZ database deployments', isCorrect: true },
                { text: 'Single large EC2 instance with increased storage and memory for better performance', isCorrect: false },
                { text: 'Multiple instances in single AZ with local load balancing and shared storage', isCorrect: false },
                { text: 'Container-based architecture using single availability zone with backup containers', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the different types of Elastic Load Balancers and when to use each?',
            explanation: 'AWS offers three types of load balancers: 1) Application Load Balancer (ALB) - operates at Layer 7 (HTTP/HTTPS), supports path-based routing, host-based routing, and integrates with AWS services like ECS and Lambda, ideal for modern applications; 2) Network Load Balancer (NLB) - operates at Layer 4 (TCP/UDP), provides ultra-high performance and static IP addresses, ideal for high-performance applications; 3) Classic Load Balancer - legacy option for applications built within EC2-Classic, operates at both Layer 4 and Layer 7. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html',
            points: 1,
            answers: {
              create: [
                { text: 'ALB for HTTP/HTTPS applications, NLB for high-performance TCP/UDP, CLB for legacy applications', isCorrect: true },
                { text: 'Only Application Load Balancer available for all types of traffic distribution', isCorrect: false },
                { text: 'Internal and External load balancers based on public vs private subnet deployment', isCorrect: false },
                { text: 'Regional and Global load balancers for different geographic distribution needs', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement data encryption in transit and at rest for AWS services?',
            explanation: 'Data encryption implementation: At Rest - S3 with SSE-S3/SSE-KMS/SSE-C, EBS encryption, RDS encryption, DynamoDB encryption, and Redshift encryption. In Transit - HTTPS/SSL for web traffic, VPC endpoints for private connections, AWS Certificate Manager for SSL certificates, and VPN/Direct Connect for network encryption. Use AWS KMS for key management with customer-managed keys (CMK) and automatic key rotation. Enable CloudTrail for audit logging of key usage. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/overview.html',
            points: 1,
            answers: {
              create: [
                { text: 'At rest: S3/EBS/RDS encryption with KMS; In transit: HTTPS/SSL with Certificate Manager', isCorrect: true },
                { text: 'Only application-level encryption using third-party tools and libraries', isCorrect: false },
                { text: 'Hardware security modules (HSM) required for all encryption operations', isCorrect: false },
                { text: 'Manual key management with customer-provided encryption keys only', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between Security Groups and Network ACLs in VPC?',
            explanation: 'Security Groups vs NACLs: Security Groups operate at instance level, are stateful (return traffic automatically allowed), support allow rules only, evaluate all rules before allowing traffic, and apply to instances explicitly associated. NACLs operate at subnet level, are stateless (return traffic must be explicitly allowed), support both allow and deny rules, process rules in numbered order, and apply to all instances in associated subnets automatically. Use both for defense-in-depth security strategy. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html',
            points: 1,
            answers: {
              create: [
                { text: 'Security Groups: instance-level, stateful, allow rules; NACLs: subnet-level, stateless, allow/deny rules', isCorrect: true },
                { text: 'Security Groups for external traffic, NACLs for internal VPC communication only', isCorrect: false },
                { text: 'Security Groups are free tier, NACLs require additional charges for advanced features', isCorrect: false },
                { text: 'Security Groups use IP addresses, NACLs use DNS names for rule configuration', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement disaster recovery with AWS services and what are the different strategies?',
            explanation: 'DR strategies in order of cost and complexity: 1) Backup and Restore - lowest cost, higher RTO/RPO, using S3/Glacier for backups; 2) Pilot Light - core services running in secondary region, faster recovery than backup/restore; 3) Warm Standby - scaled-down fully functional environment, faster recovery with some capacity always running; 4) Multi-Site Active/Active - full production environment in multiple regions, lowest RTO/RPO but highest cost. Use services like Route 53 for DNS failover, RDS cross-region replication, and S3 cross-region replication. Reference: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html',
            points: 1,
            answers: {
              create: [
                { text: 'Backup/Restore, Pilot Light, Warm Standby, and Multi-Site strategies with increasing cost and decreasing RTO', isCorrect: true },
                { text: 'Only automated backup solutions with point-in-time recovery capabilities', isCorrect: false },
                { text: 'Single region deployment with multiple availability zone redundancy', isCorrect: false },
                { text: 'Manual processes for data replication and application deployment', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the best practices for cost optimization in AWS architecture?',
            explanation: 'Cost optimization best practices: Right-sizing instances using CloudWatch metrics and AWS Compute Optimizer, using Reserved Instances and Savings Plans for predictable workloads, implementing Auto Scaling for dynamic workloads, choosing appropriate storage classes (S3 IA, Glacier), using Spot Instances for fault-tolerant workloads, implementing lifecycle policies for automated data management, monitoring costs with AWS Cost Explorer and Budgets, and using AWS Trusted Advisor for cost recommendations. Follow the AWS Well-Architected Cost Optimization pillar. Reference: https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'Right-sizing, Reserved Instances, Auto Scaling, appropriate storage classes, and cost monitoring', isCorrect: true },
                { text: 'Always use largest instance types for better performance and resource utilization', isCorrect: false },
                { text: 'Deploy all resources in single availability zone to reduce data transfer costs', isCorrect: false },
                { text: 'Use only on-demand pricing for maximum flexibility and cost predictability', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement monitoring and logging for AWS applications?',
            explanation: 'Comprehensive monitoring and logging: CloudWatch for metrics, alarms, and dashboards; CloudWatch Logs for centralized log management with log groups and streams; AWS X-Ray for distributed tracing and application insights; CloudTrail for API call auditing and compliance; AWS Config for resource configuration tracking; VPC Flow Logs for network traffic analysis; and third-party integrations with tools like Datadog or New Relic. Set up automated responses using CloudWatch Events/EventBridge and SNS notifications. Reference: https://docs.aws.amazon.com/cloudwatch/latest/monitoring/WhatIsCloudWatch.html',
            points: 1,
            answers: {
              create: [
                { text: 'CloudWatch for metrics/alarms, CloudWatch Logs, X-Ray for tracing, CloudTrail for auditing', isCorrect: true },
                { text: 'Only application-level logging using custom logging frameworks and file systems', isCorrect: false },
                { text: 'Manual log collection and analysis using EC2 instances with custom scripts', isCorrect: false },
                { text: 'Third-party monitoring tools only without using any AWS native services', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the different deployment strategies for applications on AWS?',
            explanation: 'AWS deployment strategies: Blue/Green - maintain two identical environments, switch traffic instantly with zero downtime using Route 53 or ALB; Rolling deployment - gradually update instances in Auto Scaling Group; Canary deployment - route small percentage of traffic to new version using ALB weighted routing; Immutable deployment - create new instances with updated code, terminate old ones; In-place deployment - update existing instances directly. Use AWS CodeDeploy for automated deployments, Elastic Beanstalk for application deployments, or container services like ECS/EKS. Reference: https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'Blue/Green, Rolling, Canary, Immutable, and In-place strategies with varying risk and downtime', isCorrect: true },
                { text: 'Only manual deployment processes with direct server access and file copying', isCorrect: false },
                { text: 'Single deployment strategy using infrastructure as code templates only', isCorrect: false },
                { text: 'Container-only deployment strategies without traditional server deployments', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement caching strategies in AWS architecture?',
            explanation: 'AWS caching strategies: CloudFront for edge caching of static and dynamic content globally; ElastiCache with Redis (data structures, persistence, clustering) or Memcached (simple key-value) for in-memory caching; Application-level caching using ElastiCache; Database query result caching; API Gateway caching for REST APIs; S3 Transfer Acceleration for upload optimization; and DAX (DynamoDB Accelerator) for microsecond latency. Choose caching layers based on access patterns, latency requirements, and cost considerations. Reference: https://docs.aws.amazon.com/elasticache/latest/red-ug/Replication.Redis.Groups.html',
            points: 1,
            answers: {
              create: [
                { text: 'CloudFront for edge caching, ElastiCache for in-memory caching, API Gateway caching, and DAX for DynamoDB', isCorrect: true },
                { text: 'Only application-level caching using local file systems and memory stores', isCorrect: false },
                { text: 'Database-only caching using read replicas and query optimization techniques', isCorrect: false },
                { text: 'CDN-only caching strategy without any application or database level caching', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the security best practices for AWS Solutions Architect Associate level?',
            explanation: 'Security best practices: Implement least privilege access using IAM policies, roles, and groups; enable MFA for all users; use AWS Organizations for account management; encrypt data at rest and in transit; implement network segmentation using VPCs, subnets, and security groups; enable CloudTrail for auditing; use AWS Config for compliance monitoring; implement AWS GuardDuty for threat detection; use AWS Secrets Manager for credential management; enable VPC Flow Logs; and follow shared responsibility model. Regular security reviews and AWS Security Hub for centralized findings. Reference: https://docs.aws.amazon.com/security/',
            points: 1,
            answers: {
              create: [
                { text: 'IAM least privilege, MFA, encryption, network segmentation, CloudTrail auditing, and threat detection', isCorrect: true },
                { text: 'Only perimeter security using firewalls and intrusion detection systems', isCorrect: false },
                { text: 'Application-level security only without infrastructure security considerations', isCorrect: false },
                { text: 'Default security settings with minimal configuration changes required', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you design for scalability and performance optimization in AWS?',
            explanation: 'Scalability and performance design: Horizontal scaling using Auto Scaling Groups and load balancers; vertical scaling for compute-intensive workloads; database read replicas and connection pooling; content delivery using CloudFront; asynchronous processing with SQS/SNS; microservices architecture with API Gateway; containerization using ECS/EKS; serverless computing with Lambda; caching at multiple layers; and performance monitoring with CloudWatch and X-Ray. Design for stateless applications and use managed services for better scalability. Reference: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'Auto Scaling, load balancers, read replicas, CDN, asynchronous processing, and microservices architecture', isCorrect: true },
                { text: 'Single large instance with maximum CPU and memory configuration', isCorrect: false },
                { text: 'Vertical scaling only with periodic manual capacity planning', isCorrect: false },
                { text: 'Monolithic architecture with shared database and synchronous processing', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the different data migration strategies and services available in AWS?',
            explanation: 'AWS data migration strategies and services: AWS Database Migration Service (DMS) for database migrations with minimal downtime; AWS Snow family (Snowball, Snowball Edge, Snowmobile) for large-scale data transfer; AWS DataSync for online data transfer to S3, EFS, or FSx; AWS Storage Gateway for hybrid cloud storage; AWS Direct Connect for dedicated network connections; AWS Migration Hub for tracking migration progress; AWS Application Discovery Service for inventory; and AWS Server Migration Service for VM migrations. Choose based on data volume, network bandwidth, and migration timeline. Reference: https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'DMS for databases, Snow family for large data, DataSync for online transfer, Storage Gateway for hybrid', isCorrect: true },
                { text: 'Only manual data export and import processes using standard database tools', isCorrect: false },
                { text: 'FTP and SFTP based transfers for all types of data migration requirements', isCorrect: false },
                { text: 'Application-level data synchronization without using AWS migration services', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement event-driven architecture using AWS services?',
            explanation: 'Event-driven architecture with AWS: Amazon EventBridge (CloudWatch Events) for routing events between services; SNS for pub/sub messaging and fan-out patterns; SQS for reliable message queuing and decoupling; Lambda for event processing; Step Functions for workflow orchestration; Kinesis for real-time data streaming; API Gateway for RESTful event APIs; and S3 event notifications. Design patterns include producer-consumer, publish-subscribe, and event sourcing. Implement dead letter queues for error handling and retry mechanisms. Reference: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html',
            points: 1,
            answers: {
              create: [
                { text: 'EventBridge for event routing, SNS/SQS for messaging, Lambda for processing, Step Functions for workflows', isCorrect: true },
                { text: 'Direct API calls between services without any event-driven components', isCorrect: false },
                { text: 'Database triggers and stored procedures for all event processing logic', isCorrect: false },
                { text: 'Cron jobs and scheduled tasks for reactive event-driven processing', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the considerations for multi-region architecture design?',
            explanation: 'Multi-region architecture considerations: Data replication using RDS cross-region replicas, S3 cross-region replication; DNS failover with Route 53 health checks; Global load balancing using CloudFront or Global Accelerator; Cross-region VPC peering or Transit Gateway for network connectivity; Regional service availability and compliance requirements; Data sovereignty and latency considerations; Cost implications of data transfer; Disaster recovery and business continuity planning; and consistent deployment using CloudFormation StackSets. Consider read-heavy vs write-heavy workloads for data consistency. Reference: https://docs.aws.amazon.com/whitepapers/latest/building-fault-tolerant-applications/building-fault-tolerant-applications.pdf',
            points: 1,
            answers: {
              create: [
                { text: 'Data replication, DNS failover, global load balancing, compliance, latency, and cost considerations', isCorrect: true },
                { text: 'Single region deployment with multiple availability zones for redundancy', isCorrect: false },
                { text: 'Manual failover processes with operator intervention for region switching', isCorrect: false },
                { text: 'Identical resource configuration in all regions without optimization', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  console.log(`✅ Seeded AWS Solutions Architect Associate certification with comprehensive questions`)
  return awsSolutionsArchitectAssociate
}
