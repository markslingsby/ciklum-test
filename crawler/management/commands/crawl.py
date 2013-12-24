from django.core.management.base import BaseCommand, CommandError
from monitoring.settings import webpage_list
from crawler.views import crawl

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Starting crawling %d urls' % len(webpage_list))

        crawl(webpage_list)

        self.stdout.write('Successfully finished')
