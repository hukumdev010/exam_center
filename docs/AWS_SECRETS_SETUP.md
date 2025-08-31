# AWS Secrets Manager Setup

This application is configured to use AWS Secrets Manager with a static secret name `examCenterCredentials` to manage environment variables securely.

## Secret Configuration

Create a secret in AWS Secrets Manager with the name `examCenterCredentials` and the following JSON structure:

```json
{
  "GOOGLE_CLIENT_ID": "your-google-oauth-client-id",
  "GOOGLE_CLIENT_SECRET": "your-google-oauth-client-secret",
  "NEXTAUTH_SECRET": "your-nextauth-secret-at-least-32-characters-long",
  "DATABASE_URL": "your-postgresql-connection-string",
  "NODE_ENV": "production"
}
```

## AWS Configuration

Make sure your environment has the following AWS configuration:

1. **AWS Region**: Set `AWS_REGION` environment variable (defaults to `us-east-1`)
2. **AWS Credentials**: Ensure your application has access to AWS Secrets Manager through:
   - IAM roles (recommended for EC2/ECS)
   - AWS credentials file
   - Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)

## Required IAM Permissions

Your application needs the following IAM permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": "arn:aws:secretsmanager:*:*:secret:examCenterCredentials*"
    }
  ]
}
```

## Local Development

For local development, you can either:

1. Use AWS credentials configured locally and the actual AWS secret
2. Set the environment variables directly in your `.env` file as fallback

The application will first try to load from AWS Secrets Manager, then fall back to process.env variables.

## Environment Variables

The following environment variables are loaded from the `examCenterCredentials` secret:

- `GOOGLE_CLIENT_ID`: Google OAuth 2.0 client ID
- `GOOGLE_CLIENT_SECRET`: Google OAuth 2.0 client secret  
- `NEXTAUTH_SECRET`: NextAuth.js secret for JWT signing (minimum 32 characters)
- `DATABASE_URL`: PostgreSQL connection string
- `NODE_ENV`: Application environment (development/production/test)

## Cache Behavior

- Secrets are cached for 5 minutes to reduce AWS API calls
- Environment configuration is cached for the application lifetime
- Clear cache by restarting the application
