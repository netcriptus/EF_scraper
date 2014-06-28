DEBUG = True
CSRF_ENABLED = True
SQLALCHEMY_DATABASE_URI = "mysql://scraper:scraper@127.0.0.1/scraper"
CELERY_BROKER_URL = 'redis://localhost:6379',
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
FACEBOOK = {'consumer_key': '1503901056508224',
            'consumer_secret': 'd255714adb8bd73ce7a0c56572ca4f98'}
TWITTER_BASE_URL = 'http://twitter.com/'
