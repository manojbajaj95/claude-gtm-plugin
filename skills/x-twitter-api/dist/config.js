import { readFileSync } from "fs";
import { resolve } from "path";
const REQUIRED_VARS = [
    "X_API_KEY",
    "X_API_SECRET",
    "X_ACCESS_TOKEN",
    "X_ACCESS_TOKEN_SECRET",
];
function parseEnvFile(path) {
    try {
        const content = readFileSync(path, "utf-8");
        const vars = {};
        for (const line of content.split("\n")) {
            const trimmed = line.trim();
            if (!trimmed || trimmed.startsWith("#"))
                continue;
            const eqIndex = trimmed.indexOf("=");
            if (eqIndex === -1)
                continue;
            const key = trimmed.slice(0, eqIndex).trim();
            const raw = trimmed.slice(eqIndex + 1).trim();
            vars[key] = raw.replace(/^["']|["']$/g, "");
        }
        return vars;
    }
    catch {
        return {};
    }
}
function resolveVar(key, sources) {
    for (const source of sources) {
        if (source[key])
            return source[key];
    }
    return process.env[key];
}
export function loadConfig(pluginDir) {
    const cwd = process.cwd();
    // cwd first (project-level), then plugin dir — matches bash plugin pattern
    const sources = [
        parseEnvFile(resolve(cwd, ".env.local")),
        parseEnvFile(resolve(cwd, ".env")),
        parseEnvFile(resolve(pluginDir, ".env.local")),
        parseEnvFile(resolve(pluginDir, ".env")),
    ];
    const missing = [];
    const get = (key) => {
        const value = resolveVar(key, sources);
        if (!value)
            missing.push(key);
        return value ?? "";
    };
    const config = {
        apiKey: get("X_API_KEY"),
        apiSecret: get("X_API_SECRET"),
        accessToken: get("X_ACCESS_TOKEN"),
        accessTokenSecret: get("X_ACCESS_TOKEN_SECRET"),
    };
    if (missing.length > 0) {
        throw new Error(`Missing required environment variables: ${missing.join(", ")}\n` +
            `Set them in .env.local, .env, or as environment variables.`);
    }
    return config;
}
