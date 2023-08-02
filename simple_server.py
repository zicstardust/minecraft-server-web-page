# Import flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from lib.server_status import get_server_status
from lib.checkpoints import get_world_checkpoints
from lib.backups import get_backups
from lib.users import handle_login, handle_signup, setup_login_manager
from generate_secret_key import KEY_FILE
from lib.sql import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, setup_db

import os


# Configure for port 80
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
setup_db(app)
setup_login_manager(app)

# Configure for secret key
with open(KEY_FILE, "rb") as f:
    app.secret_key = f.read()


@app.route("/")
def index():
    server_status = get_server_status()
    return render_template("index.html", server_status=server_status)


@app.route("/checkpoints")
def checkpoints():
    world_checkpoints = get_world_checkpoints()
    return render_template("checkpoints.html", checkpoints=world_checkpoints)


@app.route("/backups")
def backups():
    backups = get_backups()
    return render_template("backups.html", backups=backups)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")
    return handle_login(username, password)


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirm = request.form.get("password-confirm")
    return handle_signup(username, password, password_confirm)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
