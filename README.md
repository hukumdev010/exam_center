# Exam Center

A full-stack certification learning and exam platform with:
- **Frontend**: Next.js 15 + React 19 + TypeScript
- **Backend**: FastAPI + SQLAlchemy + Alembic
- **Database**: PostgreSQL
- **Infrastructure**: AWS CDK (EC2-based deployment)

## Monorepo Structure

```text
exam_center/
├── frontend/   # Next.js web app
├── backend/    # FastAPI API + business logic + migrations
├── cdk/        # AWS CDK infrastructure app
└── .devcontainer/ # Preconfigured local dev environment
```

## Quick Start (Recommended: Dev Container)

If you use VS Code Dev Containers, most setup is automated.

1. Open this repository in VS Code.
2. Run **Dev Containers: Reopen in Container**.
3. Wait for `.devcontainer/post-create.sh` to finish.
4. Start services:

```bash
# Terminal 1
cd backend
source venv/bin/activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 10000

# Terminal 2
cd frontend
yarn dev
```

App URLs:
- Frontend: http://localhost:3000
- Backend API docs: http://localhost:10000/docs

---

## Manual Local Setup (Without Dev Container)

## 1) Prerequisites
- Node.js 20+
- Yarn 4+
- Python 3.10+
- PostgreSQL 15+

## 2) Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

Update at least these values in `backend/.env`:
- `DATABASE_URL`
- `SECRET_KEY`
- `NEXTAUTH_SECRET`
- `FRONTEND_URL` (usually `http://localhost:3000`)

Run migrations and seed:

```bash
cd backend
source venv/bin/activate
alembic upgrade head
python run_seed.py
```

Start backend:

```bash
cd backend
source venv/bin/activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 10000
```

## 3) Frontend Setup

```bash
cd frontend
cp .env.example .env.local
yarn install
yarn dev
```

Set at least these values in `frontend/.env.local`:
- `NEXT_PUBLIC_API_URL=http://localhost:10000`
- `NEXTAUTH_URL=http://localhost:3000`
- `NEXTAUTH_SECRET=<same secret used by backend or your app auth flow>`

---

## Common Commands

## Frontend (`frontend/`)

```bash
yarn dev
yarn build
yarn start
yarn lint
yarn type-check
```

## Backend (`backend/`)

```bash
source venv/bin/activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 10000
alembic upgrade head
alembic revision --autogenerate -m "describe change"
python run_seed.py
```

---

## Environment Variables

Use the included templates:
- `backend/.env.example`
- `frontend/.env.example`

Important backend settings (selected):
- `DATABASE_URL`
- `SECRET_KEY`
- `ACCESS_TOKEN_EXPIRE_MINUTES`
- `FRONTEND_URL`
- `USE_SECRETS_MANAGER`
- `GEMINI_API`

Important frontend settings (selected):
- `NEXT_PUBLIC_API_URL`
- `NEXTAUTH_URL`
- `NEXTAUTH_SECRET`
- `NEXT_PUBLIC_GEMINI_API_KEY`

---

## Database & Migrations

All backend DB migrations live in `backend/alembic/versions`.

Typical flow:

```bash
cd backend
source venv/bin/activate
alembic revision --autogenerate -m "add new field"
alembic upgrade head
```

To inspect/seed data tooling, see `backend/scripts/`.

---

## Deployment (AWS CDK)

Infrastructure code is in `cdk/`.

Basic flow:

```bash
cd cdk
npm install
npm run build
npm run synth
npm run deploy
```

For full deployment instructions and parameterized examples, see:
- `cdk/README.md`
- `backend/aws-deployment/README.md`

---

## Additional Documentation

- Dev container guide: `.devcontainer/README.md`
- Backend script/seeding notes: `backend/scripts/README.md`
- CDK infrastructure guide: `cdk/README.md`

---

## Troubleshooting

- Ensure backend runs on **port 10000** and frontend points to it via `NEXT_PUBLIC_API_URL`.
- If auth/cookies fail in local dev, verify `FRONTEND_URL`, `NEXTAUTH_URL`, and CORS origins.
- If migrations fail, check PostgreSQL connectivity and `DATABASE_URL`.
- In dev container, run health check:

```bash
bash /tmp/health-check.sh
```

---

## Tech Stack Snapshot

- **Frontend**: Next.js, React, TypeScript, Redux Toolkit, SWR, Tailwind
- **Backend**: FastAPI, SQLAlchemy (async), Alembic, Pydantic
- **Data**: PostgreSQL
- **Infra**: AWS CDK
