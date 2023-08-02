from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://web_page:web_page@localhost/minecraft_server_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()


def setup_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
