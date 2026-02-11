import type { Client } from "@xdevplatform/xdk";
import { parseArgs, PAGINATION, RAW } from "../lib/args.js";
import { USER_FIELDS } from "../lib/fields.js";

export async function likers(client: Client, args: string[]): Promise<unknown> {
  const flags = parseArgs<{
    tweetId: string;
    maxResults?: number;
    nextToken?: string;
    raw: boolean;
  }>(args, {
    positional: { key: "tweetId", label: "A tweet ID" },
    flags: { ...PAGINATION, ...RAW },
  });

  const options: Record<string, unknown> = {
    userFields: USER_FIELDS,
    ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
    ...(flags.nextToken !== undefined && { paginationToken: flags.nextToken }),
  };

  const response = await client.posts.getLikingUsers(flags.tweetId, options);
  return flags.raw ? response : (response.data ?? []);
}
