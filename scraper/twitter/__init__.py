from flask import Blueprint

twitter = Blueprint('twitter', __name__, url_prefix='/twitter')

import controllers
