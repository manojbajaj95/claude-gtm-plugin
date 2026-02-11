Deletes a post owned by the authenticated user. Maps to DELETE /2/tweets/:id. Invoke via `node <base_directory>/x.js delete <id>`. Output is JSON to stdout.

[!OUTPUT-SHAPE] Returns `{ "data": { "deleted": true } }` on success.
