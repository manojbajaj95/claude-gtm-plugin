import { Client, OAuth1 } from "@xdevplatform/xdk";
export function createClient(config) {
    const oauth1 = new OAuth1({
        apiKey: config.apiKey,
        apiSecret: config.apiSecret,
        callback: "oob",
        accessToken: config.accessToken,
        accessTokenSecret: config.accessTokenSecret,
    });
    return new Client({ oauth1 });
}
