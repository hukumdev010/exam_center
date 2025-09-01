import { PrismaClient } from '../../../src/generated/prisma'

export async function seedAwsSecuritySpecialty(prisma: PrismaClient, categoryId: number) {
  // AWS Security Specialty Certification
  const awsSecuritySpecialty = await prisma.certification.create({
    data: {
      name: 'AWS Certified Security – Specialty',
      description: 'Advanced AWS security certification covering incident response, logging and monitoring, infrastructure security, identity and access management, and data protection. This certification validates advanced technical skills and experience in securing AWS platforms and applications.',
      slug: 'aws-security-specialty',
      level: 'Specialty',
      duration: 170,
      questionsCount: 65,
      categoryId,
      questions: {
        create: [
          {
            text: 'Which service provides centralized logging for security events across AWS services and how should it be configured?',
            explanation: 'AWS CloudTrail provides logging of API calls and events across AWS services, essential for security auditing and compliance. Best practices include: enabling CloudTrail in all regions, using multiple trails for separation of duties, enabling log file integrity validation, storing logs in dedicated S3 buckets with MFA delete, encrypting logs with KMS, setting up CloudWatch Events for real-time notifications, implementing log analysis with CloudWatch Insights or third-party SIEM tools, and configuring proper retention policies. CloudTrail captures API calls made through AWS Management Console, SDKs, CLI, and other AWS services. Reference: https://docs.aws.amazon.com/cloudtrail/latest/userguide/cloudtrail-user-guide.html',
            points: 1,
            answers: {
              create: [
                { text: 'AWS CloudTrail with multi-region trails, log integrity validation, KMS encryption, and S3 storage', isCorrect: true },
                { text: 'Amazon CloudWatch Logs with basic log aggregation and local storage only', isCorrect: false },
                { text: 'AWS Config for configuration changes without API call logging capabilities', isCorrect: false },
                { text: 'Amazon GuardDuty for threat detection without centralized logging functionality', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the best practice for managing secrets in AWS applications and why?',
            explanation: 'AWS Secrets Manager provides secure storage and automatic rotation of secrets like passwords, API keys, and database credentials. Best practices include: using Secrets Manager for automatic rotation with supported services (RDS, Redshift, DocumentDB), implementing fine-grained access control with IAM policies, enabling encryption at rest and in transit, using resource-based policies for cross-account access, implementing least privilege access, monitoring access with CloudTrail, using SDK integration for automatic credential retrieval, and implementing proper error handling for secret retrieval failures. Never store secrets in code, environment variables, or configuration files. Reference: https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html',
            points: 1,
            answers: {
              create: [
                { text: 'AWS Secrets Manager with automatic rotation, IAM policies, encryption, and SDK integration', isCorrect: true },
                { text: 'Amazon S3 with client-side encryption and public bucket access for simplicity', isCorrect: false },
                { text: 'AWS Systems Manager Parameter Store without encryption for better performance', isCorrect: false },
                { text: 'Hard-coding secrets in application source code for faster development', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement defense-in-depth security for VPC network architecture?',
            explanation: 'Defense-in-depth VPC security implementation: Network ACLs at subnet level for stateless filtering (allow/deny rules), Security Groups at instance level for stateful filtering (allow rules only), VPC Flow Logs for network traffic monitoring and analysis, AWS WAF for application layer protection, AWS Shield for DDoS protection, PrivateLink for private connectivity to AWS services, VPC endpoints to avoid internet routing, bastion hosts or Session Manager for secure access, network segmentation with multiple subnets, and AWS Network Firewall for advanced inspection. Implement principle of least privilege and regular security assessments. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html',
            points: 1,
            answers: {
              create: [
                { text: 'NACLs, Security Groups, VPC Flow Logs, WAF, Shield, PrivateLink, network segmentation, and monitoring', isCorrect: true },
                { text: 'Only Security Groups with default allow-all rules for development simplicity', isCorrect: false },
                { text: 'Single subnet design with all resources in public subnet for easy management', isCorrect: false },
                { text: 'Perimeter security only without any internal network segmentation or monitoring', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the key components of AWS identity and access management (IAM) security best practices?',
            explanation: 'IAM security best practices: Implement principle of least privilege with minimal necessary permissions, use IAM roles instead of long-term access keys, enable MFA for all users and privileged operations, implement strong password policies and regular rotation, use IAM groups for permission management, implement cross-account access with roles and external IDs, enable CloudTrail for IAM activity monitoring, regularly review and audit permissions with Access Analyzer, implement permission boundaries for developer access, use service-linked roles for AWS services, implement just-in-time access for privileged operations, and use temporary credentials with STS. Never share credentials or embed them in code. Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html',
            points: 1,
            answers: {
              create: [
                { text: 'Least privilege, IAM roles, MFA, strong passwords, groups, regular auditing, temporary credentials', isCorrect: true },
                { text: 'Single admin user with full access permissions for all AWS operations', isCorrect: false },
                { text: 'Shared credentials across team members for collaboration efficiency', isCorrect: false },
                { text: 'Long-term access keys stored in application configuration files', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement encryption at rest and in transit for AWS services?',
            explanation: 'AWS encryption implementation: At rest - S3 with SSE-S3/SSE-KMS/SSE-C, EBS encryption with KMS keys, RDS encryption for databases, DynamoDB encryption, Redshift encryption, and EFS encryption. In transit - HTTPS/TLS for web traffic, VPC endpoints for private connections, SSL/TLS for database connections, AWS Certificate Manager for SSL certificates, and VPN/Direct Connect with encryption. Use AWS KMS for centralized key management with customer-managed keys (CMK), enable automatic key rotation, implement cross-region key replication, use envelope encryption for large datasets, and audit key usage with CloudTrail. Reference: https://docs.aws.amazon.com/kms/latest/developerguide/overview.html',
            points: 1,
            answers: {
              create: [
                { text: 'KMS for key management, service-native encryption, SSL/TLS for transit, Certificate Manager for certificates', isCorrect: true },
                { text: 'Client-side encryption only without any AWS-managed encryption services', isCorrect: false },
                { text: 'No encryption required since AWS provides inherent security for all services', isCorrect: false },
                { text: 'Manual key management using self-generated keys stored in application code', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Amazon GuardDuty and how does it enhance AWS security monitoring?',
            explanation: 'Amazon GuardDuty is a threat detection service that uses machine learning, anomaly detection, and integrated threat intelligence to identify malicious activity and unauthorized behavior. Key features include: continuous monitoring of VPC Flow Logs, CloudTrail events, and DNS logs; threat intelligence feeds from AWS Security, CrowdStrike, and Proofpoint; machine learning models for behavioral analysis; automated threat detection for compromised instances, cryptocurrency mining, reconnaissance attacks, and data exfiltration; integration with Security Hub for centralized findings; custom threat lists and suppression rules; multi-account support through AWS Organizations. GuardDuty provides actionable security findings with severity levels and remediation guidance. Reference: https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html',
            points: 1,
            answers: {
              create: [
                { text: 'ML-powered threat detection service analyzing VPC Flow Logs, CloudTrail, DNS logs with threat intelligence', isCorrect: true },
                { text: 'Network firewall service for blocking malicious traffic at VPC boundaries', isCorrect: false },
                { text: 'Vulnerability scanning service for EC2 instances and container images only', isCorrect: false },
                { text: 'Compliance auditing service for regulatory requirement validation', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement secure CI/CD pipelines using AWS security services?',
            explanation: 'Secure CI/CD pipeline implementation: Use IAM roles for service authentication, implement least privilege access for pipeline stages, store secrets in Secrets Manager or Parameter Store, enable code signing with AWS Signer, implement security testing with CodeGuru and third-party tools, use private VPC endpoints for service communication, implement artifact scanning with Inspector or ECR vulnerability scanning, enable detailed logging and monitoring with CloudTrail and CloudWatch, implement approval workflows for production deployments, use separate AWS accounts for different environments, implement infrastructure as code security scanning, and enable automated security testing in build processes. Reference: https://docs.aws.amazon.com/codepipeline/latest/userguide/security-best-practices.html',
            points: 1,
            answers: {
              create: [
                { text: 'IAM roles, secure secret storage, code signing, security testing, private endpoints, artifact scanning', isCorrect: true },
                { text: 'Shared credentials for all pipeline stages with full administrative access', isCorrect: false },
                { text: 'No security testing in pipelines to maintain development velocity', isCorrect: false },
                { text: 'Public repositories and unsecured artifact storage for team collaboration', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the AWS compliance and governance services for enterprise security?',
            explanation: 'AWS compliance and governance services: AWS Config for resource configuration compliance and remediation, AWS Security Hub for centralized security findings aggregation, AWS Control Tower for multi-account governance and guardrails, AWS Organizations for account management and service control policies, AWS CloudFormation for infrastructure as code compliance, AWS Systems Manager for patch management and compliance reporting, AWS Trusted Advisor for security recommendations, AWS Personal Health Dashboard for service impact awareness, and AWS Artifact for compliance documentation access. Implement automated compliance checking, remediation workflows, and regular compliance reporting. Reference: https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html',
            points: 1,
            answers: {
              create: [
                { text: 'Config for compliance, Security Hub for findings, Control Tower for governance, Organizations for policies', isCorrect: true },
                { text: 'Manual compliance checking using spreadsheets and periodic reviews only', isCorrect: false },
                { text: 'Third-party compliance tools without any AWS-native governance services', isCorrect: false },
                { text: 'Single account deployment without any organizational or governance controls', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement incident response and forensics capabilities in AWS?',
            explanation: 'AWS incident response and forensics: Enable comprehensive logging with CloudTrail, VPC Flow Logs, and application logs; implement automated incident detection with GuardDuty and Security Hub; create incident response runbooks with Systems Manager documents; implement automated isolation with Lambda functions and Step Functions; use EC2 instance isolation and EBS snapshot creation for forensics; implement network forensics with VPC Flow Logs analysis; use AWS Security Hub for centralized incident management; implement communication workflows with SNS and ChatBot; create forensic analysis environments with isolated VPCs; and maintain incident response team access with emergency break-glass procedures. Regular incident response testing and tabletop exercises are essential. Reference: https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html',
            points: 1,
            answers: {
              create: [
                { text: 'Comprehensive logging, automated detection, incident runbooks, isolation procedures, forensic analysis capabilities', isCorrect: true },
                { text: 'Manual incident response processes without any automation or logging', isCorrect: false },
                { text: 'Only email notifications for incident response without any forensic capabilities', isCorrect: false },
                { text: 'Third-party incident response tools without AWS service integration', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the security considerations for serverless applications in AWS?',
            explanation: 'Serverless security considerations: Implement function-level IAM roles with least privilege, use environment variables encryption with KMS, implement proper input validation and output encoding, enable X-Ray tracing for security monitoring, implement API Gateway authentication and authorization, use VPC for network isolation when needed, implement proper error handling to avoid information disclosure, enable CloudWatch Logs encryption, implement secrets management with Secrets Manager, use AWS SAM for secure deployment templates, implement function versioning and aliases for secure deployments, monitor function behavior with GuardDuty, and implement proper CORS policies for web applications. Consider cold start security implications and function memory limits. Reference: https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html',
            points: 1,
            answers: {
              create: [
                { text: 'Function-level IAM roles, encryption, input validation, API Gateway auth, monitoring, and secure deployment', isCorrect: true },
                { text: 'No security considerations needed since serverless is inherently secure', isCorrect: false },
                { text: 'Only perimeter security without any function-level security controls', isCorrect: false },
                { text: 'Shared IAM roles across all functions for operational simplicity', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement container security in Amazon ECS and EKS?',
            explanation: 'Container security in ECS/EKS: Implement task-level IAM roles for fine-grained permissions, use ECR for secure container image storage with vulnerability scanning, implement image signing and verification, use Fargate for improved isolation, implement network policies for pod-to-pod communication in EKS, use AWS Security Groups for network-level security, enable container insights for monitoring, implement secrets management with Secrets Manager integration, use read-only root filesystems, implement resource limits and constraints, enable audit logging for Kubernetes API server, implement Pod Security Standards, use service mesh like App Mesh for advanced security policies, and regularly update container images and orchestration platforms. Reference: https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/security.html',
            points: 1,
            answers: {
              create: [
                { text: 'Task-level IAM, ECR scanning, image signing, Fargate isolation, network policies, secrets management', isCorrect: true },
                { text: 'Default container configurations without any security hardening measures', isCorrect: false },
                { text: 'Host-level security only without any container-specific security controls', isCorrect: false },
                { text: 'Public container images without vulnerability scanning or access controls', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the AWS security services for protecting web applications?',
            explanation: 'AWS web application security services: AWS WAF for application-layer filtering with custom rules, rate limiting, and geo-blocking; AWS Shield Standard (free DDoS protection) and Shield Advanced (enhanced DDoS protection with 24/7 support); Amazon CloudFront with origin access identity for S3 protection; AWS Certificate Manager for SSL/TLS certificates; Amazon API Gateway with throttling and authentication; AWS Cognito for user authentication and authorization; AWS App Runner with built-in security features; Application Load Balancer with security groups and SSL termination; and integration with third-party security solutions through AWS Marketplace. Implement security headers, CSRF protection, and input validation. Reference: https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html',
            points: 1,
            answers: {
              create: [
                { text: 'AWS WAF for filtering, Shield for DDoS, CloudFront, Certificate Manager, API Gateway, and Cognito', isCorrect: true },
                { text: 'Only application-level security without any AWS-managed security services', isCorrect: false },
                { text: 'Perimeter firewalls only without application-layer protection mechanisms', isCorrect: false },
                { text: 'Manual security controls without any automated or managed security services', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement data loss prevention (DLP) and data classification in AWS?',
            explanation: 'AWS data loss prevention and classification: Amazon Macie for automated discovery and classification of sensitive data in S3, AWS CloudTrail for data access auditing, S3 bucket policies and access control for data protection, S3 Object Lock for compliance and retention, KMS for encryption key management, VPC endpoints for private data access, AWS Config for data governance compliance, CloudWatch for data access monitoring, GuardDuty for anomalous data access detection, and integration with third-party DLP solutions. Implement data tagging strategies, access logging, and regular access reviews. Establish data classification policies and automated enforcement mechanisms. Reference: https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html',
            points: 1,
            answers: {
              create: [
                { text: 'Amazon Macie for classification, S3 policies, Object Lock, KMS encryption, access logging, and monitoring', isCorrect: true },
                { text: 'Manual data classification without any automated discovery or protection tools', isCorrect: false },
                { text: 'No data classification needed since all data should be treated equally', isCorrect: false },
                { text: 'Application-level DLP only without any infrastructure or storage-level protection', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the security implications of multi-account AWS architecture?',
            explanation: 'Multi-account security implications: Use AWS Organizations for centralized account management and consolidated billing, implement Service Control Policies (SCPs) for account-level guardrails, establish cross-account IAM roles for secure access, use AWS Single Sign-On for federated access management, implement centralized logging with cross-account CloudTrail and S3, use AWS Config aggregators for compliance monitoring across accounts, implement AWS Security Hub for centralized security findings, use AWS Control Tower for automated account provisioning with security baselines, establish network connectivity with Transit Gateway or VPC peering, and implement separate accounts for different environments (dev/staging/prod) and business units. Reference: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html',
            points: 1,
            answers: {
              create: [
                { text: 'Organizations, SCPs, cross-account roles, SSO, centralized logging, Config aggregators, Security Hub', isCorrect: true },
                { text: 'Single account deployment to avoid complexity of multi-account management', isCorrect: false },
                { text: 'Separate AWS accounts with no centralized management or security controls', isCorrect: false },
                { text: 'Manual account management without any organizational or governance tools', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement security automation and orchestration in AWS?',
            explanation: 'AWS security automation and orchestration: Use AWS Lambda for automated security responses and remediation, implement Step Functions for complex security workflows, use CloudWatch Events/EventBridge for security event routing, create Systems Manager Automation documents for standardized responses, implement Security Hub custom actions for automated remediation, use AWS Config Rules for continuous compliance monitoring and automatic remediation, implement GuardDuty automated responses for threat mitigation, use CloudFormation and CDK for infrastructure security automation, implement AWS Security Hub integration with ticketing systems, and use third-party SOAR platforms integrated with AWS APIs. Establish security playbooks and automated incident response procedures. Reference: https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cwe-integration.html',
            points: 1,
            answers: {
              create: [
                { text: 'Lambda for responses, Step Functions for workflows, EventBridge, Config Rules, automated remediation', isCorrect: true },
                { text: 'Only manual security processes without any automation or orchestration tools', isCorrect: false },
                { text: 'Third-party security tools without any AWS service integration capabilities', isCorrect: false },
                { text: 'Scheduled security tasks without any event-driven automation mechanisms', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the AWS services for vulnerability management and security assessments?',
            explanation: 'AWS vulnerability management services: Amazon Inspector for EC2 instance and container vulnerability assessment, ECR vulnerability scanning for container images, AWS Security Hub for centralized vulnerability findings, Systems Manager Patch Manager for automated patching, AWS Config for configuration vulnerability detection, Trusted Advisor for security recommendations, GuardDuty for runtime threat detection, Macie for data security assessment, CloudFormation Guard for infrastructure as code security, third-party vulnerability scanners available in AWS Marketplace, and AWS Well-Architected Tool for security pillar assessment. Implement continuous vulnerability scanning, patch management processes, and regular security assessments. Reference: https://docs.aws.amazon.com/inspector/latest/userguide/inspector_introduction.html',
            points: 1,
            answers: {
              create: [
                { text: 'Inspector for instances, ECR scanning, Security Hub, Patch Manager, Config, and third-party tools', isCorrect: true },
                { text: 'Manual vulnerability assessments using external tools only', isCorrect: false },
                { text: 'No vulnerability management since AWS handles all security automatically', isCorrect: false },
                { text: 'Periodic penetration testing without any continuous vulnerability monitoring', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement network security monitoring and analysis in AWS?',
            explanation: 'AWS network security monitoring: Enable VPC Flow Logs for all VPCs with comprehensive logging to S3 or CloudWatch Logs, use GuardDuty for network anomaly detection and threat intelligence, implement AWS Network Firewall for advanced packet inspection, use CloudWatch Insights for flow log analysis and queries, implement Transit Gateway Flow Logs for inter-VPC traffic monitoring, use AWS X-Ray for application-level network tracing, implement third-party network monitoring tools integrated with VPC Flow Logs, use Amazon Detective for network investigation and analysis, implement DNS logging and monitoring, and establish network security baselines with automated alerting for deviations. Regular network security assessments and penetration testing are recommended. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html',
            points: 1,
            answers: {
              create: [
                { text: 'VPC Flow Logs, GuardDuty, Network Firewall, CloudWatch Insights, Detective, DNS monitoring, and analysis', isCorrect: true },
                { text: 'Basic network ACLs without any detailed logging or monitoring capabilities', isCorrect: false },
                { text: 'Perimeter monitoring only without any internal network traffic analysis', isCorrect: false },
                { text: 'Manual network monitoring using command-line tools and spreadsheets', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the AWS security services for protecting APIs and microservices?',
            explanation: 'AWS API and microservices security: API Gateway with authentication (Cognito, IAM, Lambda authorizers), throttling and usage plans, request/response validation, AWS WAF integration for Layer 7 protection, VPC endpoints for private API access, API Gateway resource policies, AWS Certificate Manager for SSL/TLS, CloudWatch for API monitoring and logging, X-Ray for distributed tracing, AWS App Mesh for service mesh security policies, ECS/EKS task-level IAM roles, service-to-service authentication with IAM roles, Secrets Manager for API credentials, and integration with AWS Security services. Implement proper API versioning, rate limiting, and security testing in CI/CD pipelines. Reference: https://docs.aws.amazon.com/apigateway/latest/developerguide/security.html',
            points: 1,
            answers: {
              create: [
                { text: 'API Gateway auth, WAF, VPC endpoints, service mesh policies, task-level IAM, monitoring and tracing', isCorrect: true },
                { text: 'No API security since microservices communicate internally only', isCorrect: false },
                { text: 'Basic authentication without any authorization or advanced security features', isCorrect: false },
                { text: 'Shared secrets across all microservices for simplified authentication', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement security for AWS database services?',
            explanation: 'AWS database security implementation: Enable encryption at rest using KMS for RDS, DynamoDB, Redshift, and DocumentDB, implement SSL/TLS encryption in transit, use IAM database authentication where supported, implement VPC security groups and NACLs for network-level protection, enable database activity monitoring and logging, use RDS Enhanced Monitoring for detailed metrics, implement proper backup encryption and retention, use database parameter groups for security configuration, implement read replicas in separate security zones, use AWS Secrets Manager for database credentials, enable AWS Config for database configuration compliance, implement database-level firewalls and access controls, and use AWS Database Migration Service for secure migrations. Regular security patching and vulnerability assessments are essential. Reference: https://docs.aws.amazon.com/rds/latest/userguide/Overview.Encryption.html',
            points: 1,
            answers: {
              create: [
                { text: 'KMS encryption, SSL/TLS, IAM database auth, VPC security, activity monitoring, Secrets Manager', isCorrect: true },
                { text: 'Default database security without any additional encryption or access controls', isCorrect: false },
                { text: 'Application-level encryption only without any database-native security features', isCorrect: false },
                { text: 'Public database access with simple username/password authentication only', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  console.log(`✅ Seeded AWS Security Specialty certification with comprehensive questions`)
  return awsSecuritySpecialty
}
