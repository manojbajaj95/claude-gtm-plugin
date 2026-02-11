#!/usr/bin/env python3
"""
Get users who retweeted a tweet
Usage: python3 scripts/get_tweet_retweeters.py TWEET_ID --limit 50
"""
import argparse
from twitter_api import api_get, print_users_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Get tweet retweeters")
    parser.add_argument("tweet_id", help="Tweet ID")
    parser.add_argument("--limit", "-l", type=int, default=50, help="Max retweeters")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    params = {"tweetId": args.tweet_id, "cursor": args.cursor}
    data = api_get("tweet/retweeters", params)
    users = (data.get("users") or data.get("retweeters") or [])[:args.limit]

    print(f"tweet_id: {args.tweet_id}")
    print_users_list(users, "retweeters")
    print_pagination(data)


if __name__ == "__main__":
    main()
