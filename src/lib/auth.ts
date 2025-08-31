import NextAuth, { NextAuthOptions } from "next-auth"
import GoogleProvider from "next-auth/providers/google"
import { PrismaAdapter } from "@auth/prisma-adapter"
import { PrismaClient } from "@/generated/prisma"
import { getRequiredEnv } from "./env"

const prisma = new PrismaClient()

// Create auth options with validated environment configuration from AWS Secrets Manager
async function createAuthOptions(): Promise<NextAuthOptions> {
  return {
    adapter: PrismaAdapter(prisma),
    providers: [
      GoogleProvider({
        clientId: await getRequiredEnv('GOOGLE_CLIENT_ID'),
        clientSecret: await getRequiredEnv('GOOGLE_CLIENT_SECRET'),
      }),
    ],
    secret: await getRequiredEnv('NEXTAUTH_SECRET'),
    callbacks: {
      async session({ session, user }) {
        if (session?.user && user?.id) {
          session.user.id = user.id
        }
        return session
      },
    },
    session: {
      strategy: "database",
    },
  }
}

// Cache for auth options
let authOptionsCache: NextAuthOptions | null = null

// Export auth options with caching
export async function getAuthOptions(): Promise<NextAuthOptions> {
  if (authOptionsCache) {
    return authOptionsCache
  }
  
  authOptionsCache = await createAuthOptions()
  return authOptionsCache
}

// Create NextAuth handler function
export async function createAuthHandler() {
  const authOptions = await getAuthOptions()
  return NextAuth(authOptions)
}
