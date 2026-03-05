#!/bin/bash
# Validates all SKILL.md files against the Agent Skills Specification.
# Reference: https://agentskills.io/specification
# Official validator: https://github.com/agentskills/agentskills/blob/main/skills-ref/src/skills_ref/validator.py

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

PLUGINS_DIR="${1:-plugins}"
ERRORS=0
WARNINGS=0
PASSED=0
TOTAL=0
FAILED_SKILLS=()

ALLOWED_FIELDS="name description license allowed-tools metadata compatibility"

echo ""
echo -e "${BOLD}Validating Skills Against Agent Skills Specification${NC}"
echo "========================================================"
echo "Reference: https://agentskills.io/specification"
echo "Scanning:  ${PLUGINS_DIR}/"
echo ""

extract_frontmatter() {
    awk '/^---$/ { if (++n == 2) exit; next } n == 1 { print }' "$1"
}

extract_field() {
    local frontmatter="$1"
    local field="$2"
    local line

    line=$(echo "$frontmatter" | grep "^${field}:" | head -1) || true
    if [[ -z "$line" ]]; then
        echo ""
        return
    fi

    local value
    value=$(echo "$line" | sed "s/^${field}:[[:space:]]*//" | sed 's/[[:space:]]*$//')

    if [[ "$value" == '"'*'"' ]]; then
        value="${value:1:${#value}-2}"
    elif [[ "$value" == "'"*"'" ]]; then
        value="${value:1:${#value}-2}"
    fi

    echo "$value"
}

extract_description() {
    local frontmatter="$1"

    local desc_line
    desc_line=$(echo "$frontmatter" | grep "^description:" | head -1) || true

    if [[ -z "$desc_line" ]]; then
        echo ""
        return
    fi

    local value
    value=$(echo "$desc_line" | sed 's/^description:[[:space:]]*//' | sed 's/[[:space:]]*$//')

    if [[ "$value" == "|-" || "$value" == "|" || "$value" == ">-" || "$value" == ">" || "$value" == "|+" || "$value" == ">+" ]]; then
        echo "$frontmatter" | awk '
            /^description:/ { found=1; next }
            found && /^[[:space:]]/ {
                sub(/^[[:space:]]+/, "")
                if (result != "") result = result " "
                result = result $0
                next
            }
            found { exit }
            END { print result }
        '
        return
    fi

    if [[ "$value" == '"'*'"' ]]; then
        value="${value:1:${#value}-2}"
    elif [[ "$value" == "'"*"'" ]]; then
        value="${value:1:${#value}-2}"
    fi

    echo "$value"
}

# Extract top-level YAML keys (not indented, not metadata sub-keys)
extract_top_level_keys() {
    local frontmatter="$1"
    echo "$frontmatter" | grep -E "^[a-zA-Z_-]+:" | sed 's/:.*//' | sort -u
}

