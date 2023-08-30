import os
import json

DB_CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "db_credentials.json")

if not os.path.exists(DB_CREDENTIALS_FILE):
    raise FileNotFoundError(
        f'Could not find {DB_CREDENTIALS_FILE}, please create it and add the keys "user" and "password" with your db credentials.'
    )

with open(DB_CREDENTIALS_FILE, "r") as f:
    __credentials = json.load(f)

DB_USER = __credentials["user"]
DB_PASSWORD = __credentials["password"]
