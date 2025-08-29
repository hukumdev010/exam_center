# Exam Center

A comprehensive Next.js application for managing exam questions across multiple subjects and certifications, using PostgreSQL and Prisma ORM. Features Google authentication, progress tracking, and modern UI components with shadcn/ui.

## Features
- 🔐 **Google OAuth Authentication** - Secure sign-in with Google
- 📊 **Progress Tracking** - Track your quiz progress and scores
- 🏆 **Profile Dashboard** - View your achievements and statistics
- 🎯 **Multiple Certifications** - Wide range of technical certifications
- 💾 **Resume Quizzes** - Continue where you left off
- 🎨 **Modern UI** - Beautiful interface with shadcn/ui components
- 🔄 **Real-time Updates** - Progress synced across devices

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

## Getting Started

### Prerequisites
- Docker and Docker Compose
- VS Code with Remote-Containers extension
- Google OAuth credentials (for authentication)

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

### Google OAuth Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google+ API and Google OAuth2 API
4. Go to "Credentials" and create OAuth 2.0 Client IDs
5. Add authorized redirect URIs:
   - `http://localhost:3000/api/auth/callback/google` (for development)
6. Copy the Client ID and Client Secret to your `.env` file

### Environment Variables
Update your `.env` file with the following:
```bash
# PostgreSQL database connection
DATABASE_URL="postgresql://postgres:postgres@db:5432/exam_center"

# NextAuth.js configuration
NEXTAUTH_SECRET="your-secret-key-change-this-in-production"
NEXTAUTH_URL="http://localhost:3000"

# Google OAuth credentials
GOOGLE_CLIENT_ID="your-google-client-id"
GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

5. Start the development server: `npm run dev`
6. Open [http://localhost:3000](http://localhost:3000) in your browser

## Authentication & User Features

### Google Sign-In
- Secure authentication with Google OAuth
- User profile information stored in database
- Session management with NextAuth.js

### Progress Tracking
- **Continue Learning**: Resume quizzes where you left off
- **Real-time Progress**: Sync progress across devices
- **Score Tracking**: Track correct answers and points
- **Completion Status**: Mark completed quizzes

### Profile Dashboard
- **Statistics**: View total points, completed quizzes, and correct answers
- **In Progress**: See all quizzes currently in progress
- **Completed**: Review all finished quizzes with scores
- **Performance Metrics**: Track your learning journey

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

### Manual Database Setup (if needed)
```bash
# Generate Prisma client
npx prisma generate

# Push schema to database
npx prisma db push

# Seed database with initial data
npm run db:seed
```

### Adding UI Components
```bash
# Add shadcn/ui components
npx shadcn@latest add <component>
```

## Database Schema

### Core Models
- **Category**: Exam categories (AWS, DevOps, etc.)
- **Certification**: Individual certifications within categories
- **Question**: Quiz questions with explanations and points
- **Answer**: Multiple choice answers for questions

### Authentication Models (NextAuth.js)
- **User**: User profiles and account information
- **Account**: OAuth provider account information
- **Session**: Active user sessions

### Progress Tracking Models
- **UserProgress**: Real-time quiz progress for each user
- **QuizAttempt**: Completed quiz attempts with scores

## API Routes

### Authentication
- `GET/POST /api/auth/*` - NextAuth.js authentication endpoints

### Progress & Quizzes
- `GET/POST /api/progress` - User progress tracking
- `POST /api/quiz-attempts` - Save completed quiz attempts

### Data
- `GET /api/categories` - Available quiz categories
- `GET /api/certifications/[slug]` - Certification details and questions

## Tech Stack
- **Next.js 15** - React framework with App Router
- **TypeScript** - Type safety and developer experience
- **Tailwind CSS** - Utility-first CSS framework
- **shadcn/ui** - Beautiful React components
- **NextAuth.js** - Authentication with Google OAuth
- **Prisma** - Type-safe ORM for PostgreSQL
- **PostgreSQL** - Relational database
- **Docker** - Containerized development environment

## License
MIT
