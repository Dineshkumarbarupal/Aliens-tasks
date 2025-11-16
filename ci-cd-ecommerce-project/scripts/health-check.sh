#!/bin/bash

# Health check script

URL="http://localhost"
MAX_ATTEMPTS=30
ATTEMPT=1

while [ $ATTEMPT -le $MAX_ATTEMPTS ]; do
    if curl -f $URL > /dev/null 2>&1; then
        echo "✅ Application is healthy"
        exit 0
    fi
    
    echo "⏳ Waiting for application to be healthy... (attempt $ATTEMPT/$MAX_ATTEMPTS)"
    sleep 10
    ATTEMPT=$((ATTEMPT + 1))
done

echo "❌ Application health check failed"
exit 1