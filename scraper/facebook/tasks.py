import json
import requests

from scraper import make_celery
from scraper.models.facebook import Facebook

celery = make_celery()


@celery.task
def scrape_facebook(username):
    facebook_base_query = "?q=SELECT%20friend_count%20,%20name,%20pic%20%20FROM%20user%20WHERE%20username='{0}'"
    response = requests.get('https://graph.facebook.com/fql' + facebook_base_query.format(username))

    if response.status_code != 200:
        return False

    data = json.loads(response.content)["data"]
    if not len(data):
        return False
    data = data[0]

    profile = Facebook.query.filter_by(username=username).first()
    if not profile:
        profile = Facebook(username=username)

    profile.popularity_index = data["friend_count"]
    profile.description = ""
    profile.full_name = data["name"]
    profile.picture_url = data["pic"]

    return profile.save()
