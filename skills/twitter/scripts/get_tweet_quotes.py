#!/usr/bin/env python3
"""
Get quote tweets
Usage: python3 scripts/get_tweet_quotes.py TWEET_ID --limit 20
"""
import argparse
from twitter_api import api_get, print_tweets_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Get quote tweets")
    parser.add_argument("tweet_id", help="Tweet ID")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max quotes")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    params = {"tweetId": args.tweet_id, "cursor": args.cursor}
    data = api_get("tweet/quotes", params)
    tweets = (data.get("tweets") or data.get("quotes") or [])[:args.limit]

    print(f"tweet_id: {args.tweet_id}")
    print_tweets_list(tweets, "quotes")
    print_pagination(data)


if __name__ == "__main__":
    main()
