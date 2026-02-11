#!/usr/bin/env python3
"""
Get user's verified followers only
Usage: python3 scripts/get_verified_followers.py USERNAME --limit 20
"""
import argparse
from twitter_api import api_get, print_users_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Get user's verified followers")
    parser.add_argument("username", help="Twitter username (without @)")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max results")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    # First get user_id from username
    user_data = api_get("user/info", {"userName": args.username})
    user_id = (user_data.get("data") or user_data).get("id")
    
    params = {"user_id": user_id, "cursor": args.cursor}
    data = api_get("user/verifiedFollowers", params)
    users = (data.get("followers") or data.get("users") or [])[:args.limit]

    print(f"username: @{args.username}")
    print_users_list(users, "verified_followers")
    print_pagination(data)


if __name__ == "__main__":
    main()
