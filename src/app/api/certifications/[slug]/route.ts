import { NextResponse } from 'next/server';
import { PrismaClient } from '@/generated/prisma';

const prisma = new PrismaClient();

export async function GET(
  request: Request,
  { params }: { params: Promise<{ slug: string }> }
) {
  try {
    const { slug } = await params;
    const certification = await prisma.certification.findFirst({
      where: {
        slug: slug,
        isActive: true
      },
      include: {
        questions: {
          include: {
            answers: true
          },
          orderBy: {
            id: 'asc'
          }
        },
        category: true
      }
    });

    if (!certification) {
      return NextResponse.json(
        { error: 'Certification not found' },
        { status: 404 }
      );
    }

    return NextResponse.json(certification);
  } catch (error) {
    console.error('Error fetching certification:', error);
    return NextResponse.json(
      { error: 'Failed to fetch certification' },
      { status: 500 }
    );
  } finally {
    await prisma.$disconnect();
  }
}
