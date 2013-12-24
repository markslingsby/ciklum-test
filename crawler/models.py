from django.db import models
from datetime import datetime


class WebPage(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    body = models.TextField()
    updated = models.DateField(auto_now=True, default=datetime.now)
