import { PrismaClient } from '../../../src/generated/prisma'

export async function seedAwsDeveloperAssociate(prisma: PrismaClient, categoryId: number) {
  // AWS Developer Associate Certification
  const awsDeveloperAssociate = await prisma.certification.create({
    data: {
      name: 'AWS Certified Developer – Associate',
      description: 'Develop and maintain applications on the AWS platform with focus on deployment, security, development best practices, and troubleshooting. This certification validates expertise in developing, deploying, and debugging cloud-based applications using AWS services.',
      slug: 'aws-developer-associate',
      level: 'Associate',
      duration: 130,
      questionsCount: 65,
      categoryId,
      questions: {
        create: [
          {
            text: 'Which AWS service is primarily used for application deployment and management with automatic scaling?',
            explanation: 'AWS Elastic Beanstalk is designed for easy application deployment and management. It handles the deployment details including capacity provisioning, load balancing, auto-scaling, and application health monitoring while you focus on your application code. Beanstalk supports Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker applications. You maintain full control over AWS resources and can access them at any time. Reference: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'AWS Elastic Beanstalk with automatic scaling and platform management', isCorrect: true },
                { text: 'AWS CodePipeline for continuous integration and deployment workflows only', isCorrect: false },
                { text: 'Amazon ECS for container orchestration without automatic scaling', isCorrect: false },
                { text: 'AWS Lambda for serverless functions with manual capacity management', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the best way to store user session data for a web application on AWS and ensure high availability?',
            explanation: 'Amazon DynamoDB provides fast, predictable performance and is ideal for storing user session data with automatic scaling. It offers single-digit millisecond latency, built-in security, and global replication capabilities. For session storage, DynamoDB provides: automatic scaling based on traffic, built-in high availability and durability, integration with AWS services, and consistent performance. Alternatively, ElastiCache (Redis) can be used for session storage with sub-millisecond latency. Reference: https://docs.aws.amazon.com/dynamodb/latest/developerguide/bp-session-management.html',
            points: 1,
            answers: {
              create: [
                { text: 'Amazon DynamoDB with automatic scaling and high availability', isCorrect: true },
                { text: 'Amazon S3 for simple object storage with versioning enabled', isCorrect: false },
                { text: 'Amazon RDS with read replicas for relational data storage', isCorrect: false },
                { text: 'Amazon EFS for shared file system across multiple instances', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement CI/CD pipelines using AWS developer tools?',
            explanation: 'AWS CI/CD pipeline implementation: AWS CodeCommit for Git repositories, CodeBuild for build and testing with buildspec.yml, CodeDeploy for automated deployments to EC2/Lambda/ECS, and CodePipeline for orchestrating the entire workflow. Additional tools include: CodeArtifact for artifact management, CodeGuru for code reviews and performance recommendations, X-Ray for application tracing, and CloudFormation for infrastructure as code. Integration with third-party tools like GitHub, Jenkins, and Docker is also supported. Reference: https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'CodeCommit, CodeBuild, CodeDeploy, and CodePipeline for complete CI/CD workflow', isCorrect: true },
                { text: 'Only Jenkins running on EC2 instances for build and deployment', isCorrect: false },
                { text: 'Manual deployment processes with direct file upload to servers', isCorrect: false },
                { text: 'GitHub Actions only without any AWS-native CI/CD services', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the different ways to handle application secrets and configuration in AWS?',
            explanation: 'AWS provides multiple services for secrets management: AWS Secrets Manager for automatic rotation of database credentials, API keys, and other secrets with fine-grained access control; AWS Systems Manager Parameter Store for configuration data and secrets with hierarchical organization and encryption; AWS KMS for encryption key management; Environment variables in Lambda, ECS, or Elastic Beanstalk; and IAM roles for temporary credentials. Best practices include never hardcoding secrets, using least privilege access, enabling automatic rotation, and auditing access with CloudTrail. Reference: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html',
            points: 1,
            answers: {
              create: [
                { text: 'Secrets Manager for credentials, Parameter Store for config, environment variables, and IAM roles', isCorrect: true },
                { text: 'Hard-coding secrets in application configuration files for simplicity', isCorrect: false },
                { text: 'Storing all secrets in S3 buckets with public read permissions', isCorrect: false },
                { text: 'Using only database storage for all application secrets and configuration', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement error handling and logging in AWS Lambda functions?',
            explanation: 'Lambda error handling and logging: Use try-catch blocks for synchronous invocations, implement dead letter queues (DLQ) for failed asynchronous invocations, configure retry attempts and maximum age of events, use CloudWatch Logs for automatic logging with log groups and streams, implement structured logging with JSON format, use AWS X-Ray for distributed tracing and performance insights, set up CloudWatch Alarms for error metrics, and implement custom error handling with proper HTTP status codes for API Gateway integration. Reference: https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html',
            points: 1,
            answers: {
              create: [
                { text: 'Try-catch blocks, dead letter queues, CloudWatch Logs, X-Ray tracing, and structured logging', isCorrect: true },
                { text: 'Only console.log statements for debugging without centralized logging', isCorrect: false },
                { text: 'File-based logging on local Lambda execution environment storage', isCorrect: false },
                { text: 'Email notifications only for all error conditions and exceptions', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the best practices for developing serverless applications with AWS Lambda?',
            explanation: 'Serverless development best practices: Keep functions small and focused on single responsibility, minimize cold starts by optimizing package size and using provisioned concurrency, implement proper error handling and retry logic, use environment variables for configuration, leverage AWS SDK efficiently with connection pooling, implement proper security with least privilege IAM roles, use layers for shared code and libraries, monitor with CloudWatch and X-Ray, implement proper testing strategies including unit and integration tests, and design for idempotency to handle duplicate invocations safely. Reference: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html',
            points: 1,
            answers: {
              create: [
                { text: 'Small functions, cold start optimization, proper error handling, security, monitoring, and idempotency', isCorrect: true },
                { text: 'Large monolithic functions handling multiple responsibilities for efficiency', isCorrect: false },
                { text: 'No error handling since Lambda automatically retries all failed executions', isCorrect: false },
                { text: 'Always use maximum memory allocation for optimal performance', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement authentication and authorization for AWS APIs?',
            explanation: 'API authentication and authorization: Amazon Cognito for user pools (authentication) and identity pools (authorization), API Gateway with built-in authorization including Cognito, Lambda authorizers (custom authorization logic), IAM authorization for AWS service integration, API keys for usage plans and throttling, OAuth 2.0/OpenID Connect integration, JWT token validation, and resource-based policies. Implement proper token refresh mechanisms, secure token storage, and follow OAuth 2.0 security best practices for web and mobile applications. Reference: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html',
            points: 1,
            answers: {
              create: [
                { text: 'Cognito for user management, API Gateway authorization, Lambda authorizers, and IAM policies', isCorrect: true },
                { text: 'Only basic authentication with username and password stored in database', isCorrect: false },
                { text: 'No authentication required for internal APIs and microservices', isCorrect: false },
                { text: 'API keys only without any user-based authentication or authorization', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the different deployment patterns for Lambda functions and their use cases?',
            explanation: 'Lambda deployment patterns: All-at-once deployment (default) - simple but risky, overwrites all traffic to new version instantly; Linear deployment - gradually shifts traffic over time (10% every minute); Canary deployment - shifts specific percentage to new version, monitors, then completes; Blue/green deployment using aliases and weighted routing; Rolling deployment with reserved concurrency; and immutable deployment creating new versions. Use AWS SAM or CodeDeploy for advanced deployment patterns. Monitor with CloudWatch metrics and rollback automatically on errors. Reference: https://docs.aws.amazon.com/lambda/latest/dg/lambda-rolling-deployments.html',
            points: 1,
            answers: {
              create: [
                { text: 'All-at-once, Linear, Canary, Blue/green deployment patterns with monitoring and rollback', isCorrect: true },
                { text: 'Only manual deployment by uploading ZIP files to Lambda console', isCorrect: false },
                { text: 'Single deployment strategy without any traffic shifting capabilities', isCorrect: false },
                { text: 'Database-driven deployment using stored procedures and triggers', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you optimize DynamoDB performance for application development?',
            explanation: 'DynamoDB performance optimization: Design efficient partition keys to distribute traffic evenly, use composite sort keys for flexible querying, implement Global Secondary Indexes (GSI) for alternative access patterns, use Local Secondary Indexes (LSI) for different sort orders, enable DynamoDB Accelerator (DAX) for microsecond latency, implement proper pagination with exclusive start key, use batch operations for multiple items, enable auto-scaling for capacity management, use on-demand billing for unpredictable workloads, and implement proper error handling with exponential backoff for throttling. Reference: https://docs.aws.amazon.com/dynamodb/latest/developerguide/best-practices.html',
            points: 1,
            answers: {
              create: [
                { text: 'Efficient partition keys, GSI/LSI, DAX caching, batch operations, auto-scaling, and error handling', isCorrect: true },
                { text: 'Single table design with all data stored in one partition for simplicity', isCorrect: false },
                { text: 'Always use strongly consistent reads for all application queries', isCorrect: false },
                { text: 'Maximum provisioned capacity settings for all tables regardless of usage', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the security considerations for developing applications on AWS?',
            explanation: 'AWS application security considerations: Implement least privilege access with IAM roles and policies, use temporary credentials instead of long-term access keys, encrypt data in transit (HTTPS/TLS) and at rest (KMS), validate and sanitize all input data, implement proper authentication and authorization, use VPC for network isolation, enable CloudTrail for audit logging, implement proper session management, use AWS WAF for web application protection, scan for vulnerabilities with Inspector, store secrets in Secrets Manager, and implement proper CORS policies for web applications. Reference: https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Best_Practices.pdf',
            points: 1,
            answers: {
              create: [
                { text: 'Least privilege IAM, encryption, input validation, VPC isolation, audit logging, and secret management', isCorrect: true },
                { text: 'Only perimeter security with firewalls without application-level security', isCorrect: false },
                { text: 'Hard-coded credentials in source code for development simplicity', isCorrect: false },
                { text: 'Public S3 buckets for all application data and configuration files', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement event-driven architecture using AWS services for application development?',
            explanation: 'Event-driven architecture implementation: Amazon SNS for publish-subscribe messaging and fan-out patterns, SQS for reliable queuing and decoupling services, EventBridge for routing events between services with rules and targets, Lambda for event processing, Kinesis for real-time streaming data, Step Functions for complex workflows and state machines, S3 event notifications for object changes, DynamoDB Streams for database changes, and API Gateway for HTTP-based events. Implement proper error handling, dead letter queues, and monitoring for all event-driven components. Reference: https://aws.amazon.com/event-driven-architecture/',
            points: 1,
            answers: {
              create: [
                { text: 'SNS for pub-sub, SQS for queuing, EventBridge for routing, Lambda for processing, Step Functions for workflows', isCorrect: true },
                { text: 'Direct REST API calls between all services without any asynchronous processing', isCorrect: false },
                { text: 'Polling-based architecture with scheduled Lambda functions checking for updates', isCorrect: false },
                { text: 'Database triggers and stored procedures for all event-driven processing', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the monitoring and debugging tools available for AWS application development?',
            explanation: 'AWS monitoring and debugging tools: CloudWatch for metrics, logs, and alarms with custom dashboards, X-Ray for distributed tracing and application insights, AWS Personal Health Dashboard for service health, CloudTrail for API call auditing, VPC Flow Logs for network traffic analysis, AWS Config for resource configuration tracking, Application Load Balancer access logs, Lambda execution logs and metrics, DynamoDB monitoring with CloudWatch metrics, and third-party integrations. Implement proper logging strategies with structured logging and correlation IDs for request tracking. Reference: https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html',
            points: 1,
            answers: {
              create: [
                { text: 'CloudWatch for metrics/logs, X-Ray for tracing, CloudTrail for auditing, structured logging with correlation IDs', isCorrect: true },
                { text: 'Only application-level logging without any AWS-native monitoring services', isCorrect: false },
                { text: 'Manual log file analysis on EC2 instances without centralized monitoring', isCorrect: false },
                { text: 'Third-party tools only without leveraging any AWS monitoring capabilities', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement caching strategies for AWS applications?',
            explanation: 'AWS application caching strategies: ElastiCache with Redis (advanced data structures, persistence, clustering) or Memcached (simple key-value caching), API Gateway caching for REST API responses, CloudFront for edge caching of static and dynamic content, DynamoDB Accelerator (DAX) for microsecond DynamoDB access, Application Load Balancer sticky sessions for session affinity, Lambda@Edge for compute at edge locations, and application-level caching with proper cache invalidation strategies. Consider cache-aside, write-through, and write-behind patterns based on use case. Reference: https://docs.aws.amazon.com/elasticache/latest/red-ug/Replication.Redis.Groups.html',
            points: 1,
            answers: {
              create: [
                { text: 'ElastiCache for in-memory, API Gateway caching, CloudFront for edge, DAX for DynamoDB, with proper invalidation', isCorrect: true },
                { text: 'Only database query result caching without any distributed caching mechanisms', isCorrect: false },
                { text: 'File-based caching on local server storage without any distributed solutions', isCorrect: false },
                { text: 'No caching implementation to ensure data consistency and freshness', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the best practices for API design and development using AWS API Gateway?',
            explanation: 'API Gateway best practices: Implement proper HTTP methods and status codes, use resource-based URL design with meaningful paths, implement input validation with request validators, enable throttling and usage plans for rate limiting, implement proper CORS configuration, use stages for environment management (dev/staging/prod), implement proper error handling with custom error responses, enable caching for appropriate endpoints, use custom domain names with SSL certificates, implement request/response transformations using mapping templates, enable detailed monitoring and logging, and implement proper security with authorization mechanisms. Reference: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html',
            points: 1,
            answers: {
              create: [
                { text: 'RESTful design, input validation, throttling, CORS, stages, error handling, caching, and security', isCorrect: true },
                { text: 'Single endpoint handling all operations with POST method only', isCorrect: false },
                { text: 'No input validation or error handling for development simplicity', isCorrect: false },
                { text: 'Public APIs without any authentication or rate limiting mechanisms', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you handle database migrations and schema changes in AWS RDS?',
            explanation: 'RDS migration and schema management: Use AWS Database Migration Service (DMS) for heterogeneous migrations, implement blue-green deployments for minimal downtime, use read replicas for testing migrations, implement proper backup strategies with automated backups and snapshots, use AWS Schema Conversion Tool (SCT) for engine conversions, implement gradual rollout with connection string updates, use parameter groups for configuration management, implement proper monitoring during migrations, use Multi-AZ deployments for high availability during changes, and implement rollback procedures with point-in-time recovery. Reference: https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'DMS for migrations, blue-green deployments, read replicas for testing, automated backups, and rollback procedures', isCorrect: true },
                { text: 'Direct schema changes on production database without any backup or testing', isCorrect: false },
                { text: 'Manual SQL script execution during business hours without downtime planning', isCorrect: false },
                { text: 'Application-level schema management without any database migration tools', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the container deployment options available in AWS for application development?',
            explanation: 'AWS container deployment options: Amazon ECS (Elastic Container Service) with EC2 or Fargate launch types for Docker containers, Amazon EKS (Elastic Kubernetes Service) for Kubernetes orchestration, AWS App Runner for containerized web applications with automatic scaling, Elastic Beanstalk with Docker platform for simple container deployments, Lambda container images for serverless containers up to 10GB, and Amazon ECR (Elastic Container Registry) for container image storage. Consider factors like orchestration needs, operational overhead, scaling requirements, and existing Kubernetes expertise. Reference: https://docs.aws.amazon.com/ecs/latest/developerguide/Welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'ECS with EC2/Fargate, EKS for Kubernetes, App Runner, Elastic Beanstalk, Lambda containers, and ECR', isCorrect: true },
                { text: 'Only Docker running directly on EC2 instances without orchestration', isCorrect: false },
                { text: 'Virtual machines only without any containerization support', isCorrect: false },
                { text: 'Third-party container platforms without any AWS-native services', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement testing strategies for AWS applications?',
            explanation: 'AWS application testing strategies: Unit testing for individual functions with local development tools like SAM Local, integration testing with temporary AWS resources using CloudFormation, end-to-end testing with staging environments, load testing using tools like Artillery or AWS Load Testing solution, security testing with AWS Inspector and third-party tools, infrastructure testing with tools like LocalStack for local AWS simulation, automated testing in CI/CD pipelines with CodeBuild, canary deployments for production testing, synthetic monitoring with CloudWatch Synthetics, and chaos engineering for resilience testing. Reference: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-automated-tests.html',
            points: 1,
            answers: {
              create: [
                { text: 'Unit, integration, end-to-end, load testing with staging environments, automated CI/CD testing, and monitoring', isCorrect: true },
                { text: 'Only manual testing in production environment without any automated testing', isCorrect: false },
                { text: 'No testing required since AWS services are inherently reliable', isCorrect: false },
                { text: 'Only unit testing without any integration or end-to-end testing strategies', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the cost optimization strategies for AWS application development?',
            explanation: 'Cost optimization for AWS applications: Right-size resources based on actual usage patterns, use Reserved Instances and Savings Plans for predictable workloads, implement auto-scaling to match demand, use Spot Instances for fault-tolerant workloads, optimize Lambda function memory allocation and execution time, implement efficient database queries and indexing, use appropriate storage classes for different data access patterns, implement lifecycle policies for automated data management, monitor costs with AWS Cost Explorer and Budgets, use AWS Compute Optimizer for rightsizing recommendations, and implement tagging strategies for cost allocation and tracking. Reference: https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'Right-sizing, Reserved Instances, auto-scaling, Spot Instances, Lambda optimization, and cost monitoring', isCorrect: true },
                { text: 'Always use maximum capacity settings to ensure optimal performance', isCorrect: false },
                { text: 'Deploy all resources in single availability zone to minimize data transfer costs', isCorrect: false },
                { text: 'Use only free tier services regardless of application requirements', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement data processing and analytics pipelines using AWS services?',
            explanation: 'AWS data processing and analytics: Amazon Kinesis for real-time streaming data ingestion and processing, AWS Glue for ETL jobs with serverless Apache Spark, Amazon EMR for big data processing with Hadoop ecosystem, AWS Step Functions for orchestrating data workflows, Lambda for event-driven data processing, S3 for data lake storage with partitioning strategies, Athena for serverless SQL queries, QuickSight for business intelligence and visualization, Redshift for data warehousing, and SageMaker for machine learning pipelines. Implement proper data governance, security, and monitoring throughout the pipeline. Reference: https://docs.aws.amazon.com/kinesis/latest/dev/introduction.html',
            points: 1,
            answers: {
              create: [
                { text: 'Kinesis for streaming, Glue for ETL, EMR for big data, Step Functions for orchestration, S3 for storage, Athena for queries', isCorrect: true },
                { text: 'Only relational databases for all data processing and analytics requirements', isCorrect: false },
                { text: 'Manual data processing using custom scripts on EC2 instances', isCorrect: false },
                { text: 'Single monolithic application handling all data processing operations', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  console.log(`✅ Seeded AWS Developer Associate certification with comprehensive questions`)
  return awsDeveloperAssociate
}
