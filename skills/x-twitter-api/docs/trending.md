Retrieves trending topics. By default returns worldwide trends (WOEID 1). Maps to GET /2/trends/by/woeid/:woeid or GET /2/trends/personalized. Invoke via `node <base_directory>/x.js trending [flags]`. Output is JSON to stdout.

[!FLAGS] a) no flags — returns worldwide trending topics. b) `--personalized` — returns personalized trends for the authenticated user instead. c) `--raw` — output the full API response envelope.

[!OUTPUT-SHAPE] Default produces an array of trend objects. With `--raw`, wraps into the full API response envelope.
