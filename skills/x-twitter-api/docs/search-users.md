Searches users matching a query. Maps to GET /2/users/search. Invoke via `node <base_directory>/x.js search-users "<query>" [flags]`. Output is JSON to stdout.

[!FLAGS] a) no flags — returns up to 10 matching users with default profile fields (name, username, bio, metrics, avatar, verification). b) `--max-results <1-100>` — set number of results per page. c) `--next-token <token>` — pagination token from a previous response. d) `--raw` — output the full API response envelope.

[!OUTPUT-SHAPE] Default produces an array of user objects. With `--raw`, wraps into the API envelope with `data` and `meta` (next_token for pagination).
