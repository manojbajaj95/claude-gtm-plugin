#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ALL_SKILLS_FILE="$PROJECT_ROOT/ALL_SKILLS.md"
README_FILE="$PROJECT_ROOT/README.md"

declare -A CATEGORY_NAMES=(
    ["ads"]="Ads & Paid"
    ["analytics"]="Analytics & Data"
    ["content"]="Content & Copywriting"
    ["crm"]="CRM & Automation"
    ["growth"]="Growth & Conversion"
    ["outbound"]="Email & Outbound"
    ["sales"]="Sales"
    ["seo"]="SEO & AI Search"
    ["social"]="Social Media"
    ["strategy"]="Strategy & Positioning"
)

extract_frontmatter_field() {
    local file="$1"
    local field="$2"
    if [ -f "$file" ]; then
        grep "^${field}:" "$file" | head -1 \
            | sed "s/^${field}: *//" \
            | sed 's/^"//' | sed 's/"$//' \
            | sed "s/^'//" | sed "s/'$//"
    fi
}

echo "Generating skills list from plugins/..."

categories=($(ls -d "$PROJECT_ROOT/plugins"/*/ 2>/dev/null | xargs -n1 basename | sort))

declare -A category_skills
declare -A category_descriptions
total_skills=0

for category in "${categories[@]}"; do
    skills=()
    category_path="$PROJECT_ROOT/plugins/$category/skills"

    if [ -d "$category_path" ]; then
        for skill_dir in $(ls -d "$category_path"/*/ 2>/dev/null | sort); do
            skill_file="${skill_dir}SKILL.md"
            if [ -f "$skill_file" ]; then
                skill_name=$(extract_frontmatter_field "$skill_file" "name")
                if [ -n "$skill_name" ]; then
                    skills+=("$skill_name")
                    ((total_skills++))
                fi
            fi
        done
    fi

    category_skills[$category]="${skills[*]}"
done

generate_all_skills_md() {
    echo "# All Skills"
    echo ""
    echo "Total: **$total_skills skills** across **${#categories[@]} categories**"
    echo ""

    for category in "${categories[@]}"; do
        display_name="${CATEGORY_NAMES[$category]:-$category}"
        skills_list=(${category_skills[$category]})
        skill_count="${#skills_list[@]}"

        echo "## $display_name ($skill_count)"
        echo ""
        echo "\`\`\`"
        echo "plugins/$category/skills/"

        last_idx=$((skill_count - 1))
        for i in "${!skills_list[@]}"; do
            skill="${skills_list[$i]}"
            if [ "$i" -lt "$last_idx" ]; then
                echo "├── $skill"
            else
                echo "└── $skill"
            fi
        done
        echo "\`\`\`"
        echo ""
    done
}

generate_readme_skills_section() {
    echo "## Skills"
    echo ""

    for category in "${categories[@]}"; do
        display_name="${CATEGORY_NAMES[$category]:-$category}"
        skills_list=(${category_skills[$category]})
        skill_count="${#skills_list[@]}"

        echo "### $display_name ($skill_count)"
        echo ""

        last_idx=$((skill_count - 1))
        for i in "${!skills_list[@]}"; do
            skill="${skills_list[$i]}"
            if [ "$i" -lt "$last_idx" ]; then
                echo "├── \`$skill\`"
            else
                echo "└── \`$skill\`"
            fi
        done
        echo ""
    done
}

generate_all_skills_md > "$ALL_SKILLS_FILE"
echo "Created $ALL_SKILLS_FILE"

if [ -f "$README_FILE" ]; then
    SKILLS_CONTENT=$(generate_readme_skills_section)

    python3 - "$README_FILE" << PYTHON_SCRIPT
import sys

readme_file = sys.argv[1]
new_section = """$SKILLS_CONTENT"""

with open(readme_file, 'r') as f:
    content = f.read()

start_marker = "\n## Skills\n"
end_marker = "\n## Routing Rules"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + "\n" + new_section + "\n\n## Routing Rules" + content[end_idx + len(end_marker):]
    with open(readme_file, 'w') as f:
        f.write(new_content)
    print("Updated README.md")
else:
    print(f"Warning: markers not found (## Skills: {start_idx != -1}, ## Routing Rules: {end_idx != -1})")
PYTHON_SCRIPT
fi

echo "Done! $total_skills skills across ${#categories[@]} categories"
