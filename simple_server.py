# Import flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from lib.server_status import get_server_status
from lib.checkpoints import get_world_checkpoints
from lib.backups import get_backups
from web.lib.users import handle_login

# Configure for port 80
app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
