#!/usr/bin/env python3
"""
Get tweets by IDs
Usage: python3 scripts/get_tweet.py TWEET_ID [TWEET_ID2...]
"""
import argparse
from twitter_api import api_get, clean_tweet, print_tweet


def main():
    parser = argparse.ArgumentParser(description="Get tweets by IDs")
    parser.add_argument("tweet_ids", nargs="+", help="Tweet ID(s)")
    args = parser.parse_args()

    ids = ",".join(args.tweet_ids)
    data = api_get("tweets", {"tweet_ids": ids})
    tweets = data.get("tweets") or []

    for i, tweet in enumerate(tweets):
        if i > 0:
            print("---")
        print_tweet(clean_tweet(tweet))


if __name__ == "__main__":
    main()
