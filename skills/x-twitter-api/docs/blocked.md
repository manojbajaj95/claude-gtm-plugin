Lists accounts blocked by the authenticated user. Maps to GET /2/users/:id/blocking. Invoke via `node <base_directory>/x.js blocked [flags]`. Output is JSON to stdout.

[!FLAGS] a) no flags — returns blocked users with default profile fields (name, username, bio, metrics, avatar, verification). b) `--max-results <1-1000>` — set number of results per page. c) `--next-token <token>` — pagination token from a previous response. d) `--raw` — output the full API response envelope.

[!OUTPUT-SHAPE] Default produces an array of user objects. With `--raw`, wraps into the API envelope with `data` and `meta` (next_token for pagination).
