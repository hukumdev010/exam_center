# Exam Center

A comprehensive Next.js application for managing exam questions across multiple subjects and certifications, using PostgreSQL and Prisma ORM. Includes shadcn/ui for modern UI components and a devcontainer for easy development setup.

## Available Subjects & Certifications

### Programming Languages & Technologies
- **JavaScript** - Modern JavaScript programming concepts and best practices
- **TypeScript** - TypeScript language features and advanced type system
- **Node.js** - Server-side JavaScript runtime and ecosystem

### System Design & Architecture
- **System Design** - Comprehensive system design concepts and best practices

### AWS Certifications
- **AWS Certified Cloud Practitioner** - Entry-level AWS certification covering cloud fundamentals
- **AWS Certified Solutions Architect – Associate** - Entry-level AWS certification for solutions architects
- **AWS Certified Solutions Architect – Professional** - Advanced AWS certification for experienced solutions architects
- **AWS Certified Developer – Associate** - AWS certification for developers building applications on AWS
- **AWS Certified SysOps Administrator – Associate** - AWS certification for systems administrators
- **AWS Certified DevOps Engineer – Professional** - Advanced AWS certification for DevOps engineers
- **AWS Certified Security – Specialty** - Advanced AWS security certification
- **AWS Certified Advanced Networking – Specialty** - Advanced AWS networking certification
- **AWS Certified Machine Learning – Specialty** - AWS machine learning and AI services certification
- **AWS Certified Data Analytics – Specialty** - AWS data analytics and big data services certification
- **AWS Certified Database – Specialty** - AWS database services and optimization certification
- **AWS Certified SAP on AWS – Specialty** - AWS certification for SAP workloads on AWS

### DevOps & Infrastructure
- **HashiCorp Certified: Terraform Associate** - Infrastructure as Code with Terraform
- **HashiCorp Certified: Terraform Professional** - Advanced Terraform skills and enterprise features

### Kubernetes Certifications
- **Certified Kubernetes Administrator (CKA)** - Kubernetes cluster administration and management
- **Certified Kubernetes Application Developer (CKAD)** - Kubernetes application development and deployment
- **Certified Kubernetes Security Specialist (CKS)** - Kubernetes security best practices and implementation

### Linux
- **Linux Fundamentals** - Core Linux operating system concepts and administration
- **Linux Professional Institute Certification (LPIC)** - Advanced Linux system administration and security

## Features
- Next.js (TypeScript, Tailwind CSS, ESLint, App Router)
- PostgreSQL database with Docker Compose
- Prisma ORM for schema and migrations
- shadcn/ui for UI components
- Devcontainer for VS Code with PostgreSQL

## Getting Started

### Prerequisites
- Docker and Docker Compose
- VS Code with Remote-Containers extension

### Setup Instructions
1. Clone the repository
2. Open in VS Code
3. When prompted, choose "Reopen in Container"
4. The devcontainer will automatically:
   - Start PostgreSQL database
   - Install npm dependencies
   - Generate Prisma client
   - Push database schema
   - Seed the database with initial data
5. Start the development server: `npm run dev`

### Manual Database Setup (if needed)
```bash
# Generate Prisma client
npx prisma generate

# Push schema to database
npx prisma db push

# Seed database with initial data
npm run db:seed
```

## Development

### Database Operations
```bash
# View database in Prisma Studio
npx prisma studio

# Reset database and reseed
npx prisma db push --force-reset && npm run db:seed

# Create migration
npx prisma migrate dev --name migration_name
```

### Adding UI Components
```bash
# Add shadcn/ui components
npx shadcn@latest add <component>
```

## Environment Variables
Copy `.env.example` to `.env` and update as needed:
```bash
cp .env.example .env
```

## Database Schema
- **Certification**: Represents exam subjects/certifications
- **Question**: Individual exam questions linked to certifications
- **Answer**: Multiple choice answers for each question

## License
MIT
This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
