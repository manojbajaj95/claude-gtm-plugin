#!/bin/bash
#
# Generate a changelog from git commit history.
#
# Usage:
#   ./scripts/generate-changelog.sh                    # full history
#   ./scripts/generate-changelog.sh HEAD~10..HEAD      # last 10 commits
#   ./scripts/generate-changelog.sh v1.0.0..v2.0.0    # between tags
#   ./scripts/generate-changelog.sh --since=2025-01-01 # since date
#   ./scripts/generate-changelog.sh -o CHANGELOG.md    # write to file
#
# Commits are grouped by conventional-commit prefix:
#   feat, fix, docs, refactor, chore, test, perf, ci, style, build
#
# Merge commits and empty messages are excluded.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT"

RANGE=""
SINCE=""
OUTPUT=""

while [ $# -gt 0 ]; do
    case "$1" in
        -o|--output)
            OUTPUT="$2"
            shift 2
            ;;
        --since=*)
            SINCE="${1#--since=}"
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [range] [--since=DATE] [-o FILE]"
            echo ""
            echo "Examples:"
            echo "  $0                          # full history"
            echo "  $0 HEAD~10..HEAD            # last 10 commits"
            echo "  $0 v1.0.0..v2.0.0          # between tags"
            echo "  $0 --since=2025-01-01       # since date"
            echo "  $0 -o CHANGELOG.md          # write to file"
            exit 0
            ;;
        *)
            RANGE="$1"
            shift
            ;;
    esac
done

GIT_ARGS=(log --no-merges --format="%H|%s")

if [ -n "$SINCE" ]; then
    GIT_ARGS+=(--since="$SINCE")
fi

if [ -n "$RANGE" ]; then
    GIT_ARGS+=("$RANGE")
fi

declare -A CATEGORIES
CATEGORIES=(
    [feat]=""
    [fix]=""
    [docs]=""
    [refactor]=""
    [chore]=""
    [test]=""
    [perf]=""
    [ci]=""
    [style]=""
    [build]=""
)
UNCATEGORIZED=""

CATEGORY_LABELS=(
    "feat:🚀 Features"
    "fix:🐛 Bug Fixes"
    "docs:📝 Documentation"
    "refactor:♻️  Refactors"
    "perf:⚡ Performance"
    "test:🧪 Tests"
    "ci:🔧 CI"
    "build:📦 Build"
    "style:🎨 Style"
    "chore:🏠 Chores"
)

declare -A LABEL_MAP
for entry in "${CATEGORY_LABELS[@]}"; do
    key="${entry%%:*}"
    val="${entry#*:}"
    LABEL_MAP[$key]="$val"
done

DISPLAY_ORDER=(feat fix docs refactor perf test ci build style chore)

while IFS='|' read -r hash subject; do
    [ -z "$subject" ] && continue

    if [[ "$subject" =~ ^([a-z]+)(\(.*\))?:\ (.+)$ ]]; then
        prefix="${BASH_REMATCH[1]}"
        msg="${BASH_REMATCH[3]}"
        short_hash="${hash:0:7}"

        msg="$(echo "${msg:0:1}" | tr '[:lower:]' '[:upper:]')${msg:1}"

        line="- ${msg} (\`${short_hash}\`)"

        if [ -n "${CATEGORIES[$prefix]+_}" ]; then
            CATEGORIES[$prefix]+="${line}"$'\n'
        else
            UNCATEGORIZED+="${line}"$'\n'
        fi
    else
        short_hash="${hash:0:7}"
        msg="$(echo "${subject:0:1}" | tr '[:lower:]' '[:upper:]')${subject:1}"
        UNCATEGORIZED+="- ${msg} (\`${short_hash}\`)"$'\n'
    fi
done < <(git "${GIT_ARGS[@]}" 2>/dev/null)

MANIFEST="$PROJECT_ROOT/.claude-plugin/plugin.json"
VERSION=""
if [ -f "$MANIFEST" ]; then
    VERSION=$(grep -o '"version": "[^"]*"' "$MANIFEST" | head -1 | sed 's/"version": "//;s/"//')
fi

generate() {
    local date_str
    date_str=$(date +%Y-%m-%d)

    if [ -n "$VERSION" ]; then
        echo "# Changelog — v${VERSION} (${date_str})"
    else
        echo "# Changelog (${date_str})"
    fi
    echo ""

    if [ -n "$RANGE" ]; then
        echo "> Range: \`${RANGE}\`"
        echo ""
    elif [ -n "$SINCE" ]; then
        echo "> Since: ${SINCE}"
        echo ""
    fi

    local has_content=false

    for cat in "${DISPLAY_ORDER[@]}"; do
        if [ -n "${CATEGORIES[$cat]}" ]; then
            has_content=true
            echo "## ${LABEL_MAP[$cat]}"
            echo ""
            echo -n "${CATEGORIES[$cat]}"
            echo ""
        fi
    done

    if [ -n "$UNCATEGORIZED" ]; then
        has_content=true
        echo "## 📋 Other"
        echo ""
        echo -n "$UNCATEGORIZED"
        echo ""
    fi

    if [ "$has_content" = false ]; then
        echo "_No commits found for the given range._"
        echo ""
    fi
}

if [ -n "$OUTPUT" ]; then
    generate > "$OUTPUT"
    echo "Changelog written to ${OUTPUT}"
else
    generate
fi
