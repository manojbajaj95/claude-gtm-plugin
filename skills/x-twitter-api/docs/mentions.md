Retrieves posts that mention the authenticated user. Maps to GET /2/users/:id/mentions. Invoke via `node <base_directory>/x.js mentions [flags]`. Output is JSON to stdout.

[!FLAGS] a) no flags — returns recent mentions with default tweet fields and expanded authors. b) `--max-results <1-100>` — set number of results per page. c) `--next-token <token>` — pagination token from a previous response. d) `--start-time <ISO8601>` — oldest timestamp (inclusive). e) `--end-time <ISO8601>` — newest timestamp (exclusive). f) `--raw` — output the full API response envelope.

[!OUTPUT-SHAPE] Default produces an array of tweet objects. With `--raw`, wraps into the API envelope with `data`, `includes`, and `meta` (next_token for pagination).
