#!/usr/bin/env python3
"""
Get community members
Usage: python3 scripts/get_community_members.py COMMUNITY_ID --limit 20
"""
import argparse
from twitter_api import api_get, print_users_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Get community members")
    parser.add_argument("community_id", help="Community ID")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max members")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    params = {"communityId": args.community_id, "cursor": args.cursor}
    data = api_get("community/members", params)
    users = (data.get("members") or data.get("users") or [])[:args.limit]

    print(f"community_id: {args.community_id}")
    print_users_list(users, "members")
    print_pagination(data)


if __name__ == "__main__":
    main()
