from flask import render_template, Blueprint

blueprint = Blueprint('test', __name__)


@blueprint.route('/')
@blueprint.route('/test')
def index():
    return render_template("index.html")
