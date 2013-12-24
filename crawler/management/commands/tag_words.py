from django.core.management.base import BaseCommand, CommandError
from crawler.models import Tag
from crawler.tasks import tag_words

class Command(BaseCommand):
    def handle(self, *args, **options):
        for tag in Tag.objects.exclude(words=""):
            tag_words.delay(tag)
