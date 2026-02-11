Like or unlike a post. `like` maps to POST /2/users/:id/likes. `unlike` maps to DELETE /2/users/:id/likes/:tweet_id. Invoke via `node <base_directory>/x.js like <tweet_id>` or `node <base_directory>/x.js unlike <tweet_id>`. Output is JSON to stdout.

[!FLAGS] No flags. Both commands take a single tweet ID as the first argument.

[!OUTPUT-SHAPE] `like` returns `{ "data": { "liked": true } }`. `unlike` returns `{ "data": { "liked": false } }`.
