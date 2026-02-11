import type { Client } from "@xdevplatform/xdk";
import { parseArgs } from "../lib/args.js";
import { resolveMyId } from "../lib/resolve.js";

export async function like(client: Client, args: string[]): Promise<unknown> {
  const { tweetId } = parseArgs<{ tweetId: string }>(args, {
    positional: { key: "tweetId", label: "A tweet ID" },
  });

  const myId = await resolveMyId(client);
  return client.users.likePost(myId, { body: { tweetId } });
}

export async function unlike(client: Client, args: string[]): Promise<unknown> {
  const { tweetId } = parseArgs<{ tweetId: string }>(args, {
    positional: { key: "tweetId", label: "A tweet ID" },
  });

  const myId = await resolveMyId(client);
  return client.users.unlikePost(myId, tweetId);
}
