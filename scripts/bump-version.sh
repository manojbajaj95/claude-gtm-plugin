#!/bin/bash
#
# Bump version across all plugin manifests.
#
# Usage:
#   ./scripts/bump-version.sh major    # 1.3.0 → 2.0.0
#   ./scripts/bump-version.sh minor    # 1.3.0 → 1.4.0
#   ./scripts/bump-version.sh patch    # 1.3.0 → 1.3.1
#   ./scripts/bump-version.sh 2.1.0    # explicit version
#
# Updates:
#   - .claude-plugin/plugin.json (root)
#   - plugins/*/.claude-plugin/plugin.json (all sub-plugins)
#
# Skips third-party plugin.json files (those not under .claude-plugin/).

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

PLUGIN_FILES=()
PLUGIN_FILES+=("$ROOT_MANIFEST")
for dir in "$PROJECT_ROOT"/plugins/*/.claude-plugin; do
    if [ -f "$dir/plugin.json" ]; then
        PLUGIN_FILES+=("$dir/plugin.json")
    fi
done

echo "Bumping v${CURRENT_VERSION} → v${NEW_VERSION} across ${#PLUGIN_FILES[@]} manifests..."
echo ""

for file in "${PLUGIN_FILES[@]}"; do
    rel_path="${file#$PROJECT_ROOT/}"
    old_version=$(grep -o '"version": "[^"]*"' "$file" | head -1 | sed 's/"version": "//;s/"//')
    sed -i "s/\"version\": \"${old_version}\"/\"version\": \"${NEW_VERSION}\"/" "$file"
    echo "  ${rel_path}: ${old_version} → ${NEW_VERSION}"
done

echo ""
echo "Done. All ${#PLUGIN_FILES[@]} manifests at v${NEW_VERSION}."
