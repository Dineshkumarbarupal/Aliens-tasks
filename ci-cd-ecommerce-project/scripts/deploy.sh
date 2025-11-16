#!/bin/bash

# Deployment script for e-commerce app

set -e  # Exit on error

echo "🚀 Starting deployment..."

# Pull latest changes
git pull origin main

# Build and deploy
docker-compose down
docker-compose pull
docker-compose build --no-cache
docker-compose up -d

# Run migrations (if any)
# docker-compose exec web python migrate.py

# Health check
echo "🔍 Performing health check..."
sleep 10
curl -f http://localhost || exit 1

echo "✅ Deployment completed successfully!"