#!/usr/bin/env python3
"""
Get tweet replies
Usage: python3 scripts/get_tweet_replies.py TWEET_ID --limit 20
"""
import argparse
from twitter_api import api_get, print_tweets_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Get tweet replies")
    parser.add_argument("tweet_id", help="Tweet ID")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max replies")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    params = {"tweetId": args.tweet_id, "cursor": args.cursor}
    data = api_get("tweet/replies", params)
    tweets = (data.get("tweets") or data.get("replies") or [])[:args.limit]

    print(f"tweet_id: {args.tweet_id}")
    print_tweets_list(tweets, "replies")
    print_pagination(data)


if __name__ == "__main__":
    main()
