import { PrismaClient } from '@/generated/prisma'
import { getRequiredEnv } from './env'

// Global Prisma instance with connection management
let prisma: PrismaClient | null = null

export async function getPrismaClient(): Promise<PrismaClient> {
  if (prisma) {
    return prisma
  }

  // Get DATABASE_URL from environment/secrets
  const databaseUrl = await getRequiredEnv('DATABASE_URL')
  
  prisma = new PrismaClient({
    datasources: {
      db: {
        url: databaseUrl
      }
    },
    log: process.env.NODE_ENV === 'development' ? ['query', 'error', 'warn'] : ['error']
  })

  return prisma
}

export async function disconnectPrisma(): Promise<void> {
  if (prisma) {
    await prisma.$disconnect()
    prisma = null
  }
}
