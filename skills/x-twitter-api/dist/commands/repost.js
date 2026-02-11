import { parseArgs } from "../lib/args.js";
import { resolveMyId } from "../lib/resolve.js";
export async function repost(client, args) {
    const { tweetId } = parseArgs(args, {
        positional: { key: "tweetId", label: "A tweet ID" },
    });
    const myId = await resolveMyId(client);
    return client.users.repostPost(myId, { body: { tweetId } });
}
export async function unrepost(client, args) {
    const { tweetId } = parseArgs(args, {
        positional: { key: "tweetId", label: "A tweet ID" },
    });
    const myId = await resolveMyId(client);
    return client.users.unrepostPost(myId, tweetId);
}
