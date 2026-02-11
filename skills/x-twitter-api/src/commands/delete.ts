import type { Client } from "@xdevplatform/xdk";
import { parseArgs } from "../lib/args.js";

export async function del(
  client: Client,
  args: string[],
): Promise<unknown> {
  const { id } = parseArgs<{ id: string }>(args, {
    positional: { key: "id", label: "A post ID" },
  });

  return client.posts.delete(id);
}
