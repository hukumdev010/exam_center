# Exam Center

A Next.js application for managing AWS exam questions, using PostgreSQL and Prisma ORM. Includes shadcn/ui for modern UI components and a devcontainer for easy development setup.

## Features
- Next.js (TypeScript, Tailwind CSS, ESLint, App Router)
- PostgreSQL database integration
- Prisma ORM for schema and migrations
- shadcn/ui for UI components
- Devcontainer for VS Code

## Getting Started
1. Clone the repository
2. Open in VS Code and reopen in devcontainer
3. Set up PostgreSQL and update `DATABASE_URL` in `.env`
4. Run migrations: `npx prisma migrate dev`
5. Start the app: `npm run dev`

## Devcontainer
- Dockerfile and devcontainer.json included
- PostgreSQL client installed

## Database
- Default connection: `postgresql://postgres:postgres@localhost:5432/exam_center`
- Update `.env` as needed

## UI
- Use shadcn/ui CLI to add components: `npx shadcn@latest add <component>`

## License
MIT
# Exam Center

An interactive exam practice application for certification preparation including AWS, Terraform, Cisco, and more.

## Features

- ✅ Interactive quiz interface with multiple choice questions
- ✅ Point system for correct answers on first attempt
- ✅ Detailed explanations for each question
- ✅ Progress tracking during quiz
- ✅ Final score and completion summary
- ✅ PostgreSQL database with Prisma ORM

## Tech Stack

- **Frontend**: Next.js 15, React, TypeScript, Tailwind CSS
- **UI Components**: shadcn/ui
- **Database**: PostgreSQL with Prisma ORM
- **Icons**: Lucide React

## Getting Started

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up your database:**
   - Copy `.env.example` to `.env`
   - Update `DATABASE_URL` with your PostgreSQL connection string

3. **Generate Prisma client:**
   ```bash
   npm run db:generate
   ```

4. **Run database migrations:**
   ```bash
   npm run db:migrate
   ```

5. **Seed the database with sample questions:**
   ```bash
   npm run db:seed
   ```

6. **Start the development server:**
   ```bash
   npm run dev
   ```

7. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

## Database Schema

The application uses the following main models:

- **Certification**: Represents different certification types (AWS, Cisco, etc.)
- **Question**: Individual exam questions with explanations
- **Answer**: Multiple choice answers for each question

## Sample AWS Questions

The seed file includes 5 AWS Solutions Architect Associate questions covering:
- Amazon S3 object storage
- AWS Lambda serverless compute
- Amazon VPC networking
- Amazon RDS databases
- S3 object size limits

## Usage

1. **Taking a Quiz**: Click through questions, select answers, and see immediate feedback
2. **Explanations**: Click "Show Explanation" to understand why an answer is correct
3. **Scoring**: Earn points for correct answers on first attempt
4. **Progress**: Track your progress with the progress bar
5. **Completion**: View final score and restart if desired

## Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npm run db:generate` - Generate Prisma client
- `npm run db:migrate` - Run database migrations
- `npm run db:seed` - Seed database with sample data

## Project Structure

```
src/
├── app/
│   ├── page.tsx          # Main quiz page
│   ├── layout.tsx        # App layout
│   └── globals.css       # Global styles
├── components/
│   ├── QuestionCard.tsx  # Individual question component
│   ├── ExamQuiz.tsx      # Quiz management component
│   └── ui/               # shadcn/ui components
└── lib/
    └── utils.ts          # Utility functions

prisma/
├── schema.prisma         # Database schema
└── seed.ts              # Database seeding
```

## Adding New Questions

To add new questions, you can either:

1. **Use the seed file**: Add questions to `prisma/seed.ts`
2. **Create API routes**: Build admin interfaces to manage questions
3. **Direct database**: Insert questions directly into PostgreSQL

## Environment Variables

Create a `.env` file with:

```env
DATABASE_URL="postgresql://user:password@localhost:5432/exam_center?schema=public"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request
