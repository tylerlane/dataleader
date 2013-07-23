# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Photo.style'
        db.alter_column('trueozarks_photo', 'style', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True))

        # Changing field 'Photo.credit'
        db.alter_column('trueozarks_photo', 'credit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Changing field 'Photo.position'
        db.alter_column('trueozarks_photo', 'position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'Photo.order'
        db.alter_column('trueozarks_photo', 'order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'Photo.cutline'
        db.alter_column('trueozarks_photo', 'cutline', self.gf('django.db.models.fields.TextField')(null=True, blank=True))


    def backwards(self, orm):
        
        # Changing field 'Photo.style'
        db.alter_column('trueozarks_photo', 'style', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Photo.credit'
        db.alter_column('trueozarks_photo', 'credit', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Photo.position'
        db.alter_column('trueozarks_photo', 'position', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Photo.order'
        db.alter_column('trueozarks_photo', 'order', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Photo.cutline'
        db.alter_column('trueozarks_photo', 'cutline', self.gf('django.db.models.fields.TextField')())


    models = {
        'trueozarks.infobox': {
            'Meta': {'object_name': 'InfoBox'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trueozarks.Profile']"}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'trueozarks.layout': {
            'Meta': {'object_name': 'Layout'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'stylesheet': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'trueozarks.photo': {
            'Meta': {'object_name': 'Photo'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cutline': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geocoder': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_gallery': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'in_story': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trueozarks.Profile']"}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'left'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'layout': ('django.db.models.fields.related.ForeignKey', [], {'default': "'default'", 'to': "orm['trueozarks.Layout']", 'null': 'True', 'blank': 'True'}),
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
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trueozarks.Profile']"}),
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
