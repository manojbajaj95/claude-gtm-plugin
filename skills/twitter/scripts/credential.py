#!/usr/bin/env python3
"""
Twitter API credential management.
Reads from environment: TWITTERAPI_API_KEY
"""
import os


def get_twitter_api_key() -> str | None:
    """Get TwitterAPI.io API key"""
    return os.environ.get("TWITTERAPI_API_KEY")


def has_twitter_key() -> bool:
    """Check if API key is available"""
    return get_twitter_api_key() is not None
