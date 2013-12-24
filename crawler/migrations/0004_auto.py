# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field tags on 'WebPage'
        m2m_table_name = db.shorten_name(u'crawler_webpage_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('webpage', models.ForeignKey(orm[u'crawler.webpage'], null=False)),
            ('tag', models.ForeignKey(orm[u'crawler.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['webpage_id', 'tag_id'])


    def backwards(self, orm):
        # Removing M2M table for field tags on 'WebPage'
        db.delete_table(db.shorten_name(u'crawler_webpage_tags'))


    models = {
        u'crawler.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'words': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'crawler.webpage': {
            'Meta': {'object_name': 'WebPage'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['crawler.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['crawler']