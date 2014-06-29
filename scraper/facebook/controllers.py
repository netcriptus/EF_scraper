
from flask import make_response, jsonify

from . import facebook
from scraper.facebook.tasks import scrape_facebook
from scraper.models.facebook import Facebook


@facebook.route("/<username>", methods=["GET"])
def get_user_info(username):
    profile = Facebook.query.filter_by(username=username).first()

    if not profile:
        scrape_facebook.delay(username)
        resp = make_response("processing request", 202)
    else:
        resp = jsonify(name=profile.full_name, picture_url=profile.picture_url,
                       description=profile.description, popularity_index=profile.popularity_index)
    return resp