while IFS= read -r skill_file; do
    TOTAL=$((TOTAL + 1))

    skill_dir=$(dirname "$skill_file")
    dir_name=$(basename "$skill_dir")
    relative_path="${skill_file}"

    errors=()
    warnings=()

    # ── 1. Frontmatter presence ───────────────────────────────────────────────
    dash_count=$(grep -c "^---$" "$skill_file" || true)
    if [[ "$dash_count" -lt 2 ]]; then
        errors+=("Missing YAML frontmatter (need opening and closing --- markers)")
        echo -e "${RED}❌ ${dir_name}${NC}  ${BLUE}${relative_path}${NC}"
        for e in "${errors[@]}"; do echo -e "   ${RED}Error:${NC} $e"; done
        ERRORS=$((ERRORS + 1))
        FAILED_SKILLS+=("$dir_name")
        continue
    fi

    frontmatter=$(extract_frontmatter "$skill_file")

    if [[ -z "$frontmatter" ]]; then
        errors+=("YAML frontmatter is empty (nothing between --- markers)")
        echo -e "${RED}❌ ${dir_name}${NC}  ${BLUE}${relative_path}${NC}"
        for e in "${errors[@]}"; do echo -e "   ${RED}Error:${NC} $e"; done
        ERRORS=$((ERRORS + 1))
        FAILED_SKILLS+=("$dir_name")
        continue
    fi

    # ── 2. Unknown frontmatter fields (official validator rejects these) ──────
    while IFS= read -r key; do
        is_allowed=false
        for allowed in $ALLOWED_FIELDS; do
            if [[ "$key" == "$allowed" ]]; then
                is_allowed=true
                break
            fi
        done
        if [[ "$is_allowed" == false ]]; then
            warnings+=("Unknown frontmatter field: '${key}' (spec allows: name, description, license, allowed-tools, metadata, compatibility)")
        fi
    done < <(extract_top_level_keys "$frontmatter")

    # ── 3. Name validation ────────────────────────────────────────────────────
    name=$(extract_field "$frontmatter" "name")

    if [[ -z "$name" ]]; then
        errors+=("Missing required field: name")
    else
        if [[ "$name" != "$dir_name" ]]; then
            errors+=("Directory name '${dir_name}' must match skill name '${name}'")
        fi

        if [[ "$name" != "$(echo "$name" | tr '[:upper:]' '[:lower:]')" ]]; then
            errors+=("Skill name '${name}' must be lowercase")
        fi

        if [[ "$name" == -* || "$name" == *- ]]; then
            errors+=("Skill name cannot start or end with a hyphen")
        fi

        if [[ "$name" == *--* ]]; then
            errors+=("Skill name cannot contain consecutive hyphens")
        fi

        if [[ "$name" =~ [^a-z0-9-] ]]; then
            bad_chars=$(echo "$name" | sed 's/[a-z0-9-]//g' | fold -w1 | sort -u | tr -d '\n')
            errors+=("Skill name '${name}' contains invalid characters: '${bad_chars}' (only lowercase letters, digits, and hyphens allowed)")
        fi

        if [[ ${#name} -gt 64 ]]; then
            errors+=("Skill name '${name}' exceeds 64 character limit (${#name} chars)")
        fi
    fi

    # ── 4. Description validation ─────────────────────────────────────────────
    description=$(extract_description "$frontmatter")

    if [[ -z "$description" ]]; then
        errors+=("Missing required field: description")
    else
        desc_len=${#description}

        if [[ $desc_len -gt 1024 ]]; then
            errors+=("Description exceeds 1024 character limit (${desc_len} chars)")
        fi

        if ! echo "$description" | grep -qiE "when|use |use$|mention"; then
            warnings+=("Description lacks trigger phrases (should contain 'when', 'use', or 'mention')")
        fi
    fi

    # ── 5. Compatibility validation (if present) ──────────────────────────────
    compat=$(extract_field "$frontmatter" "compatibility")
    if [[ -n "$compat" ]] && [[ ${#compat} -gt 500 ]]; then
        errors+=("Compatibility exceeds 500 character limit (${#compat} chars)")
    fi

    # ── 6. File length (spec recommendation) ──────────────────────────────────
    line_count=$(wc -l < "$skill_file" | tr -d ' ')
    if [[ "$line_count" -gt 500 ]]; then
        warnings+=("SKILL.md is ${line_count} lines (recommended <500; move details to references/)")
    fi

    # ── Report ────────────────────────────────────────────────────────────────
    if [[ ${#errors[@]} -gt 0 ]]; then
        echo -e "${RED}❌ ${dir_name}${NC}  ${BLUE}${relative_path}${NC}"
        for e in "${errors[@]}"; do echo -e "   ${RED}Error:${NC} $e"; done
        for w in "${warnings[@]}"; do echo -e "   ${YELLOW}Warn:${NC}  $w"; done
        ERRORS=$((ERRORS + 1))
        FAILED_SKILLS+=("$dir_name")
    elif [[ ${#warnings[@]} -gt 0 ]]; then
        echo -e "${YELLOW}⚠️  ${dir_name}${NC}  ${BLUE}${relative_path}${NC}"
        for w in "${warnings[@]}"; do echo -e "   ${YELLOW}Warn:${NC}  $w"; done
        WARNINGS=$((WARNINGS + 1))
    else
        echo -e "${GREEN}✓  ${dir_name}${NC}"
        PASSED=$((PASSED + 1))
    fi

done < <(find "$PLUGINS_DIR" -name "SKILL.md" -type f | sort)

echo ""
echo "========================================================"
echo -e "${BOLD}Summary${NC}: ${TOTAL} skills validated"
echo -e "  ${GREEN}✓  Passed:   ${PASSED}${NC}"
if [[ $WARNINGS -gt 0 ]]; then
    echo -e "  ${YELLOW}⚠️  Warnings: ${WARNINGS}${NC}"
fi
if [[ $ERRORS -gt 0 ]]; then
    echo -e "  ${RED}❌ Errors:   ${ERRORS}${NC}"
fi
echo ""

if [[ $ERRORS -gt 0 ]]; then
    echo -e "${RED}Failed skills:${NC}"
    for s in "${FAILED_SKILLS[@]}"; do
        echo -e "  ${RED}-${NC} $s"
    done
    echo ""
    exit 1
else
    echo -e "${GREEN}All skills passed validation!${NC}"
    exit 0
fi
