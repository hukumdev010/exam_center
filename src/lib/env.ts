import { z } from "zod"
import { getSecretJson } from "./secrets"

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

// Cache for environment configuration
let envConfigCache: EnvConfig | null = null
const STATIC_SECRET_NAME = "examCenterCredentials"

// Validate environment variables from AWS Secrets Manager
async function validateEnv(): Promise<EnvConfig> {
  try {
    // Get secrets from AWS Secrets Manager using static secret name
    const secrets = await getSecretJson(STATIC_SECRET_NAME)
    
    // Merge with process.env, giving priority to secrets
    const envVars = {
      ...process.env,
      ...secrets,
    }
    
    return envSchema.parse(envVars)
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

// Get environment configuration (async version)
export async function getEnvConfig(): Promise<EnvConfig> {
  if (envConfigCache) {
    return envConfigCache
  }
  
  envConfigCache = await validateEnv()
  return envConfigCache
}

// Simple getters for common environment values (async versions)
export async function getEnv(key: keyof EnvConfig): Promise<string | undefined> {
  const config = await getEnvConfig()
  return config[key] as string | undefined
}

export async function getRequiredEnv(key: keyof EnvConfig): Promise<string> {
  const config = await getEnvConfig()
  const value = config[key] as string
  if (!value) {
    throw new Error(`Required environment variable ${String(key)} is not set`)
  }
  return value
}

// Synchronous fallback functions for backward compatibility (use process.env directly)
export function getEnvSync(key: keyof EnvConfig): string | undefined {
  return process.env[key] as string | undefined
}

export function getRequiredEnvSync(key: keyof EnvConfig): string {
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
