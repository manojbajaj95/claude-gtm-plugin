Retrieves one or more posts by ID. Pass a single ID or comma-separated IDs. Maps to GET /2/tweets/:id (single) or GET /2/tweets (multiple, up to 100). Invoke via `node <base_directory>/x.js get <id> [flags]` or `node <base_directory>/x.js get <id1,id2,...> [flags]`. Output is JSON to stdout.

[!FLAGS] a) no flags — returns the post(s) with default tweet fields (text, author_id, created_at, conversation_id, public_metrics) and expands author (name, username). b) `--fields <comma-list>` — override default tweet fields. c) `--raw` — output the full API response envelope (data, includes, errors).

[!OUTPUT-SHAPE] Single ID: produces the post object directly. Multiple IDs: produces an array of post objects. With `--raw`, wraps into the API envelope with `data` and `includes` (expanded users).
