from django.contrib import admin

# Register your models here.
from crawler.models import WebPage

class WebPageAdmin(admin.ModelAdmin):
    list_display = ('url', 'title')

admin.site.register(WebPage, WebPageAdmin)
