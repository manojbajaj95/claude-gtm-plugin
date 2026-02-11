import type { Client } from "@xdevplatform/xdk";
import { parseArgs, PAGINATION, RAW } from "../lib/args.js";
import { USER_FIELDS } from "../lib/fields.js";
import { resolveUserId } from "../lib/resolve.js";

export async function followers(
  client: Client,
  args: string[],
): Promise<unknown> {
  const flags = parseArgs<{
    target: string;
    maxResults?: number;
    nextToken?: string;
    raw: boolean;
  }>(args, {
    positional: { key: "target", label: "A username or user ID" },
    flags: { ...PAGINATION, ...RAW },
  });

  const userId = await resolveUserId(client, flags.target);

  const options: Record<string, unknown> = {
    userFields: USER_FIELDS,
    ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
    ...(flags.nextToken !== undefined && { paginationToken: flags.nextToken }),
  };

  const response = await client.users.getFollowers(userId, options);
  return flags.raw ? response : (response.data ?? []);
}

export async function following(
  client: Client,
  args: string[],
): Promise<unknown> {
  const flags = parseArgs<{
    target: string;
    maxResults?: number;
    nextToken?: string;
    raw: boolean;
  }>(args, {
    positional: { key: "target", label: "A username or user ID" },
    flags: { ...PAGINATION, ...RAW },
  });

  const userId = await resolveUserId(client, flags.target);

  const options: Record<string, unknown> = {
    userFields: USER_FIELDS,
    ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
    ...(flags.nextToken !== undefined && { paginationToken: flags.nextToken }),
  };

  const response = await client.users.getFollowing(userId, options);
  return flags.raw ? response : (response.data ?? []);
}
