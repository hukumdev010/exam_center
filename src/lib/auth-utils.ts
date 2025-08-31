import { getServerSession } from "next-auth"
import { authOptions } from "@/lib/auth"

export async function getAuthSession() {
  return await getServerSession(authOptions)
}
