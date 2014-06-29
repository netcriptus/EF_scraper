from scraper.facebook.tasks import scrape_facebook
from scraper.models.facebook import Facebook
from scraper.tests.base import BaseTestCase


class FacebookTest(BaseTestCase):

    def test_asyncronous_response(self):
        self.setup()
        response = self.client.get("/facebook/fcezar1")
        self.assertEqual(response.status_code, 202)
        self.teardown()

    def test_parsed_profile_response(self):
        self.setup()
        profile = Facebook(username="fcezar1")
        profile.save()
        response = self.client.get("/facebook/fcezar1")
        self.assertEqual(response.status_code, 200)
        self.teardown()

    def test_scrape_tool(self):
        self.setup()
        profile = Facebook.query.filter_by(username="fcezar1").first()
        self.assertEqual(profile, None)
        scrape_facebook("fcezar1")
        profile = Facebook.query.filter_by(username="fcezar1").first()
        self.assertNotEqual(profile, None)
        self.teardown()
