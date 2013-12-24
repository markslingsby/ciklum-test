# coding=UTF-8
from os import getcwd
from django.test import TestCase
from django.conf import settings
from django.core import management

import monitoring
from crawler.tasks import tag_words, crawl
from crawler.models import WebPage, Tag


cwd, fixtures = getcwd(), ('python.org.html', 'lacoon.com.html', 'yandex.ru.html', 'thepiratebay.org.html')
test_webpage_list = ["file:%s/crawler/fixtures/%s" % (cwd, fname) for fname in fixtures]


class TestTagging(TestCase):
    fixtures = ['testdata.yaml']

    def test_python_parsed_programming(self):
        python = WebPage.objects.get(url='http://python.org')
        self.assertEqual(len(python.tags.all()), 0)

        management.call_command('tag_words', verbosity=0, interactive=False)

        pt = Tag.objects.get(name="programming")

        self.assertEqual(python.tags.all()[0], pt)
        self.assertEqual(len(python.tags.all()), 1)

    def test_banners(self):
        two_banners = WebPage.objects.get(url='http://test.url')
        tpb = WebPage.objects.get(url='http://thepiratebay.org')
        self.assertEqual(len(two_banners.tags.all()), 0)
        self.assertEqual(len(tpb.tags.all()), 0)

        management.call_command('tag_banners', verbosity=0, interactive=False)

        pt = Tag.objects.get(name="programming")
        banners = Tag.objects.get(name="banners")
        torrents = Tag.objects.get(name="torrents")

        self.assertEqual(len(two_banners.tags.all()), 0)

        self.assertTrue(banners in tpb.tags.all())
        self.assertEqual(len(tpb.tags.all()), 1)

        management.call_command('tag_words', verbosity=0, interactive=False)
        self.assertTrue(torrents in tpb.tags.all())
        self.assertEqual(len(tpb.tags.all()), 2)


class TestCrawler(TestCase):
    def test_crawl_pages(self):
        monitoring.settings.webpage_list= test_webpage_list

        self.assertFalse(WebPage.objects.all())

        management.call_command('crawl', verbosity=0, interactive=False)

        python = WebPage.objects.get(url=test_webpage_list[0])
        self.assertEqual(python.title, u'Python Programming Language \u2013 Official Website')

        lacoon = WebPage.objects.get(url=test_webpage_list[1])
        self.assertEqual(lacoon.description, 'Blueprint: ')

        ya = WebPage.objects.get(url=test_webpage_list[2])
        assert(u'Дизайн' in ya.body)
