#!/usr/bin/env python3
"""
Get long-form article from tweet
Usage: python3 scripts/get_article.py TWEET_ID
"""
import argparse
import json
from twitter_api import api_get


def main():
    parser = argparse.ArgumentParser(description="Get Twitter article")
    parser.add_argument("tweet_id", help="Tweet ID with article")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    data = api_get("article", {"tweet_id": args.tweet_id})
    article = data.get("data") or data

    if args.json:
        print(json.dumps(article, indent=2))
        return

    print(f"tweet_id: {args.tweet_id}")
    if article.get("title"):
        print(f"title: {article['title']}")
    if article.get("content"):
        print(f"---")
        print(article["content"][:2000])
        if len(article.get("content", "")) > 2000:
            print(f"... (truncated, {len(article['content'])} chars total)")


if __name__ == "__main__":
    main()
