import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

TENANT = os.getenv("C8Y_TENANT")
USERNAME = os.getenv("C8Y_USERNAME")
PASSWORD = os.getenv("C8Y_PASSWORD")
BASE_URL = os.getenv("C8Y_BASE_URL")

raw_auth = f"{TENANT}/{USERNAME}:{PASSWORD}"
encoded_auth = base64.b64encode(raw_auth.encode()).decode()

HEADERS = {
    "Authorization": f"Basic {encoded_auth}",
    "Accept": "application/json"
}

def get_current_user():
    url = f"{BASE_URL}/events"
    response = requests.get(url, headers=HEADERS)
    if response.ok:
        user = response.json()
        return f"Username: {user.get('userName')}, Roles: {[r['name'] for r in user.get('effectiveRoles', [])]}"
    return f"Error: {response.status_code} {response.text}"
