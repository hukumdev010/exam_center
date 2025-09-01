# Exam Center - Monorepo

A comprehensive monorepo containing both frontend (Next.js) and backend (FastAPI) applications for managing exam questions across multiple subjects and certifications. Uses PostgreSQL and Prisma ORM with Google authentication, progress tracking, and modern UI components.

## Architecture

This project is structured as a monorepo with separate frontend and backend applications:

```
exam_center/
├── frontend/          # Next.js application
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
├── backend/           # FastAPI application  
│   ├── main.py
│   ├── prisma/
│   ├── routers/
│   ├── package.json
│   └── Dockerfile
├── package.json       # Root package.json for monorepo management
├── docker-compose.yml # Multi-service Docker setup
└── README.md
```

## Features
- 🔐 **Google OAuth Authentication** - Secure sign-in with Google
- 📊 **Progress Tracking** - Track your quiz progress and scores
- 🏆 **Profile Dashboard** - View your achievements and statistics
- 🎯 **Multiple Certifications** - Wide range of technical certifications
- 💾 **Resume Quizzes** - Continue where you left off
- 🎨 **Modern UI** - Beautiful interface with shadcn/ui components
- 🔄 **Real-time Updates** - Progress synced across devices
- 🏗️ **Monorepo Architecture** - Organized codebase with separate frontend/backend

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
- Node.js 20+ (if running without Docker)
- Python 3.11+ (for backend development)
- Google OAuth credentials (for authentication)

### Setup Instructions

#### Option 1: Using DevContainer (Recommended)
1. Clone the repository
2. Open in VS Code
3. When prompted, choose "Reopen in Container"
4. The devcontainer will automatically:
   - Start PostgreSQL database
   - Install all dependencies (frontend + backend)
   - Generate Prisma client
   - Push database schema
   - Seed the database with initial data

#### Option 2: Manual Setup
```bash
# Install root dependencies
npm install

# Install frontend dependencies
cd frontend && npm install

# Install backend dependencies  
cd ../backend && npm install
pip install -r requirements.txt

# Setup database
cd .. && npm run db:generate
npm run db:migrate
npm run db:seed
```

### Environment Variables

Create `.env` files in both `frontend/` and `backend/` directories based on the `.env.example` files provided.

#### Frontend Environment (`frontend/.env`)
```bash
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/exam_center"
NEXTAUTH_SECRET="your-secret-key-change-this-in-production"
GOOGLE_CLIENT_ID="your-google-client-id"
GOOGLE_CLIENT_SECRET="your-google-client-secret"
NEXT_PUBLIC_API_URL="http://localhost:8000"
```

#### Backend Environment (`backend/.env`)
```bash
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/exam_center"
GOOGLE_CLIENT_ID="your-google-client-id"
GOOGLE_CLIENT_SECRET="your-google-client-secret"
API_BASE_URL="http://localhost:8000"
FRONTEND_URL="http://localhost:3000"
```

**Production Note**: In production, these variables are automatically loaded from AWS Secrets Manager using the secret name `examCenterCredentials`.

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

### Running the Application

#### Development Mode (Both Services)
```bash
# Run both frontend and backend concurrently
npm run dev

# Or run individually:
npm run frontend:dev  # Runs on http://localhost:3000
npm run backend:dev   # Runs on http://localhost:8000
```

#### Using Docker Compose
```bash
# Run all services (frontend, backend, database)
npm run docker:dev

# Build and run
npm run docker:build
```

### Database Operations
```bash
# View database in Prisma Studio
cd backend && npm run db:studio

# Reset database and reseed  
cd backend && npx prisma db push --force-reset && npm run db:seed

# Create migration
cd backend && npm run db:migrate

# Generate Prisma client
cd backend && npm run db:generate
```

### Project Structure Commands
```bash
# Install dependencies for specific workspace
npm run install:frontend
npm run install:backend

# Build specific workspace
npm run frontend:build
npm run backend:build
```

### Adding UI Components
```bash
# Add shadcn/ui components (run from frontend directory)
cd frontend && npx shadcn@latest add <component>
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
