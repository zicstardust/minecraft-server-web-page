import os
import json

DB_CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "db_credentials.json")

with open(DB_CREDENTIALS_FILE, "r") as f:
    __credentials = json.load(f)

DB_USER = __credentials["user"]
DB_PASSWORD = __credentials["password"]
