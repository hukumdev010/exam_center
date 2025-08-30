import { PrismaClient } from '../src/generated/prisma'
import { seedJavaScript } from './seeds/javascript'
import { seedTypeScript } from './seeds/typescript'
import { seedNodeJS } from './seeds/nodejs'
import { seedPython } from './seeds/python'
import { seedReact } from './seeds/react'
import { seedDSA } from './seeds/dsa'
import { seedAwsCertifications } from './seeds/aws'
import { seedDevOps } from './seeds/devops'
import { seedSystemsCertifications } from './seeds/systems'
import { seedWebHacking } from './seeds/webhacking'

const prisma = new PrismaClient()

async function main() {
  console.log('🌱 Starting database seed...')

  // Clear existing data for clean seeding
  console.log('🗑️ Clearing existing data...')
  await prisma.answer.deleteMany({})
  await prisma.question.deleteMany({})
  await prisma.quizAttempt.deleteMany({})
  await prisma.userProgress.deleteMany({})
  await prisma.certification.deleteMany({})
  await prisma.category.deleteMany({})
  console.log('✅ Database cleared successfully!')

  // Create Categories
  console.log('📚 Creating categories...')
  const awsCategory = await prisma.category.create({
    data: {
      name: 'Amazon Web Services (AWS)',
      description: 'Cloud computing certifications from AWS',
      slug: 'aws',
      icon: 'aws',
      color: 'orange'
    },
  })

  const devCategory = await prisma.category.create({
    data: {
      name: 'Software Development',
      description: 'Programming languages and development frameworks',
      slug: 'development',
      icon: 'code',
      color: 'blue'
    },
  })

  const devopsCategory = await prisma.category.create({
    data: {
      name: 'DevOps & Infrastructure',
      description: 'DevOps practices, container orchestration, and infrastructure management',
      slug: 'devops',
      icon: 'server',
      color: 'purple'
    },
  })

  const systemsCategory = await prisma.category.create({
    data: {
      name: 'System Administration',
      description: 'Operating systems, networking, and system administration',
      slug: 'systems',
      icon: 'terminal',
      color: 'green'
    },
  })

  // Seed Development Certifications
  console.log('💻 Seeding development certifications...')
  const javascript = await seedJavaScript(prisma, devCategory.id)
  const typescript = await seedTypeScript(prisma, devCategory.id)
  const nodejs = await seedNodeJS(prisma, devCategory.id)
  const python = await seedPython(prisma, devCategory.id)
  const react = await seedReact(prisma, devCategory.id)
  const dsa = await seedDSA(prisma, devCategory.id)

  // Seed AWS Certifications
  console.log('☁️ Seeding AWS certifications...')
  const awsCerts = await seedAwsCertifications(prisma, awsCategory.id)

  // Seed DevOps Certifications
  console.log('🔧 Seeding DevOps certifications...')
  const devopsCerts = await seedDevOps(prisma)

  // Seed Systems Certifications
  console.log('🖥️ Seeding systems certifications...')
  const systemsCerts = await seedSystemsCertifications(prisma, systemsCategory.id)
  const webHacking = await seedWebHacking(prisma, systemsCategory.id)

  console.log('\n✅ Database has been seeded successfully!')
  console.log('\n📚 Categories created:')
  console.log(`- ${awsCategory.name}`)
  console.log(`- ${devCategory.name}`)
  console.log(`- ${devopsCategory.name}`)
  console.log(`- ${systemsCategory.name}`)
  
  console.log('\n🎯 Certifications created:')
  console.log('\nDevelopment:')
  console.log(`- ${javascript.name}`)
  console.log(`- ${typescript.name}`)
  console.log(`- ${nodejs.name}`)
  console.log(`- ${python.name}`)
  console.log(`- ${react.name}`)
  console.log(`- ${dsa.name}`)
  
  console.log('\nAWS:')
  console.log(`- ${awsCerts.awsCloudPractitioner.name}`)
  console.log(`- ${awsCerts.awsSolutionsArchitectAssociate.name}`)
  console.log(`- ${awsCerts.awsDeveloperAssociate.name}`)
  console.log(`- ${awsCerts.awsSolutionsArchitectProfessional.name}`)
  console.log(`- ${awsCerts.awsSecuritySpecialty.name}`)
  
  console.log('\nDevOps:')
  devopsCerts.forEach(cert => console.log(`- ${cert.name}`))
  
  console.log('\nSystems:')
  console.log(`- ${systemsCerts.linuxFundamentals.name}`)
  console.log(`- ${systemsCerts.networkingFundamentals.name}`)
  console.log(`- ${systemsCerts.systemDesign.name}`)
  console.log(`- ${webHacking.name}`)
}

main()
  .then(async () => {
    await prisma.$disconnect()
  })
  .catch(async (e) => {
    console.error(e)
    await prisma.$disconnect()
    process.exit(1)
  })
