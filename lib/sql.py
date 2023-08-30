from flask_sqlalchemy import SQLAlchemy
from secrets.db_credentials import DB_USER, DB_PASSWORD

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@localhost/minecraft_server_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()


def setup_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
