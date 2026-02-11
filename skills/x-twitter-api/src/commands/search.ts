import type { Client } from "@xdevplatform/xdk";
import { parseArgs, PAGINATION, TEMPORAL, RAW } from "../lib/args.js";
import { TWEET_FIELDS, TWEET_EXPANSIONS, TWEET_USER_FIELDS } from "../lib/fields.js";

interface SearchFlags {
  query: string;
  all: boolean;
  maxResults?: number;
  sortOrder?: string;
  startTime?: string;
  endTime?: string;
  sinceId?: string;
  untilId?: string;
  nextToken?: string;
  tweetFields: string[];
  raw: boolean;
}

export async function search(
  client: Client,
  args: string[],
): Promise<unknown> {
  const flags = parseArgs<SearchFlags>(args, {
    positional: { key: "query", label: "A search query" },
    flags: {
      ...PAGINATION,
      ...TEMPORAL,
      ...RAW,
      "--all": { key: "all", type: "boolean" },
      "--sort": { key: "sortOrder", type: "string" },
      "--since-id": { key: "sinceId", type: "string" },
      "--until-id": { key: "untilId", type: "string" },
      "--fields": { key: "tweetFields", type: "string[]" },
    },
    defaults: { tweetFields: TWEET_FIELDS },
  });

  const options = {
    tweetFields: flags.tweetFields,
    expansions: TWEET_EXPANSIONS,
    userFields: TWEET_USER_FIELDS,
    ...(flags.maxResults !== undefined && { maxResults: flags.maxResults }),
    ...(flags.sortOrder !== undefined && { sortOrder: flags.sortOrder }),
    ...(flags.startTime !== undefined && { startTime: flags.startTime }),
    ...(flags.endTime !== undefined && { endTime: flags.endTime }),
    ...(flags.sinceId !== undefined && { sinceId: flags.sinceId }),
    ...(flags.untilId !== undefined && { untilId: flags.untilId }),
    ...(flags.nextToken !== undefined && { nextToken: flags.nextToken }),
  };

  const response = flags.all
    ? await client.posts.searchAll(flags.query, options)
    : await client.posts.searchRecent(flags.query, options);

  return flags.raw ? response : (response.data ?? []);
}
