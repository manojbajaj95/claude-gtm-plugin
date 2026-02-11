import { parseArgs, PAGINATION, RAW } from "../lib/args.js";
import { USER_FIELDS } from "../lib/fields.js";
import { resolveMyId, resolveUserId } from "../lib/resolve.js";
export async function mute(client, args) {
    const { target } = parseArgs(args, {
        positional: { key: "target", label: "A username or user ID" },
    });
    const myId = await resolveMyId(client);
    const targetUserId = await resolveUserId(client, target);
    return client.users.muteUser(myId, { body: { targetUserId } });
}
export async function unmute(client, args) {
    const { target } = parseArgs(args, {
        positional: { key: "target", label: "A username or user ID" },
    });
    const myId = await resolveMyId(client);
    const targetUserId = await resolveUserId(client, target);
    return client.users.unmuteUser(myId, targetUserId);
}
export async function muted(client, args) {
    const flags = parseArgs(args, { flags: { ...PAGINATION, ...RAW } });
    const myId = await resolveMyId(client);
    const options = {
        userFields: USER_FIELDS,
        ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
        ...(flags.nextToken !== undefined && { paginationToken: flags.nextToken }),
    };
    const response = await client.users.getMuting(myId, options);
    return flags.raw ? response : (response.data ?? []);
}
