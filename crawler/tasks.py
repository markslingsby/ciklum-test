# coding=UTF-8
from __future__ import absolute_import
import urllib2
import re

from bs4 import BeautifulSoup
from celery.utils.log import get_task_logger

from monitoring.celeryapp import app
from crawler.models import Tag, WebPage


@app.task
def tag_banners():
    tag = Tag.objects.get(name="banners")
    ad_hosts = ['adexprt', 'exoclick', 'doubleclick', 'google_ads']

    for page in WebPage.objects.all():
        soup = BeautifulSoup(page.body)

        if len(soup.find_all("iframe", src=re.compile("|".join(ad_hosts)))) >= tag.relevancy:
            page.tags.add(tag)


@app.task
def tag_words(tag):
    for page in WebPage.objects.all():
        for word in tag.words.split(","):
            if word in page.body:
                page.tags.add(tag)
                break

@app.task
def crawl(webpage_list):
    for url in webpage_list:
        wp, _ = WebPage.objects.get_or_create(url=url)

        wp.body = urllib2.urlopen(url).read()

        soup = BeautifulSoup(wp.body)

        wp.title = soup.title.string

        desc = soup.find("meta", {'name': 'description'})

        if desc:
            wp.description = desc.get('content', '')

        wp.save()
