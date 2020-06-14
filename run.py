from flask import Flask
from views import blueprint

app = Flask(__name__, static_folder="static", template_folder="templates")

app.register_blueprint(blueprint)
app.config.from_object('configurations.DevelopmentConfig')

app.run()
