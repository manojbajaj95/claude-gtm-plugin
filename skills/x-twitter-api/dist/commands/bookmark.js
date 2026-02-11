import { parseArgs, PAGINATION, RAW } from "../lib/args.js";
import { TWEET_FIELDS, TWEET_EXPANSIONS, TWEET_USER_FIELDS } from "../lib/fields.js";
import { resolveMyId } from "../lib/resolve.js";
export async function bookmark(client, args) {
    const { tweetId } = parseArgs(args, {
        positional: { key: "tweetId", label: "A tweet ID" },
    });
    const myId = await resolveMyId(client);
    return client.users.createBookmark(myId, { tweetId });
}
export async function unbookmark(client, args) {
    const { tweetId } = parseArgs(args, {
        positional: { key: "tweetId", label: "A tweet ID" },
    });
    const myId = await resolveMyId(client);
    return client.users.deleteBookmark(myId, tweetId);
}
export async function bookmarks(client, args) {
    const flags = parseArgs(args, { flags: { ...PAGINATION, ...RAW } });
    const myId = await resolveMyId(client);
    const options = {
        tweetFields: TWEET_FIELDS,
        expansions: TWEET_EXPANSIONS,
        userFields: TWEET_USER_FIELDS,
        ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
        ...(flags.nextToken !== undefined && { paginationToken: flags.nextToken }),
    };
    const response = await client.users.getBookmarks(myId, options);
    return flags.raw ? response : (response.data ?? []);
}
