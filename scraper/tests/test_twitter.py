from scraper import db
from scraper.tests import BaseTestCase


class AuthorizationTest(BaseTestCase):

    def test_asyncronous_response(self):
        db.create_all()
        response = self.client.get("/twitter/fernando_cezar")
        self.assertEqual(response.status_code, 202)
        db.session.remove()
        db.drop_all()

    def test_parsed_profile_response(self):
        db.create_all()
        response = self.client.get("/twitter/fernando_cezar")
        self.assertEqual(response.status_code, 202)
        response = self.client.get("/twitter/fernando_cezar")
        self.assertEqual(response.status_code, 200)
        db.session.remove()
        db.drop_all()
