from .sql import db


class Checkpoint(db.Model):
    "id, name, coords, date_added"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    coords = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Checkpoint {self.name} {self.coords} {self.date_added}>"

    # Set tablename
    __tablename__ = "checkpoints"


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
