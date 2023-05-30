# Import flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from lib import get_server_status


# Configure for port 80
app = Flask(__name__)


@app.route("/")
def index():
    server_status = get_server_status()
    return render_template("index.html", server_status=server_status)


app.run(host="mc.parcerisa.xyz", port=80)
