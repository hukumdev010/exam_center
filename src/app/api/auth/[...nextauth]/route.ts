import { createAuthHandler } from "@/lib/auth"

// Get the auth handler
const handler = await createAuthHandler()

export { handler as GET, handler as POST }
