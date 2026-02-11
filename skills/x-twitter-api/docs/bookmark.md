Manage bookmarks: add, remove, or list. `bookmark` maps to POST /2/users/:id/bookmarks. `unbookmark` maps to DELETE /2/users/:id/bookmarks/:tweet_id. `bookmarks` maps to GET /2/users/:id/bookmarks. Invoke via `node <base_directory>/x.js bookmark <tweet_id>`, `node <base_directory>/x.js unbookmark <tweet_id>`, or `node <base_directory>/x.js bookmarks [flags]`. Output is JSON to stdout.

[!FLAGS] `bookmark` and `unbookmark` take a tweet ID as the first argument with no additional flags. `bookmarks` accepts: a) `--max-results <1-100>` — set number of results per page. b) `--next-token <token>` — pagination token. c) `--raw` — output the full API response envelope.

[!OUTPUT-SHAPE] `bookmark` returns `{ "data": { "bookmarked": true } }`. `unbookmark` returns `{ "data": { "bookmarked": false } }`. `bookmarks` default produces an array of tweet objects. With `--raw`, wraps into the API envelope with `data`, `includes`, and `meta`.
