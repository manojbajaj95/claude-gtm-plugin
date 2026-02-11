import { parseArgs, PAGINATION, RAW } from "../lib/args.js";
import { USER_FIELDS } from "../lib/fields.js";
import { resolveMyId } from "../lib/resolve.js";
export async function blocked(client, args) {
    const flags = parseArgs(args, { flags: { ...PAGINATION, ...RAW } });
    const myId = await resolveMyId(client);
    const options = {
        userFields: USER_FIELDS,
        ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
        ...(flags.nextToken !== undefined && { paginationToken: flags.nextToken }),
    };
    const response = await client.users.getBlocking(myId, options);
    return flags.raw ? response : (response.data ?? []);
}
