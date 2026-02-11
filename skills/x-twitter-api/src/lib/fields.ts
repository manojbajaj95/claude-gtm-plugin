export const TWEET_FIELDS = [
  "author_id",
  "created_at",
  "conversation_id",
  "public_metrics",
  "text",
];

export const TWEET_EXPANSIONS = ["author_id"];
export const TWEET_USER_FIELDS = ["name", "username"];

export const USER_FIELDS = [
  "created_at",
  "description",
  "id",
  "name",
  "profile_image_url",
  "public_metrics",
  "username",
  "verified_type",
];

export const USER_FIELDS_EXTENDED = [
  ...USER_FIELDS,
  "location",
  "protected",
  "url",
];
