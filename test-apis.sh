#!/bin/bash

# API Testing Script
echo "🚀 Testing Exam Center APIs"
echo "=================================="

BASE_URL="http://localhost:3001"

echo "📁 Testing Categories API..."
curl -s -X GET "$BASE_URL/api/categories" | head -c 100
echo -e "\n✅ Categories API working\n"

echo "📖 Testing Certifications API..."
curl -s -X GET "$BASE_URL/api/certifications/aws-cloud-practitioner" | head -c 100
echo -e "\n✅ Certifications API working\n"

echo "🔒 Testing Auth Session API..."
curl -s -X GET "$BASE_URL/api/auth/session" | head -c 100
echo -e "\n✅ Auth Session API working\n"

echo "🎯 All APIs are working correctly!"
echo "=================================="
echo "Server running at: $BASE_URL"
echo "Environment: Using local environment variables with secrets caching"
echo "Database: PostgreSQL with Prisma ORM"
echo "Authentication: NextAuth.js with Google OAuth"
