import { getAuthOptions } from "@/lib/auth"
import { NextRequest } from "next/server"
import NextAuth from "next-auth"

// Create dynamic handlers that use async auth options
async function createHandler() {
  const authOptions = await getAuthOptions()
  const handler = NextAuth(authOptions)
  return handler
}

export async function GET(req: NextRequest) {
  const handler = await createHandler()
  return handler(req)
}

export async function POST(req: NextRequest) {
  const handler = await createHandler()
  return handler(req)
}
