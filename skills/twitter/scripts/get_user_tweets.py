#!/usr/bin/env python3
"""
Get user's recent tweets
Usage: python3 scripts/get_user_tweets.py USERNAME --limit 20
"""
import argparse
from twitter_api import api_get, print_tweets_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Get user's tweets")
    parser.add_argument("username", help="Twitter username (without @)")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max tweets")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    parser.add_argument("--include-replies", action="store_true", help="Include replies")
    args = parser.parse_args()

    params = {
        "userName": args.username,
        "cursor": args.cursor,
        "includeReplies": "true" if args.include_replies else "false",
    }
    data = api_get("user/last_tweets", params)
    tweets = (data.get("tweets") or [])[:args.limit]

    print(f"username: @{args.username}")
    print_tweets_list(tweets)
    print_pagination(data)


if __name__ == "__main__":
    main()
