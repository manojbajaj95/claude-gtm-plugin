import { parseArgs } from "../lib/args.js";
export async function post(client, args) {
    const flags = parseArgs(args, {
        positional: { key: "text", label: "Post text" },
        flags: {
            "--reply-to": { key: "replyTo", type: "string" },
            "--quote": { key: "quoteTweetId", type: "string" },
            "--reply-settings": { key: "replySettings", type: "string" },
        },
    });
    const body = { text: flags.text };
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
