DEBUG = True
CSRF_ENABLED = True
SQLALCHEMY_DATABASE_URI = "mysql://scraper:scraper@127.0.0.1/scraper"
BROKER_URL = 'redis://localhost:6379',
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_IMPORTS = ("tasks",)
FACEBOOK_BASE_URL = 'https://graph.facebook.com/fql'
TWITTER_BASE_URL = 'http://twitter.com/'
