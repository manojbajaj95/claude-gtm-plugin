Follow or unfollow a user. Accepts a username or user ID. `follow` maps to POST /2/users/:id/following. `unfollow` maps to DELETE /2/users/:source_id/following/:target_id. Invoke via `node <base_directory>/x.js follow <username|id>` or `node <base_directory>/x.js unfollow <username|id>`. Output is JSON to stdout.

[!FLAGS] No flags. Both commands take a single username (with or without @) or user ID as the first argument.

[!OUTPUT-SHAPE] `follow` returns `{ "data": { "following": true, "pending_follow": false } }`. `unfollow` returns `{ "data": { "following": false } }`.
