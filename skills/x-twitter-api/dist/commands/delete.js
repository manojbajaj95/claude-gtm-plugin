import { parseArgs } from "../lib/args.js";
export async function del(client, args) {
    const { id } = parseArgs(args, {
        positional: { key: "id", label: "A post ID" },
    });
    return client.posts.delete(id);
}
