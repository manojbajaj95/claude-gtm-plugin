#!/usr/bin/env python3
"""
Get community info by ID
Usage: python3 scripts/get_community.py COMMUNITY_ID
"""
import argparse
import json
from twitter_api import api_get, format_count


def main():
    parser = argparse.ArgumentParser(description="Get community info")
    parser.add_argument("community_id", help="Community ID")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    data = api_get("community", {"communityId": args.community_id})
    community = data.get("data") or data

    if args.json:
        print(json.dumps(community, indent=2))
        return

    print(f"id: {community.get('id', '')}")
    print(f"name: {community.get('name', '')}")
    print(f"description: {community.get('description', '')[:200]}")
    print(f"members: {format_count(community.get('member_count'))}")
    print(f"created: {community.get('created_at', '')}")


if __name__ == "__main__":
    main()
