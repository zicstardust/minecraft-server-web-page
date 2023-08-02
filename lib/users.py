from flask import Flask, render_template, request, redirect, url_for, flash, jsonify


def handle_login(username, password):
    if username == "admin" and password == "admin":
        return redirect(url_for("index"))
    else:
        flash("Invalid credentials")
        return redirect(url_for("login"))
