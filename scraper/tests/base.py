from scraper import db
from flask import g
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
        g.db = db
        g.db.init_app(self.app)
        g.db.drop_all(app=self.app)
        g.db.create_all(app=self.app)

    def teardown(self):
        g.db = db
        g.db.session.remove()
        g.db.drop_all(app=self.app)
