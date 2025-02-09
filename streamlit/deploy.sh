#!/bin/bash

# Set the project ID (replace with your actual project ID)
gcloud config set project ba882-dhruv

echo "======================================================"
echo "Build (no cache)"
echo "======================================================"

# Build the Docker image with no cache
docker build --no-cache -t gcr.io/ba882-dhruv/streamlit-portfolio .

echo "======================================================"
echo "Push to GCR"
echo "======================================================"

# Push the Docker image to Google Container Registry
docker push gcr.io/ba882-dhruv/streamlit-portfolio

echo "======================================================"
echo "Deploy to Cloud Run"
echo "======================================================"

# Deploy the Docker image to Cloud Run
gcloud run deploy streamlit-portfolio \
    --image gcr.io/ba882-dhruv/streamlit-portfolio \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 1Gi

# Print out the service URL
echo "======================================================"
echo "Deployment Complete! Your app is live at:"
gcloud run services describe streamlit-portfolio --platform managed --region us-central1 --format "value(status.url)"
