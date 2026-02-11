Look up one or more users by username or ID. Auto-detects input type: username (string), user ID (all digits), or comma-separated IDs (for batch lookup). Maps to GET /2/users/by/username/:username, GET /2/users/:id, or GET /2/users. Invoke via `node <base_directory>/x.js user <username|id|id1,id2,...> [flags]`. Output is JSON to stdout.

[!FLAGS] a) no flags — returns user profile with default fields (identity, bio, metrics, location, verification, avatar, dates). b) `--raw` — outputs the full API response envelope.

[!OUTPUT-SHAPE] Single user: produces the user object directly. Multiple IDs: produces an array of user objects. With `--raw`, wraps into the API envelope with `data` and `includes`.
