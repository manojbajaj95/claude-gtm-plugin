import type { Client } from "@xdevplatform/xdk";
import { parseArgs, PAGINATION, RAW } from "../lib/args.js";
import { USER_FIELDS } from "../lib/fields.js";

export async function searchUsers(
  client: Client,
  args: string[],
): Promise<unknown> {
  const flags = parseArgs<{
    query: string;
    maxResults?: number;
    nextToken?: string;
    raw: boolean;
  }>(args, {
    positional: { key: "query", label: "A search query" },
    flags: { ...PAGINATION, ...RAW },
  });

  const options: Record<string, unknown> = {
    userFields: USER_FIELDS,
    ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
    ...(flags.nextToken !== undefined && { nextToken: flags.nextToken }),
  };

  const response = await client.users.search(flags.query, options);
  return flags.raw ? response : (response.data ?? []);
}
