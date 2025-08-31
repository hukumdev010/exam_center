import { z } from "zod"

// Define environment schema with validation
const envSchema = z.object({
  // Google OAuth
  GOOGLE_CLIENT_ID: z.string().min(1, "GOOGLE_CLIENT_ID is required"),
  GOOGLE_CLIENT_SECRET: z.string().min(1, "GOOGLE_CLIENT_SECRET is required"),
  
  // NextAuth
  NEXTAUTH_SECRET: z.string().min(32, "NEXTAUTH_SECRET must be at least 32 characters"),
  
  // Database
  DATABASE_URL: z.string().min(1, "DATABASE_URL is required"),
  
  // Environment
  NODE_ENV: z.enum(["development", "production", "test"]).default("development"),
})

type EnvConfig = z.infer<typeof envSchema>

// Validate environment variables
function validateEnv(): EnvConfig {
  try {
    return envSchema.parse(process.env)
  } catch (error) {
    if (error instanceof z.ZodError) {
      const errorMessages = error.issues.map(issue => 
        `${issue.path.join('.')}: ${issue.message}`
      ).join('\n')
      throw new Error(`Environment validation failed:\n${errorMessages}`)
    }
    throw error
  }
}

// Get environment configuration
export function getEnvConfig(): EnvConfig {
  return validateEnv()
}

// Simple getters for common environment values
export function getEnv(key: keyof EnvConfig): string | undefined {
  return process.env[key] as string | undefined
}

export function getRequiredEnv(key: keyof EnvConfig): string {
  const value = process.env[key] as string
  if (!value) {
    throw new Error(`Required environment variable ${String(key)} is not set`)
  }
  return value
}

export function isDevelopment(): boolean {
  return process.env.NODE_ENV === 'development'
}

export function isProduction(): boolean {
  return process.env.NODE_ENV === 'production'
}
