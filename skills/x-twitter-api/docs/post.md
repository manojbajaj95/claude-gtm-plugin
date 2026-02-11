Creates a new post (tweet, reply, or quote tweet). Maps to POST /2/tweets. Invoke via `node <base_directory>/x.js post "<text>" [flags]`. Output is JSON to stdout.

[!FLAGS] a) no flags — creates a standalone tweet with the given text. b) `--reply-to <id>` — makes this post a reply to the specified post ID. c) `--quote <id>` — makes this a quote tweet of the specified post ID. d) `--reply-settings <following|mentionedUsers|subscribers|verified>` — restrict who can reply.

[!THREADS] To create a thread, post the first tweet, capture its ID from the response, then use `--reply-to <id>` for each subsequent tweet in the chain.

[!OUTPUT-SHAPE] Returns the API response with `data` containing the created post's `id` and `text`.
