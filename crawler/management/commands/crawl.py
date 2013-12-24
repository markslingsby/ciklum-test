from django.core.management.base import BaseCommand, CommandError
from monitoring.settings import webpage_list
from crawler.tasks import crawl

class Command(BaseCommand):
    def handle(self, *args, **options):
        crawl.delay(webpage_list)
