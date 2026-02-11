#!/usr/bin/env python3
"""
Get community moderators
Usage: python3 scripts/get_community_moderators.py COMMUNITY_ID
"""
import argparse
from twitter_api import api_get, print_users_list, print_pagination


def main():
    parser = argparse.ArgumentParser(description="Get community moderators")
    parser.add_argument("community_id", help="Community ID")
    parser.add_argument("--cursor", "-c", help="Pagination cursor")
    args = parser.parse_args()

    params = {"communityId": args.community_id, "cursor": args.cursor}
    data = api_get("community/moderators", params)
    users = data.get("moderators") or data.get("users") or []

    print(f"community_id: {args.community_id}")
    print_users_list(users, "moderators")
    print_pagination(data)


if __name__ == "__main__":
    main()
