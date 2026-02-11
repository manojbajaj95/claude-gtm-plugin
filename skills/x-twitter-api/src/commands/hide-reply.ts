import type { Client } from "@xdevplatform/xdk";
import { parseArgs } from "../lib/args.js";

export async function hideReply(
  client: Client,
  args: string[],
): Promise<unknown> {
  const { tweetId } = parseArgs<{ tweetId: string }>(args, {
    positional: { key: "tweetId", label: "A tweet ID" },
  });

  return client.posts.hideReply(tweetId, { body: { hidden: true } });
}
