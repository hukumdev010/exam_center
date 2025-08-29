import { NextRequest, NextResponse } from "next/server"
import { getAuthSession } from "@/lib/auth-utils"
import { PrismaClient } from "@/generated/prisma"

const prisma = new PrismaClient()

export async function GET() {
  try {
    const session = await getAuthSession()
    
    if (!session?.user?.id) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
    }

    const progress = await prisma.userProgress.findMany({
      where: { userId: session.user.id },
      include: {
        certification: {
          include: {
            category: true
          }
        }
      },
      orderBy: { lastActiveAt: "desc" }
    })

    return NextResponse.json(progress)
  } catch (error) {
    console.error("Error fetching user progress:", error)
    return NextResponse.json(
      { error: "Failed to fetch progress" },
      { status: 500 }
    )
  }
}

export async function POST(request: NextRequest) {
  try {
    const session = await getAuthSession()
    
    if (!session?.user?.id) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
    }

    const body = await request.json()
    const { certificationId, currentQuestion, correctAnswers, points, isCompleted } = body

    const certification = await prisma.certification.findUnique({
      where: { id: certificationId },
      include: { questions: true }
    })

    if (!certification) {
      return NextResponse.json({ error: "Certification not found" }, { status: 404 })
    }

    const progress = await prisma.userProgress.upsert({
      where: {
        userId_certificationId: {
          userId: session.user.id,
          certificationId: certificationId
        }
      },
      update: {
        currentQuestion,
        correctAnswers,
        points,
        isCompleted,
        lastActiveAt: new Date()
      },
      create: {
        userId: session.user.id,
        certificationId,
        currentQuestion,
        totalQuestions: certification.questions.length,
        correctAnswers,
        points,
        isCompleted,
        lastActiveAt: new Date()
      }
    })

    return NextResponse.json(progress)
  } catch (error) {
    console.error("Error updating user progress:", error)
    return NextResponse.json(
      { error: "Failed to update progress" },
      { status: 500 }
    )
  }
}
