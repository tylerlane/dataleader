# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Layout'
        db.create_table('trueozarks_layout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('template', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('trueozarks', ['Layout'])

        # Adding model 'Tag'
        db.create_table('trueozarks_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('time_init', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('geocoder', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
        ))
        db.send_create_signal('trueozarks', ['Tag'])

        # Adding model 'Profile'
        db.create_table('trueozarks_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('main_photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('time_init', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('geocoder', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('layout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trueozarks.Layout'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('trueozarks', ['Profile'])

        # Adding M2M table for field tags on 'Profile'
        db.create_table('trueozarks_profile_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['trueozarks.profile'], null=False)),
            ('tag', models.ForeignKey(orm['trueozarks.tag'], null=False))
        ))
        db.create_unique('trueozarks_profile_tags', ['profile_id', 'tag_id'])

        # Adding model 'Story'
        db.create_table('trueozarks_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['trueozarks.Profile'], unique=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subheadline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('byline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('time_init', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('geocoder', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
        ))
        db.send_create_signal('trueozarks', ['Story'])

        # Adding M2M table for field tags on 'Story'
        db.create_table('trueozarks_story_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm['trueozarks.story'], null=False)),
            ('tag', models.ForeignKey(orm['trueozarks.tag'], null=False))
        ))
        db.create_unique('trueozarks_story_tags', ['story_id', 'tag_id'])

        # Adding model 'PullQuote'
        db.create_table('trueozarks_pullquote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trueozarks.Story'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('trueozarks', ['PullQuote'])

        # Adding model 'InfoBox'
        db.create_table('trueozarks_infobox', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trueozarks.Story'])),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('trueozarks', ['InfoBox'])

        # Adding model 'Photo'
        db.create_table('trueozarks_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trueozarks.Profile'])),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('cutline', self.gf('django.db.models.fields.TextField')()),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('geocoder', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('time_init', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('trueozarks', ['Photo'])

        # Adding M2M table for field tags on 'Photo'
        db.create_table('trueozarks_photo_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo', models.ForeignKey(orm['trueozarks.photo'], null=False)),
            ('tag', models.ForeignKey(orm['trueozarks.tag'], null=False))
        ))
        db.create_unique('trueozarks_photo_tags', ['photo_id', 'tag_id'])


    def backwards(self, orm):
        
        # Deleting model 'Layout'
        db.delete_table('trueozarks_layout')

        # Deleting model 'Tag'
        db.delete_table('trueozarks_tag')

        # Deleting model 'Profile'
        db.delete_table('trueozarks_profile')

        # Removing M2M table for field tags on 'Profile'
        db.delete_table('trueozarks_profile_tags')

        # Deleting model 'Story'
        db.delete_table('trueozarks_story')

        # Removing M2M table for field tags on 'Story'
        db.delete_table('trueozarks_story_tags')

        # Deleting model 'PullQuote'
        db.delete_table('trueozarks_pullquote')

        # Deleting model 'InfoBox'
        db.delete_table('trueozarks_infobox')

        # Deleting model 'Photo'
        db.delete_table('trueozarks_photo')

        # Removing M2M table for field tags on 'Photo'
        db.delete_table('trueozarks_photo_tags')


    models = {
        'trueozarks.infobox': {
            'Meta': {'object_name': 'InfoBox'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trueozarks.Story']"}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'trueozarks.layout': {
            'Meta': {'object_name': 'Layout'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'trueozarks.photo': {
            'Meta': {'object_name': 'Photo'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cutline': ('django.db.models.fields.TextField', [], {}),
            'geocoder': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trueozarks.Profile']"}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['trueozarks.Tag']", 'symmetrical': 'False'}),
            'time_init': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'trueozarks.profile': {
            'Meta': {'object_name': 'Profile'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'geocoder': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'layout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trueozarks.Layout']"}),
            'main_photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['trueozarks.Tag']", 'symmetrical': 'False'}),
            'time_init': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'trueozarks.pullquote': {
            'Meta': {'object_name': 'PullQuote'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trueozarks.Story']"}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'trueozarks.story': {
            'Meta': {'object_name': 'Story'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'byline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'geocoder': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['trueozarks.Profile']", 'unique': 'True'}),
            'subheadline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['trueozarks.Tag']", 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'time_init': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'trueozarks.tag': {
            'Meta': {'object_name': 'Tag'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'geocoder': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'time_init': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['trueozarks']
