from django.contrib import admin

# Register your models here.
from crawler.models import WebPage, Tag


class WebPageAdmin(admin.ModelAdmin):
    list_display = ('url', 'title')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'words')

admin.site.register(WebPage, WebPageAdmin)
admin.site.register(Tag, TagAdmin)
