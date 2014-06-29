from scraper import db
from flask.ext.testing import TestCase
from scraper import create_app


class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://scraper:scraper@127.0.0.1/scraper_test"
        app.testing = True
        return app

    def setup(self):
        db.create_all()

    def teardown(self):
        db.session.remove()
        db.drop_all()
