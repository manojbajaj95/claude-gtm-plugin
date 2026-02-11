import { parseArgs, RAW } from "../lib/args.js";
import { USER_FIELDS_EXTENDED } from "../lib/fields.js";
export async function me(client, args) {
    const flags = parseArgs(args, {
        flags: {
            ...RAW,
            "--fields": { key: "fields", type: "string[]" },
            "--pinned-tweet": { key: "pinnedTweet", type: "boolean" },
        },
        defaults: { fields: USER_FIELDS_EXTENDED },
    });
    const options = {
        userFields: flags.fields,
    };
    if (flags.pinnedTweet) {
        options.expansions = ["pinned_tweet_id"];
        options.tweetFields = ["created_at", "text", "public_metrics"];
    }
    const response = await client.users.getMe(options);
    if (flags.raw || flags.pinnedTweet) {
        return response;
    }
    return response.data;
}
