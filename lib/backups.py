import os
from datetime import datetime

BACKUP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "backup", "backups"))


def parse_name(name):
    "Name is in format %Y-%m-%d_%H-%M-%S.zip"
    return datetime.strptime(name, "%Y-%m-%d_%H-%M-%S.zip")


def get_backups():
    backups = []
    for file in os.listdir(BACKUP_PATH):
        if file.endswith(".zip"):
            timestamp = parse_name(file)
            day = timestamp.strftime("%Y-%m-%d")
            hour = timestamp.strftime("%H:%M:%S")
            backups.append({"name": file, "day": day, "hour": hour})
    return backups
