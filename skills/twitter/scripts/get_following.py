#!/usr/bin/env python3
"""
Get user's following
Usage: python3 scripts/get_following.py USERNAME --limit 100
"""
import argparse
from twitter_api import api_get, print_users_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Get user's following")
    parser.add_argument("username", help="Twitter username (without @)")
    parser.add_argument("--limit", "-l", type=int, default=100, help="Max following (max 200/page)")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    params = {
        "userName": args.username,
        "cursor": args.cursor,
        "pageSize": min(args.limit, 200),
    }
    data = api_get("user/followings", params)
    users = (data.get("followings") or data.get("users") or [])[:args.limit]

    print(f"username: @{args.username}")
    print_users_list(users, "following")
    print_pagination(data)


if __name__ == "__main__":
    main()
