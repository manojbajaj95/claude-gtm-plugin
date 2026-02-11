import { parseArgs, PAGINATION, RAW } from "../lib/args.js";
import { TWEET_FIELDS, TWEET_EXPANSIONS, TWEET_USER_FIELDS } from "../lib/fields.js";
export async function quotes(client, args) {
    const flags = parseArgs(args, {
        positional: { key: "tweetId", label: "A tweet ID" },
        flags: { ...PAGINATION, ...RAW },
    });
    const options = {
        tweetFields: TWEET_FIELDS,
        expansions: TWEET_EXPANSIONS,
        userFields: TWEET_USER_FIELDS,
        ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
        ...(flags.nextToken !== undefined && { paginationToken: flags.nextToken }),
    };
    const response = await client.posts.getQuoted(flags.tweetId, options);
    return flags.raw ? response : (response.data ?? []);
}
