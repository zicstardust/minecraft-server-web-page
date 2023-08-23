import sys
sys.path.insert(0, '/var/www/minecraft-server-web-page')

activate_this = '/home/mcuser/.local/share/virtualenvs/minecraft-server-web-page-lrOPK7zN'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import app as application