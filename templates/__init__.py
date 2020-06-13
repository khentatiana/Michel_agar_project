from flask import Flask

app = Flask(__name__, static_folder="./public", template_folder="./static")

from templates.dir.views import blueprint

app.register_blueprint(blueprint)
