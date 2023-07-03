from .sql import sql


get_query = "SELECT id, name, coords, date_added FROM checkpoints;"


def get_world_checkpoints():
    checkpoints = sql(get_query)

    checkpoints.sort(key=lambda x: x[3], reverse=True)  # Sort by date added

    res = []

    for checkpoint in checkpoints:
        res.append(
            {
                "name": checkpoint[1],
                "coords": checkpoint[2],
                "day": checkpoint[3].strftime("%d/%m/%Y"),
                "hour": checkpoint[3].strftime("%H:%M:%S"),
            }
        )

    return res
