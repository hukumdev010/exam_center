#!/bin/bash

# Fix permissions script for dev container
# Run this if you encounter permission issues

set -e

echo "🔧 Fixing dev container permissions..."

# Ensure we're in the correct directory
cd /workspaces/exam_center

# Fix frontend directory permissions
if [ -d "frontend" ]; then
    echo "📁 Fixing frontend directory permissions..."
    
    # Create directories if they don't exist
    sudo mkdir -p frontend/.yarn/cache frontend/node_modules frontend/.next
    
    # Fix ownership
    sudo chown -R node:node frontend/.yarn frontend/node_modules frontend/.next || echo "⚠️ Could not change ownership"
    
    # Fix permissions
    sudo chmod -R 755 frontend/.yarn frontend/node_modules frontend/.next || echo "⚠️ Could not change permissions"
    
    echo "✅ Frontend permissions fixed"
else
    echo "⚠️ Frontend directory not found"
fi

# Fix backend directory permissions if needed
if [ -d "backend" ]; then
    echo "📁 Fixing backend directory permissions..."
    sudo chown -R node:node backend/ || echo "⚠️ Could not change backend ownership"
    echo "✅ Backend permissions fixed"
fi

# Clear yarn cache and reinstall if needed
if [ -d "frontend" ]; then
    echo "🧹 Clearing yarn cache..."
    cd frontend
    yarn cache clean || echo "⚠️ Could not clean yarn cache"
    
    echo "📦 Reinstalling frontend dependencies..."
    yarn install || echo "❌ Failed to install dependencies"
    cd ..
fi

echo "🎉 Permissions fixed! You should now be able to run yarn commands without issues."
echo ""
echo "Quick commands to test:"
echo "  cd frontend && yarn --version"
echo "  cd frontend && yarn dev"