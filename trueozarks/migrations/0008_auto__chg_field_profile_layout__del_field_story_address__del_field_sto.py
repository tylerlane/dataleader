# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Profile.layout'
        db.alter_column('trueozarks_profile', 'layout_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trueozarks.Layout'], null=True, blank=True))

        # Deleting field 'Story.address'
        db.delete_column('trueozarks_story', 'address')

        # Deleting field 'Story.geocoder'
        db.delete_column('trueozarks_story', 'geocoder')

        # Deleting field 'Story.geom'
        db.delete_column('trueozarks_story', 'geom')

        # Removing M2M table for field tags on 'Story'
        db.delete_table('trueozarks_story_tags')

        # Deleting field 'Photo.style'
        db.delete_column('trueozarks_photo', 'style')


    def backwards(self, orm):
        
        # Changing field 'Profile.layout'
        db.alter_column('trueozarks_profile', 'layout_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trueozarks.Layout']))

        # Adding field 'Story.address'
        db.add_column('trueozarks_story', 'address', self.gf('django.db.models.fields.CharField')(default='foo', max_length=255), keep_default=False)

        # Adding field 'Story.geocoder'
        db.add_column('trueozarks_story', 'geocoder', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True), keep_default=False)

        # Adding field 'Story.geom'
        db.add_column('trueozarks_story', 'geom', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True), keep_default=False)

        # Adding M2M table for field tags on 'Story'
        db.create_table('trueozarks_story_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm['trueozarks.story'], null=False)),
            ('tag', models.ForeignKey(orm['trueozarks.tag'], null=False))
        ))
        db.create_unique('trueozarks_story_tags', ['story_id', 'tag_id'])

        # Adding field 'Photo.style'
        db.add_column('trueozarks_photo', 'style', self.gf('django.db.models.fields.CharField')(default='foo', max_length=100), keep_default=False)


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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['trueozarks.Tag']", 'null': 'True', 'blank': 'True'}),
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
            'layout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trueozarks.Layout']", 'null': 'True', 'blank': 'True'}),
            'main_photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'most_popular': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['trueozarks.Tag']", 'null': 'True', 'blank': 'True'}),
            'time_init': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'})
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
            'byline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['trueozarks.Profile']", 'unique': 'True'}),
            'subheadline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'time_init': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'trueozarks.tag': {
            'Meta': {'object_name': 'Tag'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geocoder': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'time_init': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['trueozarks']
