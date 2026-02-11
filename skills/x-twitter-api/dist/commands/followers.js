import { parseArgs, PAGINATION, RAW } from "../lib/args.js";
import { USER_FIELDS } from "../lib/fields.js";
import { resolveUserId } from "../lib/resolve.js";
export async function followers(client, args) {
    const flags = parseArgs(args, {
        positional: { key: "target", label: "A username or user ID" },
        flags: { ...PAGINATION, ...RAW },
    });
    const userId = await resolveUserId(client, flags.target);
    const options = {
        userFields: USER_FIELDS,
        ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
        ...(flags.nextToken !== undefined && { paginationToken: flags.nextToken }),
    };
    const response = await client.users.getFollowers(userId, options);
    return flags.raw ? response : (response.data ?? []);
}
export async function following(client, args) {
    const flags = parseArgs(args, {
        positional: { key: "target", label: "A username or user ID" },
        flags: { ...PAGINATION, ...RAW },
    });
    const userId = await resolveUserId(client, flags.target);
    const options = {
        userFields: USER_FIELDS,
        ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
        ...(flags.nextToken !== undefined && { paginationToken: flags.nextToken }),
    };
    const response = await client.users.getFollowing(userId, options);
    return flags.raw ? response : (response.data ?? []);
}
