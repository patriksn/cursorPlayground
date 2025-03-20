#!/bin/bash

# Build the Docker image
echo "Building Docker image..."
docker build -t flask-app .

# Run the container
echo "Starting the container..."
docker run -p 5000:5000 flask-app 