# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Restaurant.city'
        db.alter_column('restaurants_restaurant', 'city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Changing field 'Restaurant.phone'
        db.alter_column('restaurants_restaurant', 'phone', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True))

        # Changing field 'Restaurant.brief'
        db.alter_column('restaurants_restaurant', 'brief', self.gf('django.db.models.fields.TextField')(null=True, blank=True))

        # Changing field 'Restaurant.subheadline'
        db.alter_column('restaurants_restaurant', 'subheadline', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Changing field 'Restaurant.state'
        db.alter_column('restaurants_restaurant', 'state', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True))

        # Changing field 'Restaurant.long_description'
        db.alter_column('restaurants_restaurant', 'long_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True))

        # Changing field 'Restaurant.zip_code'
        db.alter_column('restaurants_restaurant', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True))


    def backwards(self, orm):
        
        # Changing field 'Restaurant.city'
        db.alter_column('restaurants_restaurant', 'city', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Restaurant.phone'
        db.alter_column('restaurants_restaurant', 'phone', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'Restaurant.brief'
        db.alter_column('restaurants_restaurant', 'brief', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Restaurant.subheadline'
        db.alter_column('restaurants_restaurant', 'subheadline', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Restaurant.state'
        db.alter_column('restaurants_restaurant', 'state', self.gf('django.db.models.fields.CharField')(max_length=5))

        # Changing field 'Restaurant.long_description'
        db.alter_column('restaurants_restaurant', 'long_description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Restaurant.zip_code'
        db.alter_column('restaurants_restaurant', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=10))


    models = {
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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'brief': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'channel': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geocoder': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'long_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'subheadline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['restaurants']
