import NextAuth, { NextAuthOptions } from "next-auth"
import GoogleProvider from "next-auth/providers/google"
import { PrismaAdapter } from "@auth/prisma-adapter"
import { PrismaClient } from "@/generated/prisma"
import { getRequiredEnv } from "./env"

const prisma = new PrismaClient()

// Create auth options with validated environment configuration
export const authOptions: NextAuthOptions = {
  adapter: PrismaAdapter(prisma),
  providers: [
    GoogleProvider({
      clientId: getRequiredEnv('GOOGLE_CLIENT_ID'),
      clientSecret: getRequiredEnv('GOOGLE_CLIENT_SECRET'),
    }),
  ],
  secret: getRequiredEnv('NEXTAUTH_SECRET'),
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

// Export NextAuth handler
export default NextAuth(authOptions)
