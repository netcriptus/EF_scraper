from flask import Blueprint

facebook = Blueprint('facebook', __name__, url_prefix='/facebook')

import controllers
