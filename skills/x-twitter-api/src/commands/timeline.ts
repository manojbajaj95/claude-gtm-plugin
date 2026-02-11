import type { Client } from "@xdevplatform/xdk";
import { parseArgs, PAGINATION, TEMPORAL, RAW } from "../lib/args.js";
import { TWEET_FIELDS, TWEET_EXPANSIONS, TWEET_USER_FIELDS } from "../lib/fields.js";
import { resolveMyId } from "../lib/resolve.js";

export async function timeline(
  client: Client,
  args: string[],
): Promise<unknown> {
  const flags = parseArgs<{
    maxResults?: number;
    nextToken?: string;
    startTime?: string;
    endTime?: string;
    raw: boolean;
  }>(args, { flags: { ...PAGINATION, ...TEMPORAL, ...RAW } });

  const myId = await resolveMyId(client);

  const options: Record<string, unknown> = {
    tweetFields: TWEET_FIELDS,
    expansions: TWEET_EXPANSIONS,
    userFields: TWEET_USER_FIELDS,
    ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
    ...(flags.nextToken !== undefined && { paginationToken: flags.nextToken }),
    ...(flags.startTime !== undefined && { startTime: flags.startTime }),
    ...(flags.endTime !== undefined && { endTime: flags.endTime }),
  };

  const response = await client.users.getTimeline(myId, options);
  return flags.raw ? response : (response.data ?? []);
}
