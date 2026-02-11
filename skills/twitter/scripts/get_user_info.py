#!/usr/bin/env python3
"""
Get user info by username
Usage: python3 scripts/get_user_info.py USERNAME
"""
import argparse
from twitter_api import api_get, clean_user, print_user


def main():
    parser = argparse.ArgumentParser(description="Get Twitter user info")
    parser.add_argument("username", help="Twitter username (without @)")
    args = parser.parse_args()

    data = api_get("user/info", {"userName": args.username})
    user = data.get("data") or data
    print_user(clean_user(user))


if __name__ == "__main__":
    main()
