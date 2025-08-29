import { PrismaClient } from '../../src/generated/prisma'

export async function seedAwsCertifications(prisma: PrismaClient, categoryId: number) {
  // AWS Cloud Practitioner
  const awsCloudPractitioner = await prisma.certification.upsert({
    where: { slug: 'aws-cloud-practitioner' },
    update: {},
    create: {
      name: 'AWS Certified Cloud Practitioner',
      description: 'Entry-level AWS certification covering cloud fundamentals',
      slug: 'aws-cloud-practitioner',
      level: 'Foundational',
      duration: 90,
      questionsCount: 65,
      categoryId,
      questions: {
        create: [
          {
            text: 'What are the six advantages of cloud computing according to AWS?',
            explanation: 'The six advantages are: Trade capital expense for variable expense, benefit from massive economies of scale, stop guessing about capacity, increase speed and agility, stop spending money running and maintaining data centers, and go global in minutes.',
            points: 1,
            answers: {
              create: [
                { text: 'Cost savings, scalability, reliability, speed, global reach, and focus', isCorrect: true },
                { text: 'Security, compliance, performance, availability, durability, and cost', isCorrect: false },
                { text: 'Infrastructure, platform, software, monitoring, backup, and networking', isCorrect: false },
                { text: 'Compute, storage, database, networking, analytics, and machine learning', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the AWS Well-Architected Framework?',
            explanation: 'The AWS Well-Architected Framework consists of five pillars: Operational Excellence, Security, Reliability, Performance Efficiency, and Cost Optimization.',
            points: 1,
            answers: {
              create: [
                { text: 'A framework with five pillars for cloud architecture best practices', isCorrect: true },
                { text: 'A service for monitoring applications', isCorrect: false },
                { text: 'A database design methodology', isCorrect: false },
                { text: 'A security compliance standard', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  // AWS Solutions Architect Associate
  const awsSolutionsArchitectAssociate = await prisma.certification.upsert({
    where: { slug: 'aws-solutions-architect-associate' },
    update: {},
    create: {
      name: 'AWS Certified Solutions Architect – Associate',
      description: 'Design and deploy scalable, highly available systems on AWS',
      slug: 'aws-solutions-architect-associate',
      level: 'Associate',
      duration: 130,
      questionsCount: 65,
      categoryId,
      questions: {
        create: [
          {
            text: 'Which AWS service is used for object storage?',
            explanation: 'Amazon S3 (Simple Storage Service) is designed for object storage with industry-leading scalability, data availability, security, and performance.',
            points: 1,
            answers: {
              create: [
                { text: 'Amazon S3', isCorrect: true },
                { text: 'Amazon EBS', isCorrect: false },
                { text: 'Amazon EFS', isCorrect: false },
                { text: 'Amazon FSx', isCorrect: false },
              ],
            },
          },
          {
            text: 'Which service provides serverless compute in AWS?',
            explanation: 'AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume.',
            points: 1,
            answers: {
              create: [
                { text: 'AWS Lambda', isCorrect: true },
                { text: 'Amazon EC2', isCorrect: false },
                { text: 'Amazon ECS', isCorrect: false },
                { text: 'AWS Batch', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of Amazon VPC?',
            explanation: 'Amazon VPC (Virtual Private Cloud) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network.',
            points: 1,
            answers: {
              create: [
                { text: 'To create an isolated network environment', isCorrect: true },
                { text: 'To store files and objects', isCorrect: false },
                { text: 'To run containerized applications', isCorrect: false },
                { text: 'To manage user permissions', isCorrect: false },
              ],
            },
          },
          {
            text: 'Which AWS service provides managed relational databases?',
            explanation: 'Amazon RDS (Relational Database Service) makes it easy to set up, operate, and scale relational databases in the cloud.',
            points: 1,
            answers: {
              create: [
                { text: 'Amazon RDS', isCorrect: true },
                { text: 'Amazon DynamoDB', isCorrect: false },
                { text: 'Amazon ElastiCache', isCorrect: false },
                { text: 'Amazon Redshift', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Amazon CloudFront?',
            explanation: 'Amazon CloudFront is a content delivery network (CDN) service that delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds.',
            points: 1,
            answers: {
              create: [
                { text: 'A content delivery network (CDN) service', isCorrect: true },
                { text: 'A cloud storage service', isCorrect: false },
                { text: 'A database service', isCorrect: false },
                { text: 'A monitoring service', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  // AWS Developer Associate
  const awsDeveloperAssociate = await prisma.certification.upsert({
    where: { slug: 'aws-developer-associate' },
    update: {},
    create: {
      name: 'AWS Certified Developer – Associate',
      description: 'Develop and maintain applications on the AWS platform',
      slug: 'aws-developer-associate',
      level: 'Associate',
      duration: 130,
      questionsCount: 65,
      categoryId,
      questions: {
        create: [
          {
            text: 'Which AWS service is primarily used for application deployment and management?',
            explanation: 'AWS Elastic Beanstalk is designed for easy application deployment and management. It handles the deployment details while you focus on your application code.',
            points: 1,
            answers: {
              create: [
                { text: 'AWS Elastic Beanstalk', isCorrect: true },
                { text: 'AWS CodePipeline', isCorrect: false },
                { text: 'Amazon ECS', isCorrect: false },
                { text: 'AWS Lambda', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the best way to store user session data for a web application on AWS?',
            explanation: 'Amazon DynamoDB provides fast, predictable performance and is ideal for storing user session data with automatic scaling.',
            points: 1,
            answers: {
              create: [
                { text: 'Amazon DynamoDB', isCorrect: true },
                { text: 'Amazon S3', isCorrect: false },
                { text: 'Amazon RDS', isCorrect: false },
                { text: 'Amazon EFS', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  // AWS Solutions Architect Professional
  const awsSolutionsArchitectProfessional = await prisma.certification.upsert({
    where: { slug: 'aws-solutions-architect-professional' },
    update: {},
    create: {
      name: 'AWS Certified Solutions Architect – Professional',
      description: 'Advanced AWS certification for experienced solutions architects',
      slug: 'aws-solutions-architect-professional',
      level: 'Professional',
      duration: 180,
      questionsCount: 75,
      categoryId,
    },
  })

  // AWS Security Specialty
  const awsSecuritySpecialty = await prisma.certification.upsert({
    where: { slug: 'aws-security-specialty' },
    update: {},
    create: {
      name: 'AWS Certified Security – Specialty',
      description: 'Advanced AWS security certification',
      slug: 'aws-security-specialty',
      level: 'Specialty',
      duration: 170,
      questionsCount: 65,
      categoryId,
      questions: {
        create: [
          {
            text: 'Which service provides centralized logging for security events across AWS services?',
            explanation: 'AWS CloudTrail provides logging of API calls and events across AWS services, essential for security auditing and compliance.',
            points: 1,
            answers: {
              create: [
                { text: 'AWS CloudTrail', isCorrect: true },
                { text: 'Amazon CloudWatch', isCorrect: false },
                { text: 'AWS Config', isCorrect: false },
                { text: 'Amazon GuardDuty', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the best practice for managing secrets in AWS applications?',
            explanation: 'AWS Secrets Manager provides secure storage and automatic rotation of secrets like passwords, API keys, and database credentials.',
            points: 1,
            answers: {
              create: [
                { text: 'AWS Secrets Manager', isCorrect: true },
                { text: 'Amazon S3 with encryption', isCorrect: false },
                { text: 'AWS Systems Manager Parameter Store', isCorrect: false },
                { text: 'Hard-code in application', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  return {
    awsCloudPractitioner,
    awsSolutionsArchitectAssociate,
    awsDeveloperAssociate,
    awsSolutionsArchitectProfessional,
    awsSecuritySpecialty
  }
}
