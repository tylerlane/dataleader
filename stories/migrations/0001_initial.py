# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Story'
        db.create_table('story', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('long_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_removed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('byline', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('images', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('stories', ['Story'])

        # Adding model 'Pageview'
        db.create_table('pageview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stories.Story'], null=True, blank=True)),
            ('time_init', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('stories', ['Pageview'])

        # Adding model 'Keyword'
        db.create_table('keyword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stories.Story'])),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('stories', ['Keyword'])


    def backwards(self, orm):
        
        # Deleting model 'Story'
        db.delete_table('story')

        # Deleting model 'Pageview'
        db.delete_table('pageview')

        # Deleting model 'Keyword'
        db.delete_table('keyword')


    models = {
        'stories.keyword': {
            'Meta': {'object_name': 'Keyword', 'db_table': "'keyword'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stories.Story']"})
        },
        'stories.pageview': {
            'Meta': {'object_name': 'Pageview', 'db_table': "'pageview'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stories.Story']", 'null': 'True', 'blank': 'True'}),
            'time_init': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'stories.story': {
            'Meta': {'object_name': 'Story', 'db_table': "'story'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'byline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {}),
            'date_removed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'images': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'long_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['stories']
