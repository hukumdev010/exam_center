import { PrismaClient } from './src/generated/prisma'

const prisma = new PrismaClient()

async function main() {
  console.log('🔍 Checking database contents...\n')
  
  // Check categories
  const categories = await prisma.category.findMany()
  console.log(`📚 Categories found: ${categories.length}`)
  categories.forEach(cat => console.log(`  - ${cat.name} (${cat.slug})`))
  
  // Check certifications
  const certifications = await prisma.certification.findMany({
    include: {
      category: true,
      _count: {
        select: { questions: true }
      }
    }
  })
  console.log(`\n🎯 Certifications found: ${certifications.length}`)
  certifications.forEach(cert => {
    console.log(`  - ${cert.name} (${cert.category.name}) - ${cert._count.questions} questions`)
  })
  
  // Check total questions
  const totalQuestions = await prisma.question.count()
  console.log(`\n❓ Total questions: ${totalQuestions}`)
  
  // Check some sample questions
  const sampleQuestions = await prisma.question.findMany({
    take: 3,
    include: {
      certification: true
    }
  })
  
  console.log('\n📝 Sample questions:')
  sampleQuestions.forEach((q: any, index: any) => {
    console.log(`  ${index + 1}. ${q.text.substring(0, 100)}... (${q.certification.name})`)
  })
}

main()
  .catch(console.error)
  .finally(() => prisma.$disconnect())
