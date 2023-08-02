from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .sql import db


class User(UserMixin, db.Model):
    "id, username, password"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"


def handle_login(username, password):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash("User does not exist. <a href='{}'>Sign up</a> instead?".format(url_for("signup")))
        return redirect(url_for("login"))
    elif not check_password_hash(user.password, password):
        flash("Incorrect password")
        return redirect(url_for("login"))
    else:
        # Log the user in
        login_user(user)
        return redirect(url_for("index"))


def handle_signup(username, password, password_confirm):
    if not username:
        flash("Please provide a username")
        return redirect(url_for("signup"))
    elif not password:
        flash("Please provide a password")
        return redirect(url_for("signup"))
    elif not password_confirm:
        flash("Please confirm your password")
        return redirect(url_for("signup"))
    elif password != password_confirm:
        flash("Passwords do not match")
        return redirect(url_for("signup"))
    elif len(password) < 8:
        flash("Password must be at least 8 characters long")
        return redirect(url_for("signup"))
    elif User.query.filter_by(username=username).first():
        flash("Username already exists")
        return redirect(url_for("signup"))
    else:
        user = User(username=username, password=generate_password_hash(password))

        db.session.add(user)
        db.session.commit()

        # Log the user in
        login_user(user)
        return redirect(url_for("index"))
