#!/usr/bin/env python3
"""
Advanced tweet search
Usage: python3 scripts/search_tweets.py "query" --type Latest --limit 20
"""
import argparse
from twitter_api import api_get, print_tweets_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Search tweets")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--type", "-t", choices=["Latest", "Top"], default="Latest",
                        help="Query type (default: Latest)")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max results")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    params = {
        "query": args.query,
        "queryType": args.type,
        "cursor": args.cursor,
    }
    data = api_get("tweet/advanced_search", params)
    tweets = (data.get("tweets") or [])[:args.limit]

    print(f"query: {args.query}")
    print(f"type: {args.type}")
    print_tweets_list(tweets)
    print_pagination(data)


if __name__ == "__main__":
    main()
