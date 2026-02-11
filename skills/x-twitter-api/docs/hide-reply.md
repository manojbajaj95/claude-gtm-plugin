Hides a reply to one of your posts. Maps to PUT /2/tweets/:id/hidden. Invoke via `node <base_directory>/x.js hide-reply <tweet_id>`. Output is JSON to stdout.

[!FLAGS] No flags. Takes a single tweet ID as the first argument.

[!OUTPUT-SHAPE] Returns `{ "data": { "hidden": true } }` on success.
