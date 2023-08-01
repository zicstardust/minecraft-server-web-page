import os
from datetime import datetime

BACKUP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "backup", "backups"))


def parse_name(name):
    "Name is in format %Y-%m-%d_%H-%M-%S.zip"
    return datetime.strptime(name, "%Y-%m-%d_%H-%M-%S.zip")


def get_backups():
    backups = []
    for file in os.listdir(BACKUP_PATH):
        if os.path.isdir(os.path.join(BACKUP_PATH, file)):
            section = {"name": file, "backups": []}
            for backup in os.listdir(os.path.join(BACKUP_PATH, file)):
                if file.endswith(".zip"):
                    timestamp = parse_name(backup)
                    day = timestamp.strftime("%Y-%m-%d")
                    hour = timestamp.strftime("%H:%M:%S")
                    section["backups"].append({"name": backup, "day": day, "hour": hour})
            backups.append(section)
    return backups
