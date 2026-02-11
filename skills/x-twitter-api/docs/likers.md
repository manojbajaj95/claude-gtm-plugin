Lists users who liked a specific post. Maps to GET /2/tweets/:id/liking_users. Invoke via `node <base_directory>/x.js likers <tweet_id> [flags]`. Output is JSON to stdout.

[!FLAGS] a) no flags — returns users who liked the post with default profile fields. b) `--max-results <1-100>` — set number of results per page. c) `--next-token <token>` — pagination token from a previous response. d) `--raw` — output the full API response envelope.

[!OUTPUT-SHAPE] Default produces an array of user objects. With `--raw`, wraps into the API envelope with `data` and `meta` (next_token for pagination).
