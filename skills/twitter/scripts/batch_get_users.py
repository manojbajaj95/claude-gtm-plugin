#!/usr/bin/env python3
"""
Batch get user info by user IDs
Usage: python3 scripts/batch_get_users.py USER_ID1,USER_ID2,USER_ID3
"""
import argparse
from twitter_api import api_get, print_users_list


def main():
    parser = argparse.ArgumentParser(description="Batch get Twitter users by IDs")
    parser.add_argument("user_ids", help="Comma-separated user IDs")
    args = parser.parse_args()

    data = api_get("user/batch_info_by_ids", {"userIds": args.user_ids})
    users = data.get("users") or data.get("data") or []
    
    print(f"total: {len(users)}")
    print_users_list(users)


if __name__ == "__main__":
    main()
