# DevContainer Setup for Exam Center

This DevContainer configuration provides a complete development environment for the Exam Center application with both frontend (Next.js) and backend (FastAPI + Python) components.

## What's Included

- **Node.js** with TypeScript support
- **Python 3** with virtual environment
- **PostgreSQL** database
- **Prisma** ORM for database management
- **VS Code extensions** for development

## Automatic Setup

When you open this project in VS Code with the Dev Containers extension, it will automatically:

1. 🗄️ Start a PostgreSQL database
2. 📦 Install frontend dependencies (npm install)
3. 🐍 Create a Python virtual environment
4. 📦 Install Python dependencies (pip install)
5. 🔧 Generate Prisma client
6. 🗄️ Push database schema
7. 🌱 Seed the database with sample data

## Manual Commands

If the automatic setup fails or you need to run commands manually:

### Frontend
```bash
npm run dev --prefix frontend    # Start development server
npm run build --prefix frontend  # Build for production
```

### Backend
```bash
cd backend
source venv/bin/activate         # Activate virtual environment
npm run dev                      # Start development server
npm run db:studio               # Open Prisma Studio
npm run db:seed                 # Re-seed database
```

### Database
```bash
cd backend
source venv/bin/activate
npx prisma db push              # Push schema changes
npx prisma generate             # Generate Prisma client
npx prisma studio               # Open database GUI
```

## Troubleshooting

If you encounter issues with the setup, run the troubleshooting script:

```bash
bash /tmp/troubleshoot.sh
```

This will check:
- Database connectivity
- Virtual environment status
- Dependencies installation
- Prisma client generation

## Port Forwarding

The following ports are automatically forwarded:
- **3000**: Frontend (Next.js)
- **8000**: Backend (FastAPI)
- **5432**: PostgreSQL database

## Environment Variables

The following environment variables are set:
- `DATABASE_URL`: PostgreSQL connection string
- `PYTHONPATH`: Python path for backend modules

## Database Credentials

- **Host**: localhost
- **Port**: 5432
- **Database**: exam_center
- **User**: postgres
- **Password**: postgres

## File Structure

```
.devcontainer/
├── devcontainer.json      # DevContainer configuration
├── docker-compose.yml     # Multi-service setup
├── Dockerfile            # Container definition
├── post-create.sh        # Automatic setup script
├── troubleshoot.sh       # Troubleshooting script
└── README.md            # This file
```

## Restarting Services

If you need to restart the database:
```bash
docker-compose restart db
```

To rebuild the entire container:
- Use Command Palette: "Dev Containers: Rebuild Container"
