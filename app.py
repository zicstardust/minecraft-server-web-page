from os import environ
from flask import Flask, render_template
from lib.background_image import define_background_image
from lib.server_status import get_server_status

define_background_image()

app = Flask(__name__)


@app.route("/")
def index():
    server_status = get_server_status()
    return render_template("index.html",
                           server_status=server_status,
                           server_name=environ.get("SERVER_NAME","Minecraft Server"),
                           server_uri_java=environ.get("SERVER_URI_JAVA","localhost"),
                           server_uri_bedrock=environ.get("SERVER_URI_BEDROCK",""),
                           server_map_url=environ.get("SERVER_MAP_URL",""),
                           discord_link=environ.get("DISCORD_LINK","")
                           )

def production():
    return app


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    app.run(debug=True)
