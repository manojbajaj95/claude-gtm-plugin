import type { Client } from "@xdevplatform/xdk";
import { parseArgs } from "../lib/args.js";

interface PostFlags {
  text: string;
  replyTo?: string;
  quoteTweetId?: string;
  replySettings?: string;
}

export async function post(
  client: Client,
  args: string[],
): Promise<unknown> {
  const flags = parseArgs<PostFlags>(args, {
    positional: { key: "text", label: "Post text" },
    flags: {
      "--reply-to": { key: "replyTo", type: "string" },
      "--quote": { key: "quoteTweetId", type: "string" },
      "--reply-settings": { key: "replySettings", type: "string" },
    },
  });

  const body: Record<string, unknown> = { text: flags.text };

  if (flags.replyTo) {
    body.reply = { inReplyToTweetId: flags.replyTo };
  }
  if (flags.quoteTweetId) {
    body.quoteTweetId = flags.quoteTweetId;
  }
  if (flags.replySettings) {
    body.replySettings = flags.replySettings;
  }

  return client.posts.create(body);
}
