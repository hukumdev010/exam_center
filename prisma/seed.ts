import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  // Create AWS certification
  const aws = await prisma.certification.upsert({
    where: { slug: 'aws-solutions-architect-associate' },
    update: {},
    create: {
      name: 'AWS Certified Solutions Architect – Associate',
      description: 'Entry-level AWS certification for solutions architects',
      slug: 'aws-solutions-architect-associate',
      questions: {
        create: [
          {
            text: 'Which AWS service is used for object storage?',
            explanation: 'Amazon S3 (Simple Storage Service) is designed for object storage. It provides industry-leading scalability, data availability, security, and performance.',
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
            explanation: 'Amazon VPC (Virtual Private Cloud) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.',
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
            text: 'Which AWS service is best for hosting a relational database?',
            explanation: 'Amazon RDS (Relational Database Service) makes it easy to set up, operate, and scale a relational database in the cloud with support for MySQL, PostgreSQL, Oracle, SQL Server, and more.',
            points: 1,
            answers: {
              create: [
                { text: 'Amazon RDS', isCorrect: true },
                { text: 'Amazon S3', isCorrect: false },
                { text: 'Amazon DynamoDB', isCorrect: false },
                { text: 'Amazon ElastiCache', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the maximum size of an S3 object?',
            explanation: 'The maximum size of an S3 object is 5TB. For objects larger than 100MB, AWS recommends using multipart upload.',
            points: 1,
            answers: {
              create: [
                { text: '5TB', isCorrect: true },
                { text: '1TB', isCorrect: false },
                { text: '100GB', isCorrect: false },
                { text: '10TB', isCorrect: false },
              ],
            },
          },
        ],
      },
    },
  })

  console.log(`Created certification: ${aws.name}`)
}

main()
  .then(async () => {
    await prisma.$disconnect()
  })
  .catch(async (e) => {
    console.error(e)
    await prisma.$disconnect()
    process.exit(1)
  })
