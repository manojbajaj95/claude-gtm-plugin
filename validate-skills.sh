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

    # ── 7. Security: remote code execution (curl/wget piped to shell) ────────
    if grep -qE 'curl\s.*\|\s*(ba)?sh' "$skill_file" || grep -qE 'wget\s.*\|\s*(ba)?sh' "$skill_file"; then
        errors+=("E005: Suspicious download URL — curl/wget piped to shell (remote code execution risk)")
    fi

    # ── 8. Security: third-party package manager commands ─────────────────────
    if grep -qE '^\s*(pip|pip3) install' "$skill_file"; then
        warnings+=("W011: Third-party dependency — 'pip install' command detected")
    fi
    if grep -qE '^\s*npm install|^\s*npm i ' "$skill_file"; then
        warnings+=("W011: Third-party dependency — 'npm install' command detected")
    fi
    if grep -qE 'npx\s' "$skill_file"; then
        warnings+=("W011: Third-party dependency — 'npx' command detected")
    fi
    if grep -qE '^\s*brew install' "$skill_file"; then
        warnings+=("W011: Third-party dependency — 'brew install' command detected")
    fi
    if grep -qE '^\s*(apt-get|apt) install' "$skill_file"; then
        warnings+=("W011: Third-party dependency — 'apt install' command detected")
    fi
    if grep -qE '^\s*gem install' "$skill_file"; then
        warnings+=("W011: Third-party dependency — 'gem install' command detected")
    fi
    if grep -qE '^\s*cargo install' "$skill_file"; then
        warnings+=("W011: Third-party dependency — 'cargo install' command detected")
    fi

    # ── 9. Security: third-party CLI / service dependencies ───────────────────
    if grep -qE 'infsh\s|inference\.sh|cli\.inference\.sh' "$skill_file"; then
        errors+=("Third-party CLI dependency detected (inference.sh) — remove or replace with tool-agnostic guidance")
    fi
    if grep -qE 'canifi\.com|canifi-env' "$skill_file"; then
        errors+=("Third-party CLI dependency detected (canifi.com) — remove or replace with tool-agnostic guidance")
    fi

    # ── 10. Security: credential exposure ─────────────────────────────────────
    # Plaintext password storage instructions
    if grep -qiE 'set\s+\S*(PASSWORD|SECRET)\s+"' "$skill_file"; then
        errors+=("CREDENTIALS_UNSAFE: Plaintext password/secret storage instructions detected")
    fi
    # API keys with real-looking prefixes (Google AIza, AWS AKIA, GitHub ghp_, etc.)
    if grep -qE '(AIzaSy|AKIA[0-9A-Z]|ghp_[a-zA-Z0-9]|sk-[a-zA-Z0-9]{20,}|xox[bpas]-[a-zA-Z0-9])' "$skill_file"; then
        warnings+=("CREDENTIALS_UNSAFE: Possible real API key prefix detected — use 'your-api-key-here' in examples")
    fi

    # ── 11. Security: non-standard secret-handling frontmatter fields ─────────
    if echo "$frontmatter" | grep -qiE '^(vm0_secrets|secrets|credentials):'; then
        errors+=("Non-standard secret-handling field in frontmatter — may expose credentials to unknown systems")
    fi

    # ── 12. Security: overly permissive allowed-tools ─────────────────────────
    allowed_tools=$(extract_field "$frontmatter" "allowed-tools")
    if [[ -n "$allowed_tools" ]]; then
        if echo "$allowed_tools" | grep -qE 'Bash\(\*\)|Bash\(.*\*.*\)'; then
            warnings+=("Broad shell access in allowed-tools: '${allowed_tools}' — consider restricting to specific commands")
        fi
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
