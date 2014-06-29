#!/usr/bin/env python
import os
import nose
from flask.ext.script import Manager

from scraper import create_app

manager = Manager(create_app)


@manager.command
def test():
    "run all tests in test folder"
    nose.run(argv=["", "--exe", "--rednose"])


@manager.command
def init_db():
    '''Create the local database for development'''
    from scraper import db
    db.create_all()


@manager.command
def drop_db():
    '''Drop the local database for development'''
    from scraper import db
    db.drop_all()


@manager.command
def migration_upgrade(commit='head'):
    '''Migrate database structure'''
    from alembic.config import Config
    from alembic.command import upgrade

    config = Config(os.path.normpath(os.path.abspath(__file__) + '/../alembic.ini'))
    config.set_main_option("script_location", 'alembic')

    upgrade(config, commit)


@manager.command
def migration_downgrade(commit):
    '''Migrate database structure'''
    from alembic.config import Config
    from alembic.command import downgrade

    config = Config(os.path.normpath(os.path.abspath(__file__) + '/../alembic.ini'))
    config.set_main_option("script_location", 'alembic')

    downgrade(config, commit)


if __name__ == "__main__":
    manager.run()
