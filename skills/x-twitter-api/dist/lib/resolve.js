let cachedId = null;
export async function resolveMyId(client) {
    if (cachedId)
        return cachedId;
    const response = await client.users.getMe();
    const id = response.data?.id;
    if (!id)
        throw new Error("Could not resolve authenticated user ID from /2/users/me");
    cachedId = id;
    return id;
}
export async function resolveUserId(client, input) {
    if (/^\d+$/.test(input))
        return input;
    const username = input.startsWith("@") ? input.slice(1) : input;
    const response = await client.users.getByUsername(username);
    const id = response.data?.id;
    if (!id)
        throw new Error(`Could not resolve user "${input}" to an ID.`);
    return id;
}
/** @internal — for testing only */
export function _resetMyIdCache() {
    cachedId = null;
}
