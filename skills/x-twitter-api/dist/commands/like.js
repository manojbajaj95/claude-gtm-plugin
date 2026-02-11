import { parseArgs } from "../lib/args.js";
import { resolveMyId } from "../lib/resolve.js";
export async function like(client, args) {
    const { tweetId } = parseArgs(args, {
        positional: { key: "tweetId", label: "A tweet ID" },
    });
    const myId = await resolveMyId(client);
    return client.users.likePost(myId, { body: { tweetId } });
}
export async function unlike(client, args) {
    const { tweetId } = parseArgs(args, {
        positional: { key: "tweetId", label: "A tweet ID" },
    });
    const myId = await resolveMyId(client);
    return client.users.unlikePost(myId, tweetId);
}
