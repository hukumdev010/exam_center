import { ExamQuiz } from "@/components/ExamQuiz";

// Sample data - in a real app, this would come from your API/database
const sampleQuestions = [
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
];

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-50 py-8">
      <ExamQuiz 
        questions={sampleQuestions}
        certificationName="AWS Certified Solutions Architect – Associate"
      />
    </main>
  );
}
