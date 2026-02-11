import { Client, OAuth1 } from "@xdevplatform/xdk";
import type { Config } from "./config.js";

export function createClient(config: Config): Client {
  const oauth1 = new OAuth1({
    apiKey: config.apiKey,
    apiSecret: config.apiSecret,
    callback: "oob",
    accessToken: config.accessToken,
    accessTokenSecret: config.accessTokenSecret,
  });

  return new Client({ oauth1 });
}
