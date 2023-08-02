from .sql import Checkpoint


def get_world_checkpoints():
    checkpoints = Checkpoint.query.all()

    checkpoints.sort(key=lambda x: x.date_added, reverse=True)  # Sort by date added

    res = []

    for checkpoint in checkpoints:
        res.append(
            {
                "name": checkpoint.name,
                "coords": checkpoint.coords,
                "day": checkpoint.date_added.strftime("%d/%m/%Y"),
                "hour": checkpoint.date_added.strftime("%H:%M:%S"),
            }
        )

    return res
