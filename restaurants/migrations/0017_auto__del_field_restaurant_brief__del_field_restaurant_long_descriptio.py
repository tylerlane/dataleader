# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Restaurant.brief'
        db.delete_column('restaurants_restaurant', 'brief')

        # Deleting field 'Restaurant.long_description'
        db.delete_column('restaurants_restaurant', 'long_description')

        # Deleting field 'Restaurant.subheadline'
        db.delete_column('restaurants_restaurant', 'subheadline')

        # Adding field 'Restaurant.description'
        db.add_column('restaurants_restaurant', 'description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Restaurant.brief'
        db.add_column('restaurants_restaurant', 'brief', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Restaurant.long_description'
        db.add_column('restaurants_restaurant', 'long_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Restaurant.subheadline'
        db.add_column('restaurants_restaurant', 'subheadline', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Deleting field 'Restaurant.description'
        db.delete_column('restaurants_restaurant', 'description')


    models = {
        'restaurants.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'comma_delimited': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurants.Restaurant']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'restaurants.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'restaurants.inspection': {
            'Meta': {'object_name': 'Inspection'},
            'critical': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'critical_violations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noncritical': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reinspection': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurants.Restaurant']"})
        },
        'restaurants.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'channel': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Cuisines'", 'symmetrical': 'False', 'to': "orm['restaurants.Cuisine']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geocoder': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True'}),
            'hours': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'photo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['restaurants']
