import { parseArgs, RAW } from "../lib/args.js";
import { TWEET_FIELDS, TWEET_EXPANSIONS, TWEET_USER_FIELDS } from "../lib/fields.js";
export async function get(client, args) {
    // The positional arg is comma-separated IDs; we parse it as a string then split
    const flags = parseArgs(args, {
        positional: { key: "idsRaw", label: "At least one post ID" },
        flags: {
            ...RAW,
            "--fields": { key: "tweetFields", type: "string[]" },
        },
        defaults: { tweetFields: TWEET_FIELDS },
    });
    const ids = flags.idsRaw.split(",").map((id) => id.trim());
    const options = {
        tweetFields: flags.tweetFields,
        expansions: TWEET_EXPANSIONS,
        userFields: TWEET_USER_FIELDS,
    };
    if (ids.length === 1) {
        const response = await client.posts.getById(ids[0], options);
        return flags.raw ? response : response.data;
    }
    const response = await client.posts.getByIds(ids, options);
    return flags.raw ? response : (response.data ?? []);
}
