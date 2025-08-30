import { PrismaClient } from '../../../src/generated/prisma'
import { seedAwsCloudPractitioner } from './cloud-practitioner'
import { seedAwsSolutionsArchitectAssociate } from './solutions-architect-associate'
import { seedAwsDeveloperAssociate } from './developer-associate'
import { seedAwsSolutionsArchitectProfessional } from './solutions-architect-professional'
import { seedAwsSecuritySpecialty } from './security-specialty'

export async function seedAwsCertifications(prisma: PrismaClient, categoryId: number) {
  console.log('🌱 Seeding comprehensive AWS certifications with detailed questions and reference links...')
  
  // Seed all AWS certifications with comprehensive questions and detailed explanations
  const awsCloudPractitioner = await seedAwsCloudPractitioner(prisma, categoryId)
  const awsSolutionsArchitectAssociate = await seedAwsSolutionsArchitectAssociate(prisma, categoryId)
  const awsDeveloperAssociate = await seedAwsDeveloperAssociate(prisma, categoryId)
  const awsSolutionsArchitectProfessional = await seedAwsSolutionsArchitectProfessional(prisma, categoryId)
  const awsSecuritySpecialty = await seedAwsSecuritySpecialty(prisma, categoryId)
  
  console.log('✅ AWS certifications seeded successfully with comprehensive content!')
  
  // Return all certifications for compatibility
  return {
    awsCloudPractitioner,
    awsSolutionsArchitectAssociate,
    awsDeveloperAssociate,
    awsSolutionsArchitectProfessional,
    awsSecuritySpecialty
  }
}

// Re-export individual certification seeders for flexibility
export { 
  seedAwsCloudPractitioner,
  seedAwsSolutionsArchitectAssociate,
  seedAwsDeveloperAssociate,
  seedAwsSolutionsArchitectProfessional,
  seedAwsSecuritySpecialty
}
