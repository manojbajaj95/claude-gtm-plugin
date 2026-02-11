import { parseArgs, PAGINATION, RAW } from "../lib/args.js";
import { USER_FIELDS } from "../lib/fields.js";
export async function searchUsers(client, args) {
    const flags = parseArgs(args, {
        positional: { key: "query", label: "A search query" },
        flags: { ...PAGINATION, ...RAW },
    });
    const options = {
        userFields: USER_FIELDS,
        ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
        ...(flags.nextToken !== undefined && { nextToken: flags.nextToken }),
    };
    const response = await client.users.search(flags.query, options);
    return flags.raw ? response : (response.data ?? []);
}
