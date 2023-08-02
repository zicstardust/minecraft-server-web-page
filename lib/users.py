from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from . import sql


CREATE_USER_QUERY = "INSERT INTO users (username, password) VALUES ('{username}', '{password}');"
GET_USER_QUERY = "SELECT * FROM users WHERE username='{username}';"

get_user = lambda username: sql.connection.execute(GET_USER_QUERY.format(username=username))
create_user = lambda username, password: sql.connection.execute(
    CREATE_USER_QUERY.format(username=username, password=password)
)


def handle_login(username, password):
    user = get_user(username)

    if not user:
        flash("User does not exist")
        return redirect(url_for("login"))
    elif not check_password_hash(user[2], password):
        flash("Incorrect password")
        return redirect(url_for("login"))
    else:
        # Log the user in
        return redirect(url_for("index"))


def handle_user_creation(username, password):
    if not username:
        flash("Please provide a username")
        return redirect(url_for("signup"))
    elif not password:
        flash("Please provide a password")
        return redirect(url_for("signup"))
    elif len(password) < 8:
        flash("Password must be at least 8 characters long")
        return redirect(url_for("signup"))
    elif get_user(username):
        flash("Username already exists")
        return redirect(url_for("signup"))
    else:
        create_user(username, generate_password_hash(password))

        # Log the user in
        return handle_login(username, password)
