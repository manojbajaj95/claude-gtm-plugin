
## Task 3: content-strategy-and-planning consolidation (2026-03-10)

### Patterns
- `aliases` field triggers validator warning — always fold alias values into description text as trigger keywords
- When merging 3 skills into 1, check body line count first (was 274); added ~134 lines staying at 408 (under 500 cap)
- Reference files from deleted skills are worth migrating if they cover distinct content types (blog, social, PR, AIO deep dive)
- Compact sections (40-50 lines each) from source skills add real value without bloating the file

### Approach that worked
- Edit 1: remove aliases + update description in one targeted frontmatter swap
- Edit 2: extend decision tree + replace Related Skills tail in one edit
- Copy reference files before deleting source dirs (cp then rm -rf)
- `./validate-skills.sh <path>` exits 0 = only valid frontmatter fields present
