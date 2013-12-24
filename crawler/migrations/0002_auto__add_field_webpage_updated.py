# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WebPage.updated'
        db.add_column(u'crawler_webpage', 'updated',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WebPage.updated'
        db.delete_column(u'crawler_webpage', 'updated')


    models = {
        u'crawler.webpage': {
            'Meta': {'object_name': 'WebPage'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['crawler']