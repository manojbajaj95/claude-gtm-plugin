import type { Client } from "@xdevplatform/xdk";
import { parseArgs, TEMPORAL, RAW } from "../lib/args.js";

interface CountFlags {
  query: string;
  all: boolean;
  startTime?: string;
  endTime?: string;
  granularity?: string;
  nextToken?: string;
  raw: boolean;
}

export async function count(client: Client, args: string[]): Promise<unknown> {
  const flags = parseArgs<CountFlags>(args, {
    positional: { key: "query", label: "A search query" },
    flags: {
      ...TEMPORAL,
      ...RAW,
      "--all": { key: "all", type: "boolean" },
      "--granularity": { key: "granularity", type: "string" },
      "--next-token": { key: "nextToken", type: "string" },
    },
  });

  const options: Record<string, unknown> = {
    ...(flags.startTime !== undefined && { startTime: flags.startTime }),
    ...(flags.endTime !== undefined && { endTime: flags.endTime }),
    ...(flags.granularity !== undefined && { granularity: flags.granularity }),
    ...(flags.nextToken !== undefined && { nextToken: flags.nextToken }),
  };

  const response = flags.all
    ? await client.posts.getCountsAll(flags.query, options)
    : await client.posts.getCountsRecent(flags.query, options);

  return flags.raw ? response : (response.data ?? []);
}
