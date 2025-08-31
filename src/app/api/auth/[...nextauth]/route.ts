import { getAuthOptions } from "@/lib/auth"
import NextAuth from "next-auth"

// Create the handler with async auth options
const handler = async (req: Request, context: { params: { nextauth: string[] } }) => {
  const authOptions = await getAuthOptions()
  const authHandler = NextAuth(authOptions)
  return authHandler(req, context)
}

export { handler as GET, handler as POST }
