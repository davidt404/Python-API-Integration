# Python REST API Integration Script
# Performs authenticated GET request, handles errors, and formats JSON output

import requests
import json
from datetime import datetime

API_URL = "https://api.example.com/data"
API_KEY = "YOUR_API_KEY"

def fetch_data():
    headers = {"Authorization": f"Bearer {API_KEY}", "Accept": "application/json"}
    try:
        response = requests.get(API_URL, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ✅ Request successful")
        print(json.dumps(data, indent=4))
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")

if __name__ == "__main__":
    fetch_data()
