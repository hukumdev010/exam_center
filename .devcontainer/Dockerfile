FROM mcr.microsoft.com/vscode/devcontainers/typescript-node:latest

# Install required dependencies
RUN npm install -g prisma

# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client

# Set up environment variables
ENV DATABASE_URL="postgresql://postgres:postgres@localhost:5432/exam_center"

# Expose default Next.js port
EXPOSE 3000

# Start command
CMD ["npm", "run", "dev"]
