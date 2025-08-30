import { PrismaClient } from '../../../src/generated/prisma'

export async function seedAwsSolutionsArchitectProfessional(prisma: PrismaClient, categoryId: number) {
  // AWS Solutions Architect Professional Certification
  const awsSolutionsArchitectProfessional = await prisma.certification.create({
    data: {
      name: 'AWS Certified Solutions Architect – Professional',
      description: 'Advanced AWS certification for experienced solutions architects covering complex multi-tier applications, hybrid architectures, migration strategies, cost optimization, and disaster recovery. This certification validates advanced technical skills and experience in designing distributed applications and systems on AWS.',
      slug: 'aws-solutions-architect-professional',
      level: 'Professional',
      duration: 180,
      questionsCount: 75,
      categoryId,
      questions: {
        create: [
          {
            text: 'How do you design a highly available and fault-tolerant multi-tier application architecture across multiple AWS regions?',
            explanation: 'Multi-region, multi-tier architecture design: Use Application Load Balancers in each region with health checks, Auto Scaling Groups across multiple AZs, RDS Multi-AZ with cross-region read replicas, S3 with cross-region replication, CloudFront for global content delivery, Route 53 with health checks for DNS failover, VPC peering or Transit Gateway for inter-region connectivity, AWS Config for compliance across regions, CloudTrail for audit logging, and disaster recovery automation with AWS Backup and CloudFormation StackSets. Implement database sharding, caching layers with ElastiCache clusters, and event-driven architecture with SQS/SNS for loose coupling. Reference: https://docs.aws.amazon.com/whitepapers/latest/building-fault-tolerant-applications/building-fault-tolerant-applications.pdf',
            points: 2,
            answers: {
              create: [
                { text: 'Multi-region ALB, Auto Scaling across AZs, RDS Multi-AZ with read replicas, S3 replication, Route 53 failover', isCorrect: true },
                { text: 'Single region deployment with multiple availability zones for cost optimization', isCorrect: false },
                { text: 'Multi-region but single AZ deployment for simplified network configuration', isCorrect: false },
                { text: 'Manual failover processes between regions without automated disaster recovery', isCorrect: false },
              ],
            },
          },
          {
            text: 'Design a cost-optimized data lake architecture for petabyte-scale analytics workloads with varying access patterns.',
            explanation: 'Cost-optimized data lake architecture: Use S3 with multiple storage classes (Standard for frequent access, IA for infrequent, Glacier for archival), implement intelligent tiering for automatic cost optimization, use S3 lifecycle policies for automated data management, implement data partitioning strategies in S3, use AWS Glue for serverless ETL with job bookmarks, implement Amazon EMR with Spot Instances for batch processing, use Amazon Athena for serverless queries with result caching, implement data catalog with AWS Glue Data Catalog, use Amazon QuickSight for visualization with SPICE caching, implement data compression and columnar formats (Parquet), use CloudFront for analytics dashboard delivery, and implement proper data governance with Lake Formation. Reference: https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/building-data-lake-aws.html',
            points: 2,
            answers: {
              create: [
                { text: 'S3 with multiple storage classes, Glue ETL, EMR with Spot, Athena, QuickSight, Lake Formation governance', isCorrect: true },
                { text: 'Single S3 Standard storage class for all data with manual lifecycle management', isCorrect: false },
                { text: 'Traditional data warehouse using only Amazon Redshift for all analytics workloads', isCorrect: false },
                { text: 'On-premises Hadoop cluster with AWS Direct Connect for hybrid architecture', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement a zero-downtime migration strategy for a legacy monolithic application to microservices on AWS?',
            explanation: 'Zero-downtime microservices migration: Implement strangler fig pattern with API Gateway routing traffic between legacy and new services, use blue-green deployment with Application Load Balancer weighted routing, implement database decomposition with AWS DMS for data migration, use AWS App2Container or containerize manually with ECS/EKS, implement event-driven communication with EventBridge and SQS, use AWS X-Ray for distributed tracing during migration, implement circuit breakers and bulkheads for resilience, use feature flags with AWS AppConfig for gradual rollout, implement comprehensive monitoring with CloudWatch and third-party tools, use AWS CodePipeline for automated deployments, and maintain backward compatibility during transition phase. Reference: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-phased-approach/welcome.html',
            points: 2,
            answers: {
              create: [
                { text: 'Strangler fig pattern, blue-green deployment, database decomposition, containerization, event-driven architecture', isCorrect: true },
                { text: 'Big bang migration with complete system replacement over weekend maintenance', isCorrect: false },
                { text: 'Lift-and-shift to EC2 instances without any architectural changes', isCorrect: false },
                { text: 'Parallel development with separate infrastructure and data cutover', isCorrect: false },
              ],
            },
          },
          {
            text: 'Design a hybrid cloud architecture for regulatory compliance with on-premises data residency requirements.',
            explanation: 'Hybrid cloud compliance architecture: Use AWS Outposts for on-premises AWS services with local data processing, implement AWS Direct Connect with dedicated connections for consistent performance, use AWS Storage Gateway for hybrid storage integration, implement AWS Systems Manager for unified management, use AWS PrivateLink for secure service access, implement data classification with Amazon Macie and on-premises tools, use AWS Config and AWS Security Hub for compliance monitoring, implement encryption in transit and at rest with AWS KMS and on-premises HSM integration, use AWS Single Sign-On for federated access, implement network segmentation with AWS Transit Gateway and on-premises VPN, use AWS Control Tower for governance, and maintain audit trails with CloudTrail and on-premises SIEM integration. Reference: https://docs.aws.amazon.com/whitepapers/latest/aws-microsoft-workloads/hybrid-cloud-integration-patterns.html',
            points: 2,
            answers: {
              create: [
                { text: 'AWS Outposts, Direct Connect, Storage Gateway, data classification, encryption, federated access, governance', isCorrect: true },
                { text: 'Public cloud only solution with data replication to meet compliance requirements', isCorrect: false },
                { text: 'On-premises only deployment without any cloud integration or benefits', isCorrect: false },
                { text: 'Simple VPN connectivity without any specialized hybrid cloud services', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you design a globally distributed, low-latency gaming architecture with real-time multiplayer capabilities?',
            explanation: 'Global gaming architecture: Use Amazon GameLift for dedicated game server hosting across regions, implement AWS Global Accelerator for improved connection performance, use CloudFront with Lambda@Edge for game asset delivery, implement Amazon ElastiCache for game state caching, use Amazon DynamoDB Global Tables for player data synchronization, implement Amazon Kinesis for real-time analytics and leaderboards, use Amazon Cognito for player authentication and management, implement AWS AppSync for real-time multiplayer synchronization, use Amazon SQS/SNS for event processing, implement Amazon S3 with Transfer Acceleration for game assets, use Route 53 with latency-based routing, and implement monitoring with CloudWatch and custom metrics for game performance. Reference: https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-intro.html',
            points: 2,
            answers: {
              create: [
                { text: 'GameLift for servers, Global Accelerator, CloudFront, ElastiCache, DynamoDB Global Tables, real-time sync', isCorrect: true },
                { text: 'Single region deployment with CDN for global content delivery only', isCorrect: false },
                { text: 'Traditional web application architecture without gaming-specific optimizations', isCorrect: false },
                { text: 'On-premises game servers with basic cloud storage for game assets', isCorrect: false },
              ],
            },
          },
          {
            text: 'Design a disaster recovery strategy for mission-critical applications with RTO of 1 hour and RPO of 15 minutes.',
            explanation: 'Mission-critical disaster recovery: Implement warm standby architecture with reduced capacity in secondary region, use RDS Multi-AZ with cross-region automated backups and read replicas, implement S3 cross-region replication with versioning, use AWS Backup for automated backup orchestration, implement Route 53 health checks with automatic failover, use AWS Site Recovery or CloudEndure for server replication, implement database transaction log shipping or streaming replication, use AWS Systems Manager for automated recovery procedures, implement monitoring and alerting with CloudWatch and SNS, use AWS CodePipeline for automated infrastructure deployment, implement data validation and integrity checks, and maintain regular DR testing and documentation. RTO of 1 hour requires automated failover processes and pre-provisioned infrastructure. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html',
            points: 2,
            answers: {
              create: [
                { text: 'Warm standby with automated failover, cross-region replication, automated backups, health checks, recovery automation', isCorrect: true },
                { text: 'Cold backup strategy with manual recovery processes and basic data backups', isCorrect: false },
                { text: 'Multi-site active-active for all applications regardless of cost considerations', isCorrect: false },
                { text: 'Backup and restore strategy only without any standby infrastructure', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement a secure, compliant, and cost-effective data warehousing solution for GDPR and HIPAA requirements?',
            explanation: 'Compliant data warehousing solution: Use Amazon Redshift with encryption at rest and in transit, implement fine-grained access control with IAM and database users, use AWS PrivateLink for secure connectivity, implement data masking and tokenization for sensitive data, use AWS Glue with PII detection for ETL processes, implement audit logging with CloudTrail and Redshift audit logs, use AWS Config for compliance monitoring, implement data retention and deletion policies for GDPR compliance, use AWS KMS with customer-managed keys, implement network isolation with VPC and security groups, use AWS Secrets Manager for credential management, implement data lineage tracking, use AWS Macie for sensitive data discovery, and maintain documentation and regular compliance assessments. Reference: https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security.html',
            points: 2,
            answers: {
              create: [
                { text: 'Redshift with encryption, fine-grained access, data masking, audit logging, compliance monitoring, retention policies', isCorrect: true },
                { text: 'Basic Redshift deployment with default security settings and manual compliance checking', isCorrect: false },
                { text: 'On-premises data warehouse with cloud connectivity for cost reduction only', isCorrect: false },
                { text: 'Public cloud deployment without any specific compliance or security considerations', isCorrect: false },
              ],
            },
          },
          {
            text: 'Design a machine learning pipeline for real-time fraud detection with sub-second response times and continuous model improvement.',
            explanation: 'Real-time ML fraud detection pipeline: Use Amazon SageMaker for model development and training, implement Amazon Kinesis Data Streams for real-time data ingestion, use AWS Lambda for real-time inference with SageMaker endpoints, implement Amazon DynamoDB for feature store and low-latency lookups, use Amazon ElastiCache for caching frequent queries, implement Amazon Kinesis Analytics for stream processing, use Amazon S3 for model artifacts and training data storage, implement SageMaker Model Monitor for model drift detection, use SageMaker Pipelines for automated retraining, implement A/B testing with multi-variant endpoints, use Amazon EventBridge for event-driven model updates, implement proper monitoring with CloudWatch and custom metrics, use SageMaker Clarify for bias detection, and implement feedback loops for continuous learning. Reference: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html',
            points: 2,
            answers: {
              create: [
                { text: 'SageMaker endpoints, Kinesis streams, Lambda inference, DynamoDB feature store, continuous retraining pipeline', isCorrect: true },
                { text: 'Batch processing only with daily model updates and offline fraud detection', isCorrect: false },
                { text: 'Simple rule-based system without any machine learning capabilities', isCorrect: false },
                { text: 'Third-party fraud detection service without any custom ML implementation', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement a cost optimization strategy for a large enterprise with multiple AWS accounts and complex workloads?',
            explanation: 'Enterprise cost optimization strategy: Implement AWS Organizations with consolidated billing and volume discounts, use AWS Cost Explorer for detailed cost analysis and forecasting, implement Cost and Usage Reports with custom analysis, use AWS Budgets with automated actions for cost control, implement tagging strategy for cost allocation and chargeback, use AWS Compute Optimizer for rightsizing recommendations, implement Reserved Instance and Savings Plans optimization, use Spot Instances for appropriate workloads, implement automated resource scheduling for non-production environments, use AWS Trusted Advisor for cost recommendations, implement S3 storage optimization with lifecycle policies and storage classes, use AWS Well-Architected reviews for cost optimization pillar, implement showback and chargeback processes, and establish cost governance with AWS Control Tower and Service Control Policies. Reference: https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-pillar/cost-optimization-pillar.html',
            points: 2,
            answers: {
              create: [
                { text: 'Organizations billing, Cost Explorer, tagging strategy, rightsizing, Reserved Instances, automation, governance', isCorrect: true },
                { text: 'Manual cost tracking using spreadsheets without any AWS cost management tools', isCorrect: false },
                { text: 'Single account deployment to avoid complexity of cost allocation across accounts', isCorrect: false },
                { text: 'Always use largest instance types to avoid performance issues regardless of cost', isCorrect: false },
              ],
            },
          },
          {
            text: 'Design a serverless event-driven architecture for processing millions of IoT device messages with real-time analytics and alerting.',
            explanation: 'Serverless IoT processing architecture: Use AWS IoT Core for device connectivity with device shadows and rules engine, implement Amazon Kinesis Data Firehose for data delivery to S3, use AWS Lambda for real-time processing triggered by Kinesis, implement Amazon DynamoDB for device state and time-series data storage, use Amazon Timestream for optimized time-series analytics, implement Amazon SNS for real-time alerting and notifications, use AWS Step Functions for complex workflows, implement Amazon ElastiCache for caching frequently accessed data, use Amazon Athena for ad-hoc analytics on S3 data, implement AWS Glue for ETL processing, use Amazon QuickSight for dashboards, implement proper error handling with dead letter queues, use AWS X-Ray for distributed tracing, and implement auto-scaling based on message volume. Reference: https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html',
            points: 2,
            answers: {
              create: [
                { text: 'IoT Core, Kinesis Firehose, Lambda processing, DynamoDB/Timestream, SNS alerting, Step Functions workflows', isCorrect: true },
                { text: 'Traditional server-based architecture with EC2 instances for message processing', isCorrect: false },
                { text: 'Simple database storage without any real-time processing or analytics capabilities', isCorrect: false },
                { text: 'Batch processing only with daily analytics reports without real-time capabilities', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you design a multi-cloud strategy with AWS as primary cloud and seamless failover capabilities?',
            explanation: 'Multi-cloud strategy with AWS primary: Implement container-based applications using Kubernetes for portability across clouds, use Terraform or Pulumi for infrastructure as code across multiple providers, implement API Gateway with backend service abstraction, use message queuing systems compatible across clouds (Apache Kafka), implement database replication between cloud providers, use DNS-based failover with health checks, implement monitoring and alerting across all clouds, use secrets management compatible across providers, implement consistent security policies and compliance, use cloud-agnostic CI/CD pipelines, implement data synchronization strategies, maintain application architecture that minimizes cloud-specific services, implement network connectivity between clouds, and establish governance and cost management across providers. Reference: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-with-aws/hybrid-cloud-with-aws.html',
            points: 2,
            answers: {
              create: [
                { text: 'Kubernetes containers, IaC tools, API abstraction, cross-cloud replication, DNS failover, unified monitoring', isCorrect: true },
                { text: 'AWS-only deployment with vendor lock-in and no multi-cloud considerations', isCorrect: false },
                { text: 'Separate applications deployed independently on each cloud without integration', isCorrect: false },
                { text: 'Manual failover processes between clouds without any automation', isCorrect: false },
              ],
            },
          },
          {
            text: 'Design a secure and scalable content delivery architecture for a global streaming video platform.',
            explanation: 'Global video streaming architecture: Use Amazon CloudFront with multiple origins and origin failover, implement AWS Elemental MediaStore for scalable video storage, use AWS Elemental MediaConvert for video transcoding to multiple formats and qualities, implement adaptive bitrate streaming with HLS/DASH protocols, use AWS Elemental MediaPackage for video packaging and origin services, implement DRM with AWS Elemental MediaPackage and third-party solutions, use Amazon S3 with Transfer Acceleration for content upload, implement Lambda@Edge for personalization and A/B testing, use AWS WAF for DDoS protection and geo-blocking, implement user authentication with Amazon Cognito, use CloudWatch and X-Ray for monitoring and analytics, implement content recommendation engine with Amazon Personalize, use Amazon ElastiCache for metadata caching, and implement cost optimization with storage classes and CDN optimization. Reference: https://docs.aws.amazon.com/media-services/',
            points: 2,
            answers: {
              create: [
                { text: 'CloudFront CDN, Elemental Media Services, adaptive streaming, DRM, Lambda@Edge, authentication, monitoring', isCorrect: true },
                { text: 'Simple S3 static website hosting with basic CloudFront distribution', isCorrect: false },
                { text: 'Traditional web servers with basic video file serving without streaming optimization', isCorrect: false },
                { text: 'Third-party CDN service without any AWS media services integration', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement a comprehensive backup and restore strategy for complex multi-tier applications with various RPO/RTO requirements?',
            explanation: 'Comprehensive backup and restore strategy: Use AWS Backup for centralized backup management across services, implement cross-region backup replication for disaster recovery, use EBS snapshots with lifecycle management, implement RDS automated backups with point-in-time recovery, use S3 versioning and MFA delete for critical data, implement application-consistent backups using AWS Systems Manager, use AWS Storage Gateway for hybrid backup scenarios, implement backup encryption with AWS KMS, use AWS DataSync for data transfer and synchronization, implement backup testing and validation procedures, use AWS Lambda for custom backup workflows, implement monitoring and alerting for backup failures, use AWS Config for backup compliance monitoring, establish different backup tiers for different RPO/RTO requirements, and maintain backup documentation and recovery procedures. Reference: https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html',
            points: 2,
            answers: {
              create: [
                { text: 'AWS Backup centralized management, cross-region replication, automated testing, different tiers for RPO/RTO', isCorrect: true },
                { text: 'Manual backup processes using individual service backup features without coordination', isCorrect: false },
                { text: 'Single backup strategy for all applications regardless of criticality or requirements', isCorrect: false },
                { text: 'Backup storage only without any restore testing or validation procedures', isCorrect: false },
              ],
            },
          },
          {
            text: 'Design a microservices architecture pattern for handling distributed transactions across multiple services with eventual consistency.',
            explanation: 'Distributed transaction microservices pattern: Implement Saga pattern using AWS Step Functions for orchestration or event-driven choreography, use Amazon EventBridge for event routing between services, implement compensating actions for transaction rollback, use Amazon SQS for reliable message delivery with dead letter queues, implement idempotent operations for safe retries, use Amazon DynamoDB with conditional writes for consistency, implement event sourcing pattern for audit trails, use AWS X-Ray for distributed tracing, implement circuit breaker pattern with AWS App Mesh, use Amazon SNS for event fan-out patterns, implement proper error handling and retry logic, use AWS Lambda for lightweight service implementation, implement monitoring and alerting for transaction failures, establish service contracts and API versioning, and implement comprehensive testing strategies including chaos engineering. Reference: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-workflows.html',
            points: 2,
            answers: {
              create: [
                { text: 'Saga pattern with Step Functions, EventBridge, compensating actions, idempotent operations, event sourcing', isCorrect: true },
                { text: 'Traditional distributed transactions with two-phase commit across microservices', isCorrect: false },
                { text: 'Single database shared across all microservices for transaction consistency', isCorrect: false },
                { text: 'Synchronous REST API calls without any asynchronous processing or compensation', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you design a data governance and compliance architecture for a financial services organization with strict regulatory requirements?',
            explanation: 'Financial services data governance architecture: Use AWS Lake Formation for centralized data governance and fine-grained access control, implement Amazon Macie for automated data discovery and classification, use AWS Config for continuous compliance monitoring, implement AWS CloudTrail for comprehensive audit logging, use AWS Secrets Manager for credential management, implement data lineage tracking with AWS Glue Data Catalog, use Amazon S3 with bucket policies and access logging, implement encryption at rest and in transit with AWS KMS, use AWS PrivateLink for secure service connectivity, implement AWS Organizations with Service Control Policies, use AWS Security Hub for centralized security findings, implement data retention and deletion policies, use AWS Artifact for compliance documentation, establish data classification policies, implement regular compliance assessments, and maintain detailed documentation and procedures. Reference: https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html',
            points: 2,
            answers: {
              create: [
                { text: 'Lake Formation governance, Macie classification, Config compliance, comprehensive auditing, encryption, data lineage', isCorrect: true },
                { text: 'Basic access controls without any automated governance or compliance monitoring', isCorrect: false },
                { text: 'Manual compliance processes without any AWS governance services integration', isCorrect: false },
                { text: 'Public cloud deployment without any specific financial services compliance considerations', isCorrect: false },
              ],
            },
          },
          {
            text: 'Design a high-performance computing (HPC) architecture for scientific workloads requiring massive parallel processing and low-latency interconnects.',
            explanation: 'AWS HPC architecture for scientific workloads: Use Amazon EC2 with cluster placement groups and enhanced networking, implement AWS ParallelCluster for HPC cluster management, use EC2 instances optimized for compute (C5n, C6gn) with up to 100 Gbps networking, implement Elastic Fabric Adapter (EFA) for low-latency HPC applications, use Amazon FSx for Lustre for high-performance shared storage, implement AWS Batch for job scheduling and queue management, use Spot Instances for cost optimization of batch workloads, implement auto-scaling based on workload demand, use AWS Storage Gateway for hybrid storage scenarios, implement monitoring with CloudWatch and HPC-specific metrics, use AWS Direct Connect for high-bandwidth data transfer, implement data preprocessing with AWS Glue or EMR, use Amazon S3 for results storage and archival, and implement proper security and compliance for scientific data. Reference: https://docs.aws.amazon.com/parallelcluster/latest/ug/what-is-aws-parallelcluster.html',
            points: 2,
            answers: {
              create: [
                { text: 'ParallelCluster, cluster placement groups, EFA networking, FSx Lustre, Batch scheduling, Spot Instances', isCorrect: true },
                { text: 'Basic EC2 instances without any HPC-specific optimizations or configurations', isCorrect: false },
                { text: 'On-premises HPC cluster with basic cloud storage connectivity only', isCorrect: false },
                { text: 'Serverless computing architecture without any dedicated HPC infrastructure', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement a comprehensive monitoring, logging, and observability strategy for complex distributed systems?',
            explanation: 'Comprehensive observability strategy: Use AWS X-Ray for distributed tracing across microservices, implement centralized logging with CloudWatch Logs and log aggregation, use CloudWatch Metrics with custom metrics and dimensions, implement synthetic monitoring with CloudWatch Synthetics, use AWS Health Dashboard for service health monitoring, implement application performance monitoring (APM) with third-party tools, use VPC Flow Logs for network monitoring, implement security monitoring with GuardDuty and Security Hub, use AWS Config for configuration drift monitoring, implement cost monitoring with Cost Explorer and Budgets, use CloudWatch Alarms with automated responses, implement log analysis with CloudWatch Insights and Elasticsearch, use CloudWatch Dashboards for visualization, implement SLI/SLO monitoring with proper alerting, establish on-call procedures and runbooks, and implement chaos engineering for resilience testing. Reference: https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html',
            points: 2,
            answers: {
              create: [
                { text: 'X-Ray tracing, centralized logging, custom metrics, synthetic monitoring, APM tools, automated alerting', isCorrect: true },
                { text: 'Basic CloudWatch metrics without any custom monitoring or distributed tracing', isCorrect: false },
                { text: 'Application-level logging only without any infrastructure or service monitoring', isCorrect: false },
                { text: 'Manual monitoring processes without any automated alerting or response capabilities', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  console.log(`✅ Seeded AWS Solutions Architect Professional certification with comprehensive questions`)
  return awsSolutionsArchitectProfessional
}
