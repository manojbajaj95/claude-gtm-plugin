import { parseArgs, RAW } from "../lib/args.js";
import { USER_FIELDS_EXTENDED } from "../lib/fields.js";
export async function user(client, args) {
    const flags = parseArgs(args, {
        positional: {
            key: "input",
            label: "A username, user ID, or comma-separated list of IDs",
        },
        flags: { ...RAW },
    });
    const input = flags.input.startsWith("@")
        ? flags.input.slice(1)
        : flags.input;
    const options = {
        userFields: USER_FIELDS_EXTENDED,
    };
    // Comma-separated → multiple IDs
    if (input.includes(",")) {
        const ids = input.split(",").map((id) => id.trim());
        const response = await client.users.getByIds(ids, options);
        return flags.raw ? response : (response.data ?? []);
    }
    // All digits → single ID lookup
    if (/^\d+$/.test(input)) {
        const response = await client.users.getById(input, options);
        return flags.raw ? response : response.data;
    }
    // Otherwise → username lookup
    const response = await client.users.getByUsername(input, options);
    return flags.raw ? response : response.data;
}
