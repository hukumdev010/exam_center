import { PrismaClient } from '../src/generated/prisma'
import { seedJavaScript } from './seeds/javascript'
import { seedTypeScript } from './seeds/typescript'
import { seedNodeJS } from './seeds/nodejs'
import { seedPython } from './seeds/python'
import { seedReact } from './seeds/react'
import { seedDSA } from './seeds/dsa'
import { seedAwsCertifications } from './seeds/aws'
import { seedDevOpsCertifications } from './seeds/devops'
import { seedSystemsCertifications } from './seeds/systems'
import { seedWebHacking } from './seeds/webhacking'

const prisma = new PrismaClient()

async function main() {
  console.log('🌱 Starting database seed...')

  // Create Categories
  console.log('📚 Creating categories...')
  const awsCategory = await prisma.category.upsert({
    where: { slug: 'aws' },
    update: {},
    create: {
      name: 'Amazon Web Services (AWS)',
      description: 'Cloud computing certifications from AWS',
      slug: 'aws',
      icon: 'aws',
      color: 'orange'
    },
  })

  const devCategory = await prisma.category.upsert({
    where: { slug: 'development' },
    update: {},
    create: {
      name: 'Software Development',
      description: 'Programming languages and development frameworks',
      slug: 'development',
      icon: 'code',
      color: 'blue'
    },
  })

  const devopsCategory = await prisma.category.upsert({
    where: { slug: 'devops' },
    update: {},
    create: {
      name: 'DevOps & Infrastructure',
      description: 'DevOps practices, container orchestration, and infrastructure management',
      slug: 'devops',
      icon: 'server',
      color: 'purple'
    },
  })

  const systemsCategory = await prisma.category.upsert({
    where: { slug: 'systems' },
    update: {},
    create: {
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
  const devopsCerts = await seedDevOpsCertifications(prisma, devopsCategory.id)

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
  console.log(`- ${devopsCerts.terraformAssociate.name}`)
  console.log(`- ${devopsCerts.cka.name}`)
  console.log(`- ${devopsCerts.ckad.name}`)
  console.log(`- ${devopsCerts.dockerAssociate.name}`)
  
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
