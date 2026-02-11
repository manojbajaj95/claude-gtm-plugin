#!/usr/bin/env python3
import argparse
import json
import os
import requests
import sys
from getpass import getpass

DEFAULT_BASE_URL = "https://last.leadgenius.app"
AUTH_FILE = os.path.expanduser("~/.leadgenius_auth.json")

def main():
    parser = argparse.ArgumentParser(description="Authenticate with LeadGenius Pro/EpsimoAI")
    parser.add_argument("--email", help="User email")
    parser.add_argument("--password", help="User password")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help=f"Application base URL (default: {DEFAULT_BASE_URL})")
    parser.add_argument("--save", action="store_true", default=True, help="Save credentials (default: True)")

    args = parser.parse_args()

    email = args.email or input("Email: ")
    password = args.password or getpass("Password: ")

    url = f"{args.base_url.rstrip('/')}/api/auth"
    
    print(f"Authenticating with {url}...")
    
    try:
        response = requests.post(
            url,
            json={"username": email, "password": password},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            tokens = data.get("tokens", {})
            token = tokens.get("accessToken") or data.get("jwt_token")
            
            if not token:
                print("Error: Authentication succeeded but no token was returned.")
                sys.exit(1)
                
            print("Successfully authenticated!")
            
            if args.save:
                auth_data = {
                    "token": token,
                    "email": email,
                    "base_url": args.base_url
                }
                with open(AUTH_FILE, "w") as f:
                    json.dump(auth_data, f, indent=2)
                print(f"Credentials saved to {AUTH_FILE}")
            
            return token
        else:
            print(f"Authentication failed (Status {response.status_code}): {response.text}")
            sys.exit(1)
            
    except Exception as e:
        print(f"Error connecting to authentication service: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
