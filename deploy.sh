#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   PROJECT_ID=<your-gcp-project-id> ./deploy.sh
# Optional:
#   BACKEND_SERVICE=<backend-service-name> FRONTEND_SERVICE=<frontend-service-name> PROJECT_ID=<your-gcp-project-id> ./deploy.sh

PROJECT_ID="${PROJECT_ID:-your-gcp-project-id}"
REGION="asia-northeast1"

BACKEND_SERVICE="${BACKEND_SERVICE:-edtech-backend}"
FRONTEND_SERVICE="${FRONTEND_SERVICE:-edtech-frontend}"

BACKEND_IMAGE="gcr.io/${PROJECT_ID}/${BACKEND_SERVICE}"
FRONTEND_IMAGE="gcr.io/${PROJECT_ID}/${FRONTEND_SERVICE}"

if [[ "${PROJECT_ID}" == "your-gcp-project-id" ]]; then
  echo "PROJECT_ID が未設定です。例: PROJECT_ID=my-project ./deploy.sh"
  exit 1
fi

gcloud config set project "${PROJECT_ID}"
gcloud auth configure-docker --quiet

echo "[1/4] Build backend image"
gcloud builds submit \
  --tag "${BACKEND_IMAGE}" \
  --file Dockerfile.backend \
  .

echo "[2/4] Deploy backend service"
gcloud run deploy "${BACKEND_SERVICE}" \
  --image "${BACKEND_IMAGE}" \
  --platform managed \
  --region "${REGION}" \
  --port 8080 \
  --allow-unauthenticated

BACKEND_URL="$(gcloud run services describe "${BACKEND_SERVICE}" --region "${REGION}" --format='value(status.url)')"
BACKEND_API_BASE_URL="${BACKEND_URL}/api/v1"

echo "[3/4] Build frontend image"
gcloud builds submit \
  --tag "${FRONTEND_IMAGE}" \
  --file Dockerfile.frontend \
  .

echo "[4/4] Deploy frontend service (session affinity enabled)"
gcloud run deploy "${FRONTEND_SERVICE}" \
  --image "${FRONTEND_IMAGE}" \
  --platform managed \
  --region "${REGION}" \
  --port 8080 \
  --set-env-vars "API_BASE_URL=${BACKEND_API_BASE_URL}" \
  --session-affinity \
  --allow-unauthenticated

FRONTEND_URL="$(gcloud run services describe "${FRONTEND_SERVICE}" --region "${REGION}" --format='value(status.url)')"

echo "Deploy completed."
echo "Backend URL : ${BACKEND_URL}"
echo "Backend API : ${BACKEND_API_BASE_URL}"
echo "Frontend URL: ${FRONTEND_URL}"