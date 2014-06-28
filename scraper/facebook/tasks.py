import requests
from BeautifulSoup import BeautifulSoup as Soup

from scraper import make_celery, create_app
from scraper.models.twitter import Twitter

app = create_app()
celery = make_celery(app)


@celery.task()
def scrape_twitter(username):
    response = requests.get(app.config["TWITTER_BASE_URL"] + username)
    if response.status_code != 200:
        return None

    profile = Twitter.query.filter_by(username=username).first()
    if not profile:
        profile = Twitter(username=username)

    html = Soup(response.content)

    obj = html.find("li", {"class": "ProfileNav-item ProfileNav-item--followers"})
    profile.popularity_index = int(obj.findAll("span")[-1].text)

    obj = html.find("h1", {"class": "ProfileHeaderCard-name"})
    profile.full_name = obj.text

    obj = html.find("p", {"class": "ProfileHeaderCard-bio u-dir"})
    profile.description = obj.text

    obj = html.find("img", {"class": "ProfileAvatar-image "})
    profile.picture_url = obj["src"]

    profile.save()
