import { NextRequest, NextResponse } from "next/server"
import { getAuthSession } from "@/lib/auth-utils"
import { PrismaClient } from "@/generated/prisma"

const prisma = new PrismaClient()

export async function POST(request: NextRequest) {
  try {
    const session = await getAuthSession()
    
    if (!session?.user?.id) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
    }

    const body = await request.json()
    const { certificationId, score, totalQuestions, correctAnswers, points } = body

    const quizAttempt = await prisma.quizAttempt.create({
      data: {
        userId: session.user.id,
        certificationId,
        score,
        totalQuestions,
        correctAnswers,
        points
      }
    })

    return NextResponse.json(quizAttempt)
  } catch (error) {
    console.error("Error saving quiz attempt:", error)
    return NextResponse.json(
      { error: "Failed to save quiz attempt" },
      { status: 500 }
    )
  }
}
