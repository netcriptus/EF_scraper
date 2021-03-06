# Web Scraper

# Dependecies

In order to run this software, you need to have installed on your machine:
- Python (2.6 or superior)
- Redis
- MySQL

It is also recommended, but not mandatory:
- virtualenv
- pip or easy_install

# Installing the requirements

Inside the main folder of the project
 ```
 pip install -r requirements.txt
 ```

 ### Initiating the database

 On the `mysql` shell:

 ```
 CREATE DATABASE scraper;
 CREATE USER 'scraper'@'localhost' IDENTIFIED BY 'scraper';
 GRANT ALL ON scraper.* TO 'scraper'@'localhost' IDENTIFIED BY 'scraper';
 ```

Then, on the main folder of the project once again:
```
./manage.py init_db
```

# Running tests

On the main folder of the project:
```
./manage.py test
........
-----------------------------------------------------------------------------
8 tests run in 6.5 seconds (8 tests passed)
```

# Running the project on a local environment

```
./manage.py runserver
```

You will also need a celery worker running. There should be many better ways to do this,
but due to time contraints, the following not-so-elegant line should put one worker up:

```
celery -A scraper.twitter.tasks -A scraper.facebook.tasks worker --broker=redis://localhost:6379
```

# API calls

### GET /health
This returns a `200 OK`. It is used for some services (like pingdom) to asure the app is up and running.

### GET /twitter/:username
This will scrape this user profile on Twitter. The `username` parameter MUST be the exact username on Twitter.

If this is not already scraped, the return will be a `202 processing request`. Once the processing is finished,
the next requests to this URL will return a json response with the data scraped from this user profile. E.g.:

__GET /twitter/fernando_cezar__
```
{
  "description": "",
  "name": "Fernando Cezar",
  "picture_url": "https://pbs.twimg.com/profile_images/36564982/Comic_book_400x400.jpg",
  "popularity_index": "61"
}
```

### GET /facebook/:username
This will scrape this user profile on Facebook. The `username` parameter MUST be the exact username on Facebook.

If this is not already scraped, the return will be a `202 processing request`. Once the processing is finished,
the next requests to this URL will return a json response with the data scraped from this user profile. E.g.:

__GET /facebook/fcezar1__
```
{
  "description": "",
  "name": "Fernando Cezar",
  "picture_url": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xap1/t1.0-1/s100x100/1525514_10201201796826206_46543603_n.jpg",
  "popularity_index": "94"
}
```

# Caveats

- Facebook has many privacy options for their users. Therefore it will not always be possible to scrape all informations,
and there is no easy workaround for this issue. The `popularity index` information, for instance, may be protected and
will not be parsed.

- Once past 100 thousand followers, the Twitter page adds a word or a letter after the number. So, for instance, if
one user has 120.000 followers, Twitter will display `120k`, or `120 Mil` in Brazil (it depends on where the request
comes from). It could be tricky to parse this to a number, due to geolocation changes, so the app actually displays it as received from Twitter.

# TODO
- The `/health` resource should run some checkups before returning a `200 OK`. For now it only returns `200 OK` no matter
what.

- The DRY principle wasn't very respected. Twitter and Facebook scraper functions are not much alike, but apart from that, much of
the code is exactly the same for both of them. The next step here would be to refactor the code and merge most of it.
For instance, the models would possibly merge to one more general model, with an additional `source` field, indicating where
did the data come from.

- Some workaround had to be done in some points. The test classes, for some reason not figured out yet, are not running
the `setup` and `teardown` functions on their own, so those methods had to be manually called. Also, the celery worker
is not respecting the configuration file, therefore the line starting the worker had to have some extra options, like
the `-A` and `--broker`.

- There was not enough time to put together a deploy script. This would be done using Fabric, configuring a `fabfile.py`.
