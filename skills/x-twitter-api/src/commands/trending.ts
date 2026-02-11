import type { Client } from "@xdevplatform/xdk";
import { parseArgs, RAW } from "../lib/args.js";

export async function trending(
  client: Client,
  args: string[],
): Promise<unknown> {
  const flags = parseArgs<{ personalized: boolean; raw: boolean }>(args, {
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
