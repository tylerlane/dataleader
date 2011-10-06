# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Restaurant'
        db.create_table('restaurants_restaurant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('subheadline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('brief', self.gf('django.db.models.fields.TextField')()),
            ('long_description', self.gf('django.db.models.fields.TextField')()),
            ('geocoder', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True)),
        ))
        db.send_create_signal('restaurants', ['Restaurant'])

        # Adding model 'Inspection'
        db.create_table('restaurants_inspection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurants.Restaurant'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('reinspection', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('critical', self.gf('django.db.models.fields.IntegerField')()),
            ('noncritical', self.gf('django.db.models.fields.IntegerField')()),
            ('critical_violations', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('restaurants', ['Inspection'])


    def backwards(self, orm):
        
        # Deleting model 'Restaurant'
        db.delete_table('restaurants_restaurant')

        # Deleting model 'Inspection'
        db.delete_table('restaurants_inspection')


    models = {
        'restaurants.inspection': {
            'Meta': {'object_name': 'Inspection'},
            'critical': ('django.db.models.fields.IntegerField', [], {}),
            'critical_violations': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noncritical': ('django.db.models.fields.IntegerField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'reinspection': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurants.Restaurant']"})
        },
        'restaurants.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'brief': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'geocoder': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'long_description': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'subheadline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['restaurants']
