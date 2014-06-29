from scraper.twitter.tasks import scrape_twitter
from scraper.models.twitter import Twitter
from scraper.tests.base import BaseTestCase


class TwitterTest(BaseTestCase):

    def test_asyncronous_response(self):
        self.setup()
        response = self.client.get("/twitter/fernando_cezar")
        self.assertEqual(response.status_code, 202)
        self.teardown()

    def test_parsed_profile_response(self):
        self.setup()
        profile = Twitter(username="fernando_cezar")
        profile.save()
        response = self.client.get("/twitter/fernando_cezar")
        self.assertEqual(response.status_code, 200)
        self.teardown()

    def test_scrape_tool(self):
        self.setup()
        profile = Twitter.query.filter_by(username="fernando_cezar").first()
        self.assertEqual(profile, None)
        scrape_twitter("fernando_cezar")
        profile = Twitter.query.filter_by(username="fernando_cezar").first()
        self.assertNotEqual(profile, None)
        self.teardown()

    def test_profile_do_not_exist(self):
        # TODO: this test REALLY should be mocked
        self.setup()
        profile = Twitter.query.filter_by(username="fslgkjbfds").first()
        self.assertEqual(profile, None)
        return_code = scrape_twitter("fslgkjbfds")
        self.assertEqual(return_code, False)
        profile = Twitter.query.filter_by(username="fslgkjbfds").first()
        self.assertEqual(profile, None)
        self.teardown()
