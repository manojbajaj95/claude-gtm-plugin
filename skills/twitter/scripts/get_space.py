#!/usr/bin/env python3
"""
Get Twitter Space details
Usage: python3 scripts/get_space.py SPACE_ID
"""
import argparse
import json
from twitter_api import api_get, format_count


def main():
    parser = argparse.ArgumentParser(description="Get Twitter Space details")
    parser.add_argument("space_id", help="Space ID")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    data = api_get("space", {"spaceId": args.space_id})
    space = data.get("data") or data

    if args.json:
        print(json.dumps(space, indent=2))
        return

    print(f"id: {space.get('id', '')}")
    print(f"title: {space.get('title', '')}")
    print(f"state: {space.get('state', '')}")
    print(f"host: @{space.get('creator', {}).get('userName', '')}")
    print(f"participants: {format_count(space.get('participant_count'))}")
    print(f"created: {space.get('created_at', '')}")
    print(f"started: {space.get('started_at', '')}")


if __name__ == "__main__":
    main()
