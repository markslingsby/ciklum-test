# coding=UTF-8
from os import getcwd
from django.test import TestCase

from crawler.views import crawl
from crawler.models import WebPage


class TestCrawler(TestCase):
    def test_crawl_pages(self):
        cwd, fixtures = getcwd(), ('python.org.html', 'lacoon.com.html', 'yandex.ru.html')
        test_webpage_list = ["file:%s/crawler/fixtures/%s" % (cwd, fname) for fname in fixtures]

        crawl(test_webpage_list)

        python = WebPage.objects.get(url=test_webpage_list[0])
        self.assertEqual(python.title, u'Python Programming Language \u2013 Official Website')

        lacoon = WebPage.objects.get(url=test_webpage_list[1])
        self.assertEqual(lacoon.description, 'Blueprint: ')

        ya = WebPage.objects.get(url=test_webpage_list[2])
        assert(u'Дизайн' in ya.body)
