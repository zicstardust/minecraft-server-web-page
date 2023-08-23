import sys
sys.path.insert(0, '/home/mcuser/Home-MC/web')

activate_this = '/home/mcuser/.local/share/virtualenvs/minecraft-server-web-page-lrOPK7zN/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import app as application