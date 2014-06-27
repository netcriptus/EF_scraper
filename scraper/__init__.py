
from uuid import uuid4
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from celery import Celery

db = SQLAlchemy()


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
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
    celery = make_celery(app)

    # Blueprints
    # from taco.oauth2 import oauth2
    # from taco.client import client
    # from taco.login import login
    # from taco.user import user
    from scraper.controllers import controllers
    #
    # app.register_blueprint(oauth2)
    # app.register_blueprint(client)
    # app.register_blueprint(login)
    # app.register_blueprint(user)
    app.register_blueprint(controllers)

    app.secret_key = str(uuid4())

    return app
