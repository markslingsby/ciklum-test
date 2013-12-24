from django.core.management.base import BaseCommand, CommandError
from crawler.models import Tag
from crawler.tasks import tag_banners

class Command(BaseCommand):
    def handle(self, *args, **options):
        tag_banners.delay()
