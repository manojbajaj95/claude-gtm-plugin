#!/usr/bin/env python3
"""
Get list members
Usage: python3 scripts/get_list_members.py LIST_ID --limit 20
"""
import argparse
from twitter_api import api_get, print_users_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Get list members")
    parser.add_argument("list_id", help="List ID")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max members")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    params = {"list_id": args.list_id, "cursor": args.cursor}
    data = api_get("list/members", params)
    users = (data.get("members") or data.get("users") or [])[:args.limit]

    print(f"list_id: {args.list_id}")
    print_users_list(users, "members")
    print_pagination(data)


if __name__ == "__main__":
    main()
