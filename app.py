import os
from flask import Flask, render_template
from waitress import serve
from lib.server_status import get_server_status

app = Flask(__name__)


@app.route("/")
def index():
    server_status = get_server_status()
    return render_template("index.html",
                           server_status=server_status,
                           server_name=(os.environ["SERVER_NAME"]),
                           server_uri_java=(os.environ["SERVER_URI_JAVA"]),
                           server_uri_bedrock=(os.environ["SERVER_URI_BEDROCK"]),
                           server_map_url=(os.environ["SERVER_MAP_URL"]),
                           discord_link=(os.environ["DISCORD_LINK"])
                           )

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080)
