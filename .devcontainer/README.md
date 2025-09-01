# DevContainer Setup for Exam Center

This DevContainer configuration provides a complete development environment for the Exam Center application with both frontend (Next.js) and backend (FastAPI + Python) components.

## What's Included

- **Node.js** with TypeScript support
- **Python 3** with virtual environment
- **PostgreSQL** database
- **SQLAlchemy** ORM for database management
- **Alembic** for database migrations
- **VS Code extensions** for development

## Automatic Setup

When you open this project in VS Code with the Dev Containers extension, it will automatically:

1. 🗄️ Start a PostgreSQL database
2. 📦 Install frontend dependencies (npm install)
3. 🐍 Create a Python virtual environment
4. 📦 Install Python dependencies (pip install)
5. � Run database migrations with Alembic
6. 🌱 Seed the database with sample data

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
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000  # Start development server
```

### Database Migration Commands

```bash
cd backend
source venv/bin/activate

# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# Re-seed database
python scripts/seed.py
```

npx prisma db push # Push schema changes
npx prisma generate # Generate Prisma client
npx prisma studio # Open database GUI

````

## Troubleshooting

If you encounter issues with the setup, run the troubleshooting script:

```bash
./troubleshoot.sh
# or if permissions are restricted:
bash troubleshoot.sh
````

For a quick health check of running services:

```bash
bash /tmp/health-check.sh
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
