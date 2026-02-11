import { parseArgs, PAGINATION, RAW } from "../lib/args.js";
import { USER_FIELDS } from "../lib/fields.js";
export async function reposters(client, args) {
    const flags = parseArgs(args, {
        positional: { key: "tweetId", label: "A tweet ID" },
        flags: { ...PAGINATION, ...RAW },
    });
    const options = {
        userFields: USER_FIELDS,
        ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
        ...(flags.nextToken !== undefined && { paginationToken: flags.nextToken }),
    };
    const response = await client.posts.getRepostedBy(flags.tweetId, options);
    return flags.raw ? response : (response.data ?? []);
}
