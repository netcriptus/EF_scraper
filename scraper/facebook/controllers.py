
from flask import make_response

from . import twitter
from tasks import scrape_twitter
from scraper.models.twitter import Twitter


@twitter.route("/<username>", methods=["GET"])
def get_user_info(username):
    profile = Twitter.query.filter_by(username=username).first()

    # update our data everytime this profile is requested
    scrape_twitter.delay(username)

    if not profile:
        resp = make_response("processing request", 202)
    else:
        resp = make_response(profile, 200)
    return resp
