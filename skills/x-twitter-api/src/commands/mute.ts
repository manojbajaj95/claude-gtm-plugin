import type { Client } from "@xdevplatform/xdk";
import { parseArgs, PAGINATION, RAW } from "../lib/args.js";
import { USER_FIELDS } from "../lib/fields.js";
import { resolveMyId, resolveUserId } from "../lib/resolve.js";

export async function mute(client: Client, args: string[]): Promise<unknown> {
  const { target } = parseArgs<{ target: string }>(args, {
    positional: { key: "target", label: "A username or user ID" },
  });

  const myId = await resolveMyId(client);
  const targetUserId = await resolveUserId(client, target);
  return client.users.muteUser(myId, { body: { targetUserId } });
}

export async function unmute(client: Client, args: string[]): Promise<unknown> {
  const { target } = parseArgs<{ target: string }>(args, {
    positional: { key: "target", label: "A username or user ID" },
  });

  const myId = await resolveMyId(client);
  const targetUserId = await resolveUserId(client, target);
  return client.users.unmuteUser(myId, targetUserId);
}

export async function muted(client: Client, args: string[]): Promise<unknown> {
  const flags = parseArgs<{
    maxResults?: number;
    nextToken?: string;
    raw: boolean;
  }>(args, { flags: { ...PAGINATION, ...RAW } });

  const myId = await resolveMyId(client);

  const options: Record<string, unknown> = {
    userFields: USER_FIELDS,
    ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
    ...(flags.nextToken !== undefined && { paginationToken: flags.nextToken }),
  };

  const response = await client.users.getMuting(myId, options);
  return flags.raw ? response : (response.data ?? []);
}
