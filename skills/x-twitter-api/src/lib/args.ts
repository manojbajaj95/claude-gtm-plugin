export interface FlagDef {
  key: string;
  type: "string" | "number" | "boolean" | "string[]";
}

export interface ParseSchema {
  positional?: { key: string; label: string };
  flags?: Record<string, FlagDef>;
  defaults?: Record<string, unknown>;
}

export const PAGINATION: Record<string, FlagDef> = {
  "--max-results": { key: "maxResults", type: "number" },
  "--next-token": { key: "nextToken", type: "string" },
};

export const TEMPORAL: Record<string, FlagDef> = {
  "--start-time": { key: "startTime", type: "string" },
  "--end-time": { key: "endTime", type: "string" },
};

export const RAW: Record<string, FlagDef> = {
  "--raw": { key: "raw", type: "boolean" },
};

export function parseArgs<T>(
  args: string[],
  schema: ParseSchema,
): T {
  const result: Record<string, unknown> = {};

  // Default all boolean flags to false
  if (schema.flags) {
    for (const def of Object.values(schema.flags)) {
      if (def.type === "boolean") result[def.key] = false;
    }
  }

  // Apply explicit defaults
  if (schema.defaults) {
    Object.assign(result, schema.defaults);
  }

  let startIdx = 0;

  // Extract positional arg
  if (schema.positional) {
    const first = args[0];
    if (!first || first.startsWith("--")) {
      throw new Error(
        `${schema.positional.label} is required as the first argument.`,
      );
    }
    result[schema.positional.key] = first;
    startIdx = 1;
  }

  // Parse flags
  for (let i = startIdx; i < args.length; i++) {
    const arg = args[i];
    const def = schema.flags?.[arg];

    if (!def) throw new Error(`Unknown flag: ${arg}`);

    if (def.type === "boolean") {
      result[def.key] = true;
      continue;
    }

    const value = args[++i];
    if (value === undefined) throw new Error(`${arg} requires a value`);

    switch (def.type) {
      case "number": {
        const num = Number(value);
        if (Number.isNaN(num)) throw new Error(`${arg} requires a numeric value, got "${value}"`);
        result[def.key] = num;
        break;
      }
      case "string[]":
        result[def.key] = value.split(",").map((s) => s.trim());
        break;
      default:
        result[def.key] = value;
    }
  }

  return result as T;
}
