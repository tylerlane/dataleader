# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Cuisine'
        db.create_table('restaurants_cuisine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('restaurants', ['Cuisine'])

        # Adding model 'Detail'
        db.create_table('restaurants_detail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurants.Restaurant'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('comma_delimited', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('restaurants', ['Detail'])

        # Adding field 'Restaurant.hours'
        db.add_column('restaurants_restaurant', 'hours', self.gf('django.db.models.fields.CharField')(max_length=100, null=True), keep_default=False)

        # Adding field 'Restaurant.active'
        db.add_column('restaurants_restaurant', 'active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True), keep_default=False)

        # Adding M2M table for field cuisine on 'Restaurant'
        db.create_table('restaurants_restaurant_cuisine', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('restaurant', models.ForeignKey(orm['restaurants.restaurant'], null=False)),
            ('cuisine', models.ForeignKey(orm['restaurants.cuisine'], null=False))
        ))
        db.create_unique('restaurants_restaurant_cuisine', ['restaurant_id', 'cuisine_id'])

        # Changing field 'Restaurant.channel'
        db.alter_column('restaurants_restaurant', 'channel', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))


    def backwards(self, orm):
        
        # Deleting model 'Cuisine'
        db.delete_table('restaurants_cuisine')

        # Deleting model 'Detail'
        db.delete_table('restaurants_detail')

        # Deleting field 'Restaurant.hours'
        db.delete_column('restaurants_restaurant', 'hours')

        # Deleting field 'Restaurant.active'
        db.delete_column('restaurants_restaurant', 'active')

        # Removing M2M table for field cuisine on 'Restaurant'
        db.delete_table('restaurants_restaurant_cuisine')

        # Changing field 'Restaurant.channel'
        db.alter_column('restaurants_restaurant', 'channel', self.gf('django.db.models.fields.CharField')(max_length=25))


    models = {
        'restaurants.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'restaurants.detail': {
            'Meta': {'object_name': 'Detail'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'comma_delimited': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurants.Restaurant']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '250'})
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
            'brief': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'channel': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['restaurants.Cuisine']", 'symmetrical': 'False'}),
            'geocoder': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True'}),
            'hours': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
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
