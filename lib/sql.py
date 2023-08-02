from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://web_page:web_page@localhost/minecraft_server_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()


def setup_db(app):
    db.init_app(app)
    db.create_all(app=app)


# MODELS:


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


class User(db.Model):
    "id, username, password"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
