import requests
import json

from scraper import make_celery, create_app
from scraper.models.facebook import Facebook

app = create_app()
celery = make_celery(app)


@celery.task()
def scrape_facebook(username):
    facebook_base_query = "?q=SELECT%20friend_count%20,%20name,%20pic%20%20FROM%20user%20WHERE%20uid='{0}'"
    response = requests.get(app.config["FACEBOOK_BASE_URL"] + facebook_base_query.format(username))

    if response.status_code != 200:
        return None

    profile = Facebook.query.filter_by(username=username).first()
    if not profile:
        profile = Facebook(username=username)

    data = json.loads(response.content)["data"][0]

    profile.popularity_index = data["friend_count"]
    profile.description = ""
    profile.full_name = data["name"]
    profile.picture_url = data["pic"]

    profile.save()
