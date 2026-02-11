#!/usr/bin/env python3
"""
Get user's mentions
Usage: python3 scripts/get_user_mentions.py USERNAME --limit 20
"""
import argparse
from twitter_api import api_get, print_tweets_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Get user's mentions")
    parser.add_argument("username", help="Twitter username (without @)")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max mentions")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    params = {"userName": args.username, "cursor": args.cursor}
    data = api_get("user/mentions", params)
    tweets = (data.get("tweets") or [])[:args.limit]

    print(f"username: @{args.username}")
    print_tweets_list(tweets, "mentions")
    print_pagination(data)


if __name__ == "__main__":
    main()
