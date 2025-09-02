#!/usr/bin/env python3
import requests
import json
import time

def test_categories_api():
    url = "http://localhost:8000/categories/"
    
    print("Testing Categories API...")
    print(f"URL: {url}")
    print("-" * 50)
    
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response Body:")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(json.dumps(data, indent=2))
            except json.JSONDecodeError:
                print(response.text)
        else:
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to server. Is it running on http://localhost:8000?")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    # Wait a moment for server to be ready
    time.sleep(2)
    test_categories_api()
