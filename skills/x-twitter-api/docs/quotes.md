Lists quote tweets of a specific post. Maps to GET /2/tweets/:id/quote_tweets. Invoke via `node <base_directory>/x.js quotes <tweet_id> [flags]`. Output is JSON to stdout.

[!FLAGS] a) no flags — returns quote tweets with default tweet fields and expanded authors. b) `--max-results <1-100>` — set number of results per page. c) `--next-token <token>` — pagination token from a previous response. d) `--raw` — output the full API response envelope.

[!OUTPUT-SHAPE] Default produces an array of tweet objects. With `--raw`, wraps into the API envelope with `data`, `includes`, and `meta` (next_token for pagination).
