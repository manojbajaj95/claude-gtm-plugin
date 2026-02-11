#!/usr/bin/env python3
"""
Search users by keyword
Usage: python3 scripts/search_users.py "AI researcher" --limit 20
"""
import argparse
from twitter_api import api_get, print_users_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Search Twitter users")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max results")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    params = {"query": args.query, "cursor": args.cursor}
    data = api_get("user/search", params)
    users = (data.get("users") or [])[:args.limit]

    print(f"query: {args.query}")
    print_users_list(users)
    print_pagination(data)


if __name__ == "__main__":
    main()
