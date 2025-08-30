import { PrismaClient } from '../../../src/generated/prisma'
import { seedTerraformAssociate } from './terraform-associate'
import { seedKubernetesCKA } from './kubernetes-cka'
import { seedKubernetesCKAD } from './kubernetes-ckad'
import { seedDockerAssociate } from './docker-associate'

export async function seedDevOps(prisma: PrismaClient) {
  console.log('🚀 Starting DevOps certifications seeding...')
  
  // Create or get DevOps category
  const devopsCategory = await prisma.category.upsert({
    where: { slug: 'devops' },
    update: {},
    create: {
      name: 'DevOps & Infrastructure',
      description: 'DevOps practices, containerization, infrastructure as code, and cloud-native technologies for modern software delivery and operations.',
      slug: 'devops',
    },
  })

  // Seed all DevOps certifications
  const results = await Promise.all([
    seedTerraformAssociate(prisma, devopsCategory.id),
    seedKubernetesCKA(prisma, devopsCategory.id),
    seedKubernetesCKAD(prisma, devopsCategory.id),
    seedDockerAssociate(prisma, devopsCategory.id),
  ])

  console.log(`✅ DevOps category seeded successfully with ${results.length} certifications`)
  return results
}

export {
  seedTerraformAssociate,
  seedKubernetesCKA,
  seedKubernetesCKAD,
  seedDockerAssociate,
}
