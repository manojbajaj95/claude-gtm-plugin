#!/usr/bin/env python3
"""
Get tweet thread context
Usage: python3 scripts/get_tweet_thread.py TWEET_ID
"""
import argparse
from twitter_api import api_get, print_tweets_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Get tweet thread context")
    parser.add_argument("tweet_id", help="Tweet ID")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    params = {"tweetId": args.tweet_id, "cursor": args.cursor}
    data = api_get("tweet/thread_context", params)
    tweets = data.get("replies") or data.get("tweets") or []

    print(f"tweet_id: {args.tweet_id}")
    print_tweets_list(tweets, "thread")
    print_pagination(data)


if __name__ == "__main__":
    main()
