# Gmail Integration Reference

## Status: ✅ Configured and Ready

The Gmail MCP server (`@gongrzhe/server-gmail-autoauth-mcp`) is configured and authenticated.

**Important:** Gmail MCP server requires Claude Code restart to become available. After restart, you'll have access to Gmail tools.

## Available Gmail Tools

Once Claude Code is restarted, these tools will be available:

- `draft_email` - **Use this for BD emails!** Creates email drafts in Gmail that you can review and send
- `send_email` - Sends emails directly (use with caution)
- `read_email` - Read email content
- `search_emails` - Search using Gmail syntax
- `modify_email` - Add/remove labels, organize
- `list_email_labels` - View all labels
- `create_label` - Create new labels
- `create_filter` - Set up email rules

## Workflow Evolution

### Before Gmail MCP (Manual)
1. Use bd-email skill to draft email content
2. Copy/paste into Gmail manually
3. Review and send from Gmail

### After Gmail MCP (Automated)
1. Use bd-email skill to draft email content
2. Use `draft_email` tool to create draft directly in Gmail
3. Review and send from Gmail interface

## Example Usage

**After Claude Code restart:**

```
User: "Draft BD email to Benjamin Stein using colleague reconnect template"

Claude:
1. Crafts email using bd-email skill principles
2. Calls draft_email tool:
   - to: benjamin@teammates.com
   - subject: Catch up?
   - body: [crafted email with personalization]
3. Confirms: "Draft created in Gmail Drafts folder"
```

## Testing Connection

After restart, verify Gmail MCP is working:

```
User: "List my Gmail labels"
```

If successful, you'll see your Gmail labels. If not, the MCP server may need troubleshooting.

## Configuration Files

- **Claude Config:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Gmail Credentials:** `~/.gmail-mcp/credentials.json`
- **OAuth Keys:** `~/.gmail-mcp/gcp-oauth.keys.json`

## Benefits

- **No copy/paste** - Drafts go directly to Gmail
- **Review before sending** - Drafts never send automatically
- **Maintain Gmail workflow** - Use familiar Gmail interface for final review
- **Track in Gmail** - All drafts appear in Drafts folder
- **Context efficient** - Single tool call vs manual browser workflow

## Troubleshooting

**If Gmail tools aren't available after restart:**

1. Check MCP server is configured:
   ```bash
   cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

2. Verify credentials exist:
   ```bash
   ls -la ~/.gmail-mcp/
   ```

3. Re-authenticate if needed:
   ```bash
   npx @gongrzhe/server-gmail-autoauth-mcp auth
   ```

4. Restart Claude Code again

## Next Steps

1. **Restart Claude Code** to activate Gmail MCP server
2. **Test connection** with "List my Gmail labels"
3. **Draft first BD email** using integrated workflow
