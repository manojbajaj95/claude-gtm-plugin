import { parseArgs } from "../lib/args.js";
import { resolveMyId, resolveUserId } from "../lib/resolve.js";
export async function follow(client, args) {
    const { target } = parseArgs(args, {
        positional: { key: "target", label: "A username or user ID" },
    });
    const myId = await resolveMyId(client);
    const targetUserId = await resolveUserId(client, target);
    return client.users.followUser(myId, { body: { targetUserId } });
}
export async function unfollow(client, args) {
    const { target } = parseArgs(args, {
        positional: { key: "target", label: "A username or user ID" },
    });
    const myId = await resolveMyId(client);
    const targetUserId = await resolveUserId(client, target);
    return client.users.unfollowUser(myId, targetUserId);
}
