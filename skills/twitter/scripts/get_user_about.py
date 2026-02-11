#!/usr/bin/env python3
"""
Get user profile about (extended info)
Usage: python3 scripts/get_user_about.py USERNAME
"""
import argparse
import json
from twitter_api import api_get


def main():
    parser = argparse.ArgumentParser(description="Get Twitter user about/profile")
    parser.add_argument("username", help="Twitter username (without @)")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    data = api_get("user_about", {"userName": args.username})
    user = data.get("data") or data

    if args.json:
        print(json.dumps(user, indent=2))
        return

    print(f"id: {user.get('id', '')}")
    print(f"username: @{user.get('userName', '')}")
    print(f"name: {user.get('name', '')}")
    print(f"verified: {user.get('isBlueVerified', False)}")
    print(f"protected: {user.get('protected', False)}")
    print(f"created: {user.get('createdAt', '')}")
    
    about = user.get("about_profile", {})
    if about:
        if about.get("account_based_in"):
            print(f"based_in: {about['account_based_in']}")
        changes = about.get("username_changes", {})
        if changes.get("count"):
            print(f"username_changes: {changes['count']}")


if __name__ == "__main__":
    main()
