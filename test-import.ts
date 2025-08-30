try {
  const mod = require('./prisma/seeds/aws/cloud-practitioner.ts')
  console.log('cloud-practitioner exports:', Object.keys(mod))
  console.log('seedAwsCloudPractitioner:', typeof mod.seedAwsCloudPractitioner)
} catch (e) {
  console.error('Error loading cloud-practitioner:', e.message)
}

try {
  const mod = require('./prisma/seeds/aws/index.ts')
  console.log('index exports:', Object.keys(mod))
  console.log('seedAwsCertifications:', typeof mod.seedAwsCertifications)
} catch (e) {
  console.error('Error loading index:', e.message)
}
