import type { Client } from "@xdevplatform/xdk";

let cachedId: string | null = null;

export async function resolveMyId(client: Client): Promise<string> {
  if (cachedId) return cachedId;
  const response = await client.users.getMe();
  const id = response.data?.id;
  if (!id)
    throw new Error(
      "Could not resolve authenticated user ID from /2/users/me",
    );
  cachedId = id;
  return id;
}

export async function resolveUserId(
  client: Client,
  input: string,
): Promise<string> {
  if (/^\d+$/.test(input)) return input;

  const username = input.startsWith("@") ? input.slice(1) : input;
  const response = await client.users.getByUsername(username);
  const id = response.data?.id;
  if (!id) throw new Error(`Could not resolve user "${input}" to an ID.`);
  return id;
}

/** @internal — for testing only */
export function _resetMyIdCache(): void {
  cachedId = null;
}
