import { createAuthHandler } from "@/lib/auth"
import { NextRequest } from "next/server"

// Create the handler instance
const handlerPromise = createAuthHandler()

export async function GET(request: NextRequest, context: { params: Record<string, string | string[]> }) {
  const handler = await handlerPromise
  return handler(request, context)
}

export async function POST(request: NextRequest, context: { params: Record<string, string | string[]> }) {
  const handler = await handlerPromise
  return handler(request, context)
}
