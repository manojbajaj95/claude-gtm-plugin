Mute or unmute a user, or list muted accounts. Accepts a username or user ID. `mute` maps to POST /2/users/:id/muting. `unmute` maps to DELETE /2/users/:source_id/muting/:target_id. `muted` maps to GET /2/users/:id/muting. Invoke via `node <base_directory>/x.js mute <username|id>`, `node <base_directory>/x.js unmute <username|id>`, or `node <base_directory>/x.js muted [flags]`. Output is JSON to stdout.

[!FLAGS] `mute` and `unmute` take a single username (with or without @) or user ID as the first argument. `muted` accepts: a) `--max-results <1-1000>` — set number of results per page. b) `--next-token <token>` — pagination token. c) `--raw` — output the full API response envelope.

[!OUTPUT-SHAPE] `mute` returns `{ "data": { "muting": true } }`. `unmute` returns `{ "data": { "muting": false } }`. `muted` default produces an array of user objects. With `--raw`, wraps into the API envelope with `data` and `meta`.
