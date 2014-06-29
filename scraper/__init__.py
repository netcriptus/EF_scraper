
from uuid import uuid4
from celery import Celery
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


def create_app():
    app = Flask(__name__)

    app.config.from_object('scraper.settings.base')
    db.init_app(app)

    # Blueprints
    from scraper.twitter import twitter
    from scraper.facebook import facebook
    from scraper.controllers import controllers

    # Register blueprints
    app.register_blueprint(twitter)
    app.register_blueprint(facebook)
    app.register_blueprint(controllers)

    app.secret_key = str(uuid4())

    return app
