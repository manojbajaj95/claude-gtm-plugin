Repost (retweet) or unrepost a post. `repost` maps to POST /2/users/:id/retweets. `unrepost` maps to DELETE /2/users/:id/retweets/:tweet_id. Invoke via `node <base_directory>/x.js repost <tweet_id>` or `node <base_directory>/x.js unrepost <tweet_id>`. Output is JSON to stdout.

[!FLAGS] No flags. Both commands take a single tweet ID as the first argument.

[!OUTPUT-SHAPE] `repost` returns `{ "data": { "retweeted": true } }`. `unrepost` returns `{ "data": { "retweeted": false } }`.
