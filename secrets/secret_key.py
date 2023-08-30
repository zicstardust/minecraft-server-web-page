import os
import secrets

KEY_FILE = os.path.join(os.path.dirname(__file__), "web_secret.key")

if __name__ == "__main__":
    with open(KEY_FILE, "wb") as f:
        f.write(secrets.token_bytes(128))
