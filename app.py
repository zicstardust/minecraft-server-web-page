from flask import Flask, render_template
from lib.backups import get_backups
from lib.playtime import get_player_playtime_hours
from lib.server_status import get_server_status

# Configure for port 80
app = Flask(__name__)


@app.route("/")
def index():
    server_status = get_server_status()
    return render_template("index.html", server_status=server_status)


@app.route("/backups")
def backups():
    backups = get_backups()
    return render_template("backups.html", backups=backups)


@app.route("/playtime")
def playtime():
    return render_template("playtime.html")


@app.route("/api/playtime")
def api_playtime():
    players, playtime = get_player_playtime_hours()
    return {"players": players, "playtime": playtime}


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)
    app.run()
