import { getServerSession } from "next-auth"
import { getAuthOptions } from "@/lib/auth"

export async function getAuthSession() {
  const authOptions = await getAuthOptions()
  return await getServerSession(authOptions)
}
