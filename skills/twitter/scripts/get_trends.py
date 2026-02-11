#!/usr/bin/env python3
"""
Get Twitter trends by location
Usage: python3 scripts/get_trends.py --woeid 1
"""
import argparse
import json
from twitter_api import api_get, format_count


# Common WOEIDs
WOEIDS = {
    "worldwide": 1,
    "usa": 23424977,
    "uk": 23424975,
    "japan": 23424856,
    "india": 23424848,
    "brazil": 23424768,
    "canada": 23424775,
    "australia": 23424748,
    "germany": 23424829,
    "france": 23424819,
}


def main():
    parser = argparse.ArgumentParser(description="Get Twitter trends")
    parser.add_argument("--woeid", "-w", type=int, default=1, 
                        help="WOEID (1=Worldwide, 23424977=USA)")
    parser.add_argument("--location", "-l", choices=list(WOEIDS.keys()),
                        help="Location name (alternative to woeid)")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    woeid = WOEIDS.get(args.location, args.woeid) if args.location else args.woeid
    data = api_get("trends", {"woeid": woeid})
    trends = data.get("trends") or data.get("data") or []

    if args.json:
        print(json.dumps(trends, indent=2))
        return

    print(f"woeid: {woeid}")
    print(f"trends[{len(trends)}]{{name,posts}}:")
    for t in trends[:30]:
        trend = t.get("trend", t)
        name = trend.get("name", "")
        posts = trend.get("meta_description", "-")
        print(f"  {name},{posts}")


if __name__ == "__main__":
    main()
