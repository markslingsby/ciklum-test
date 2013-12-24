Installation
============
$ mkvirtualenv lacoon
$ pip install -r requirements.txt
$ python manage.py syncdb
$ python manage.py migrate
$ python manage.py runserver

run celery worker thread in separate window(python backend, no redis needed)
$ workon lacoon
$ python monitoring/celeryapp.py worker



Management commands
===================
$ python manage.py crawl - asynchronously get pages from urls, defined in settings.py
$ python manage.py tag_words - asynchronously tag pages with tags
$ python manage.py tag_banners - asynchronously tag pages with 3 and more banners(example defined as crawler.models.Tag.relevancy with 'banners' name in fixture)



Testing
=======
python manage.py test



Task description
================
The goal of this test is to create web monitoring system based on Django
infrastructure.

The system should include 3 major parts:

1) Data crawler - will connect to the list of web pages based on
configuration file, collect the page content and store it with the meta-data to
the DB.

2) Data analysis - will asynchronously execute the list of detection
engines (the list should be easily managed by external operator). The engines
should generate tags in case of data detection. Each engine may generate any
number of tags.

   For the demo please create 2 scripts:
    - script that looks for list of words and if the word exists creates the
   relevant tag.
    - a script that looks for banners and if the page includes more than x
   banners creates a tag.


3) Data presentation - will allow an operator to see the list of
monitored sites, meta data and tags. Optional: The system will allow an operator
to remove and add manually tags from pre-defined list of tags.)
