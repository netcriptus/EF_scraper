import requests
from BeautifulSoup import BeautifulSoup as Soup

from scraper import make_celery
from scraper.models.twitter import Twitter

celery = make_celery()

@celery.task
def scrape_twitter(username):
    response = requests.get('http://twitter.com/' + username)
    if response.status_code != 200:
        return None

    profile = Twitter.query.filter_by(username=username).first()
    if not profile:
        profile = Twitter(username=username)

    html = Soup(response.content)

    obj = html.find("li", {"class": "ProfileNav-item ProfileNav-item--followers"})
    profile.popularity_index = obj.findAll("span")[-1].text if obj else "0"

    obj = html.find("h1", {"class": "ProfileHeaderCard-name"})
    profile.full_name = obj.text if obj else ""

    obj = html.find("p", {"class": "ProfileHeaderCard-bio u-dir"})
    profile.description = obj.text if obj else ""

    obj = html.find("img", {"class": "ProfileAvatar-image "})
    profile.picture_url = obj["src"] if obj else ""

    profile.save()
