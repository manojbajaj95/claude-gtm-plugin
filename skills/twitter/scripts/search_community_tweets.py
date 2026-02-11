#!/usr/bin/env python3
"""
Search tweets from all communities
Usage: python3 scripts/search_community_tweets.py "query" --limit 20
"""
import argparse
from twitter_api import api_get, print_tweets_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Search community tweets")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max tweets")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    params = {"query": args.query, "queryType": "Latest", "cursor": args.cursor}
    data = api_get("community/get_tweets_from_all_community", params)
    tweets = (data.get("tweets") or [])[:args.limit]

    print(f"query: {args.query}")
    print_tweets_list(tweets)
    print_pagination(data)


if __name__ == "__main__":
    main()
