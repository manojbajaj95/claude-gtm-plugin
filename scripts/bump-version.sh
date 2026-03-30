#!/bin/bash
#
# Bump version in the plugin manifest.
#
# Usage:
#   ./scripts/bump-version.sh major    # 1.3.0 → 2.0.0
#   ./scripts/bump-version.sh minor    # 1.3.0 → 1.4.0
#   ./scripts/bump-version.sh patch    # 1.3.0 → 1.3.1
#   ./scripts/bump-version.sh 2.1.0    # explicit version
#
# Updates:
#   - .claude-plugin/plugin.json

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ROOT_MANIFEST="$PROJECT_ROOT/.claude-plugin/plugin.json"

if [ $# -ne 1 ]; then
    echo "Usage: $0 <major|minor|patch|x.y.z>"
    exit 1
fi

CURRENT_VERSION=$(grep -o '"version": "[^"]*"' "$ROOT_MANIFEST" | head -1 | sed 's/"version": "//;s/"//')
IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT_VERSION"

case "$1" in
    major) NEW_VERSION="$((MAJOR + 1)).0.0" ;;
    minor) NEW_VERSION="${MAJOR}.$((MINOR + 1)).0" ;;
    patch) NEW_VERSION="${MAJOR}.${MINOR}.$((PATCH + 1))" ;;
    *)
        if ! echo "$1" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$'; then
            echo "Error: argument must be major, minor, patch, or semver (e.g., 1.2.0)"
            exit 1
        fi
        NEW_VERSION="$1"
        ;;
esac

echo "Bumping v${CURRENT_VERSION} → v${NEW_VERSION}..."
echo ""

rel_path="${ROOT_MANIFEST#$PROJECT_ROOT/}"
sed -i "s/\"version\": \"${CURRENT_VERSION}\"/\"version\": \"${NEW_VERSION}\"/" "$ROOT_MANIFEST"
echo "  ${rel_path}: ${CURRENT_VERSION} → ${NEW_VERSION}"

echo ""
echo "Done. Manifest at v${NEW_VERSION}."
