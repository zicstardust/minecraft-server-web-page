import os
from datetime import datetime

BACKUP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "backup", "backups"))


def parse_name(name):
    "Name is in format %Y-%m-%d_%H-%M-%S.zip"
    timestamp = datetime.strptime(name, "%Y-%m-%d_%H-%M-%S.zip")
    day = timestamp.strftime("%Y-%m-%d")
    hour = timestamp.strftime("%H:%M:%S")
    return {"name": name, "day": day, "hour": hour}


def get_backups():
    backups = []
    for folder in os.listdir(BACKUP_PATH):
        if os.path.isdir(os.path.join(BACKUP_PATH, folder)):
            section = {"name": folder, "backups": []}
            for file in os.listdir(os.path.join(BACKUP_PATH, folder)):
                if file.endswith(".zip"):
                    section["backups"].append(parse_name(file))
            backups.append(section)
    return backups
