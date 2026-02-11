#!/usr/bin/env python3
"""
Check follow relationship between two users
Usage: python3 scripts/check_relationship.py USER1 USER2
"""
import argparse
from twitter_api import api_get


def main():
    parser = argparse.ArgumentParser(description="Check follow relationship")
    parser.add_argument("source", help="Source username")
    parser.add_argument("target", help="Target username")
    args = parser.parse_args()

    params = {"source_user_name": args.source, "target_user_name": args.target}
    data = api_get("user/check_follow_relationship", params)
    result = data.get("data") or data

    print(f"source: @{args.source}")
    print(f"target: @{args.target}")
    print(f"source_follows_target: {result.get('following', False)}")
    print(f"target_follows_source: {result.get('followed_by', False)}")


if __name__ == "__main__":
    main()
