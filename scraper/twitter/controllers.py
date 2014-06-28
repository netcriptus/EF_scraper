
from flask import make_response, jsonify

from . import twitter
from tasks import scrape_twitter
from scraper.models.twitter import Twitter


@twitter.route("/<username>", methods=["GET"])
def get_user_info(username):
    profile = Twitter.query.filter_by(username=username).first()

    if not profile:
        scrape_twitter(username)
        resp = make_response("processing request", 202)
    else:
        resp = jsonify(name=profile.full_name, picture_url=profile.picture_url,
                       description=profile.description, popularity_index=profile.popularity_index)
    return resp
