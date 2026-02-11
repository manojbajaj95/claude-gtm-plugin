import type { Client } from "@xdevplatform/xdk";
import { parseArgs, RAW } from "../lib/args.js";
import { USER_FIELDS_EXTENDED } from "../lib/fields.js";

interface MeFlags {
  fields: string[];
  pinnedTweet: boolean;
  raw: boolean;
}

export async function me(client: Client, args: string[]): Promise<unknown> {
  const flags = parseArgs<MeFlags>(args, {
    flags: {
      ...RAW,
      "--fields": { key: "fields", type: "string[]" },
      "--pinned-tweet": { key: "pinnedTweet", type: "boolean" },
    },
    defaults: { fields: USER_FIELDS_EXTENDED },
  });

  const options: Record<string, unknown> = {
    userFields: flags.fields,
  };

  if (flags.pinnedTweet) {
    options.expansions = ["pinned_tweet_id"];
    options.tweetFields = ["created_at", "text", "public_metrics"];
  }

  const response = await client.users.getMe(options);

  if (flags.raw || flags.pinnedTweet) {
    return response;
  }
  return response.data;
}
