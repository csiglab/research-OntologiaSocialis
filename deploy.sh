#!/bin/sh
set -eu

IMAGE="ghcr.io/csiglab/sociognosis:latest"
CONTAINER="sociognosis"
PORT="${SOCIOGNOSIS_PORT:-8011}"

cd "$(dirname "$0")"

# Mount the repo's .env into the container (CouchDB credentials etc.).
ENV_MOUNT=""
if [ -f .env ]; then
  ENV_MOUNT="-v ${PWD}/.env:/srv/.env:ro"
fi

docker pull "$IMAGE"
docker rm -f "$CONTAINER" 2>/dev/null || true
# shellcheck disable=SC2086
exec docker run -d --name "$CONTAINER" --restart unless-stopped \
  --network host \
  $ENV_MOUNT \
  "$IMAGE" \
  python bin/sync.py --docs-root /srv/docs --port "$PORT"
