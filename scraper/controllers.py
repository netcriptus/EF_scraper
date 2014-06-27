from flask import Blueprint

controllers = Blueprint('controllers', __name__)


@controllers.route("/health", methods=["GET"])
def health():
    return "ok", 200
