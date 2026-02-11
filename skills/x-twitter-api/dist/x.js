import { dirname, resolve } from "path";
import { fileURLToPath } from "url";
import { loadConfig } from "./config.js";
import { createClient } from "./client.js";
import { me } from "./commands/me.js";
import { search } from "./commands/search.js";
import { get } from "./commands/get.js";
import { post } from "./commands/post.js";
import { del } from "./commands/delete.js";
import { like, unlike } from "./commands/like.js";
import { repost, unrepost } from "./commands/repost.js";
import { hideReply } from "./commands/hide-reply.js";
import { searchUsers } from "./commands/search-users.js";
import { count } from "./commands/count.js";
import { trending } from "./commands/trending.js";
import { timeline } from "./commands/timeline.js";
import { mentions } from "./commands/mentions.js";
import { bookmark, unbookmark, bookmarks } from "./commands/bookmark.js";
import { blocked } from "./commands/blocked.js";
import { mute, unmute, muted } from "./commands/mute.js";
import { repostsOfMe } from "./commands/reposts-of-me.js";
import { user } from "./commands/user.js";
import { follow, unfollow } from "./commands/follow.js";
import { followers, following } from "./commands/followers.js";
import { likers } from "./commands/likers.js";
import { reposters } from "./commands/reposters.js";
import { quotes } from "./commands/quotes.js";
const commands = {
    me,
    search,
    get,
    post,
    delete: del,
    like,
    unlike,
    repost,
    unrepost,
    "hide-reply": hideReply,
    "search-users": searchUsers,
    count,
    trending,
    timeline,
    mentions,
    bookmark,
    unbookmark,
    bookmarks,
    blocked,
    mute,
    unmute,
    muted,
    "reposts-of-me": repostsOfMe,
    user,
    follow,
    unfollow,
    followers,
    following,
    likers,
    reposters,
    quotes,
};
const COMMAND_NAMES = Object.keys(commands).join(", ");
function pluginDir() {
    return resolve(dirname(fileURLToPath(import.meta.url)), "../../..");
}
async function main() {
    const [command, ...args] = process.argv.slice(2);
    if (!command || !commands[command]) {
        console.error(`Usage: x <command> [args]\nCommands: ${COMMAND_NAMES}`);
        process.exit(1);
    }
    const config = loadConfig(pluginDir());
    const client = createClient(config);
    const result = await commands[command](client, args);
    if (result !== undefined) {
        console.log(JSON.stringify(result, null, 2));
    }
    process.exit(0);
}
main().catch((error) => {
    const message = error instanceof Error ? error.message : String(error);
    console.error(`Error: ${message}`);
    process.exit(1);
});
