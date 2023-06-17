# Import flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from lib.server_status import get_server_status


# Configure for port 80
app = Flask(__name__)


@app.route("/")
def index():
    server_status = get_server_status()
    return render_template("index.html", server_status=server_status)


@app.route("/checkpoints")
def checkpoints():
    return render_template("checkpoints.html", checkpoints=checkpoints)


# @app.route("/chat")
# def chat():
#     chat = get_server_chat()
#     return render_template("chat.html", chat=chat)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
