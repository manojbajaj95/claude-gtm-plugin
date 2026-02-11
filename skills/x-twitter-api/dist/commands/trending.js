import { parseArgs, RAW } from "../lib/args.js";
export async function trending(client, args) {
    const flags = parseArgs(args, {
        flags: {
            ...RAW,
            "--personalized": { key: "personalized", type: "boolean" },
        },
    });
    const response = flags.personalized
        ? await client.trends.getPersonalized()
        : await client.trends.getByWoeid(1);
    return flags.raw ? response : (response.data ?? []);
}
