# coding=UTF-8
import urllib2
from bs4 import BeautifulSoup
from crawler.models import WebPage


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
