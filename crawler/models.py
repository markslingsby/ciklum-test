from django.db import models
from django.utils.timezone import now


class Tag(models.Model):
    name = models.CharField(max_length=100)
    words = models.CharField(max_length=100, blank=True)
    updated = models.DateTimeField(auto_now=True, default=now)
    relevancy = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s: %s" % (self.name, self.words)

class WebPage(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True, default=now)
    tags = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return "'%s' @ '%s'>" % (self.url, self.title)
