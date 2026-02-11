import type { Client } from "@xdevplatform/xdk";
import { parseArgs } from "../lib/args.js";
import { resolveMyId, resolveUserId } from "../lib/resolve.js";

export async function follow(client: Client, args: string[]): Promise<unknown> {
  const { target } = parseArgs<{ target: string }>(args, {
    positional: { key: "target", label: "A username or user ID" },
  });

  const myId = await resolveMyId(client);
  const targetUserId = await resolveUserId(client, target);
  return client.users.followUser(myId, { body: { targetUserId } });
}

export async function unfollow(
  client: Client,
  args: string[],
): Promise<unknown> {
  const { target } = parseArgs<{ target: string }>(args, {
    positional: { key: "target", label: "A username or user ID" },
  });

  const myId = await resolveMyId(client);
  const targetUserId = await resolveUserId(client, target);
  return client.users.unfollowUser(myId, targetUserId);
}
