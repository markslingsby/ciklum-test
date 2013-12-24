from django.core.management.base import BaseCommand, CommandError
from crawler.models import Tag
from crawler.tasks import tag_words

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Starting tagging words')

        for tag in Tag.objects.exclude(words=""):
            tag_words.delay(tag)

        self.stdout.write('Successfully finished')
