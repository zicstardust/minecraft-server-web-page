from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from lib.server_status import get_server_status
from lib.checkpoints import get_world_checkpoints
from lib.backups import get_backups
from web.lib.users import handle_login


def handle_login(username, password):
    if username == "admin" and password == "admin":
        return redirect(url_for("index"))
    else:
        flash("Invalid credentials")
        return redirect(url_for("login"))
