import { parseArgs } from "../lib/args.js";
export async function hideReply(client, args) {
    const { tweetId } = parseArgs(args, {
        positional: { key: "tweetId", label: "A tweet ID" },
    });
    return client.posts.hideReply(tweetId, { body: { hidden: true } });
}
