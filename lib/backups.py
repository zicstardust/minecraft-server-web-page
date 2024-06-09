import os
import pathlib
from datetime import datetime


def parseFullBackup(rel_path: pathlib.Path):
    "Name is in format %Y-%m-%d_%H-%M-%S.zip"
    name = rel_path.stem
    date = datetime.strptime(name, "%Y-%m-%d_%H-%M-%S.zip")
    day = date.strftime("%Y-%m-%d")
    hour = date.strftime("%H:%M:%S")
    timestamp = date.timestamp()

    return {"name": name, "day": day, "hour": hour, "timestamp": timestamp, "type": "full", "rel_path": str(rel_path)}


def parseDifferentialBackup(rel_path: pathlib.Path):
    "Name is in format backup_%Y-%m-%d_%H-%M-%S-{type}.zip, where type can be full or partial"
    name = rel_path.stem
    if "full" in name:
        t_ = "full"
        name = name.replace("-full", "")
    elif "partial" in name:
        t_ = "partial"
        name = name.replace("-partial", "")
    else:
        t_ = "unknown"
    dt = datetime.strptime(name, "backup_%Y-%m-%d_%H-%M-%S.zip")
    day = dt.strftime("%Y-%m-%d")
    hour = dt.strftime("%H:%M:%S")
    timestamp = dt.timestamp()
    return {"name": name, "day": day, "hour": hour, "timestamp": timestamp, "type": t_, "rel_path": str(rel_path)}


def get_backups():
    backups_path = pathlib.Path(os.environ["BACKUPS_PATH"])
    backups = []
    for folder in backups_path.iterdir():
        if not folder.is_dir():
            continue

        if all(file.suffix == ".zip" for file in folder.iterdir()):
            section = {
                "name": folder.name,
                "backups": list(
                    parseFullBackup(file.resolve().relative_to(backups_path)) for file in folder.iterdir()
                ),
                "backup_type": "full",
            }
            backups.append(section)
        else:
            # For now, we'll suppose this is a backup done with ftb-backup
            worlds = list(filter(pathlib.Path.is_dir, folder.iterdir()))
            for world in worlds:
                differential = world / "differential"
                if len(list(differential.iterdir())) > 0:
                    section = {
                        "name": f"{folder.name} world '{world.name}' differentials",
                        "backups": list(
                            parseDifferentialBackup(file.resolve().relative_to(backups_path))
                            for file in differential.iterdir()
                        ),
                        "backup_type": "differential",
                    }
                    backups.append(section)

        section["backups"].sort(key=lambda x: x["timestamp"], reverse=True)

    return backups


def get_backup_folder_file(rel_path: str) -> tuple[str, str] | None:
    rel_path = pathlib.Path(rel_path)
    backups_path = pathlib.Path(os.environ["BACKUPS_PATH"])
    path = backups_path / rel_path
    if not path.exists():
        return None
    return str(path.parent), path.name
