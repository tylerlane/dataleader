# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Schools'
        db.create_table('schools', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ctydist', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('schnum', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('schid', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('facility', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('bgrade', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('egrade', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('principal', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('printitle', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('teachers', self.gf('django.db.models.fields.FloatField')()),
            ('enrollment', self.gf('django.db.models.fields.IntegerField')()),
            ('schemail', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('loc_code', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal('zones', ['Schools'])

        # Adding model 'SchoolDistricts'
        db.create_table('school_districts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('perimeter', self.gf('django.db.models.fields.FloatField')()),
            ('unsd_field', self.gf('django.db.models.fields.FloatField')()),
            ('unsd_id', self.gf('django.db.models.fields.FloatField')()),
            ('statefp', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('statens', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('unsdlea', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('unsdidfp', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lsad', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('lograde', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('higrade', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('mtfcc', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('sdtyp', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('funcstat', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('aland', self.gf('django.db.models.fields.FloatField')()),
            ('awater', self.gf('django.db.models.fields.FloatField')()),
            ('intptlat', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('intptlon', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PolygonField')()),
        ))
        db.send_create_signal('zones', ['SchoolDistricts'])

        # Adding model 'Counties'
        db.create_table('counties', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('countyfips', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('countygnis', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('name_ucase', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('pop_1990', self.gf('django.db.models.fields.IntegerField')()),
            ('pop_2000', self.gf('django.db.models.fields.IntegerField')()),
            ('acres', self.gf('django.db.models.fields.FloatField')()),
            ('sq_miles', self.gf('django.db.models.fields.FloatField')()),
            ('cnty_seat', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('co_class', self.gf('django.db.models.fields.IntegerField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('zones', ['Counties'])

        # Adding model 'ZipCodes'
        db.create_table('zip_codes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zcta5ce', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('classfp', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('mtfcc', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('funcstat', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('zones', ['ZipCodes'])

        # Adding model 'ReversePubZone'
        db.create_table('reversepub_zone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('zones', ['ReversePubZone'])


    def backwards(self, orm):
        
        # Deleting model 'Schools'
        db.delete_table('schools')

        # Deleting model 'SchoolDistricts'
        db.delete_table('school_districts')

        # Deleting model 'Counties'
        db.delete_table('counties')

        # Deleting model 'ZipCodes'
        db.delete_table('zip_codes')

        # Deleting model 'ReversePubZone'
        db.delete_table('reversepub_zone')


    models = {
        'zones.counties': {
            'Meta': {'object_name': 'Counties', 'db_table': "'counties'"},
            'acres': ('django.db.models.fields.FloatField', [], {}),
            'cnty_seat': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'co_class': ('django.db.models.fields.IntegerField', [], {}),
            'countyfips': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'countygnis': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_ucase': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'pop_1990': ('django.db.models.fields.IntegerField', [], {}),
            'pop_2000': ('django.db.models.fields.IntegerField', [], {}),
            'sq_miles': ('django.db.models.fields.FloatField', [], {})
        },
        'zones.reversepubzone': {
            'Meta': {'object_name': 'ReversePubZone', 'db_table': "'reversepub_zone'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'zones.schooldistricts': {
            'Meta': {'object_name': 'SchoolDistricts', 'db_table': "'school_districts'"},
            'aland': ('django.db.models.fields.FloatField', [], {}),
            'area': ('django.db.models.fields.FloatField', [], {}),
            'awater': ('django.db.models.fields.FloatField', [], {}),
            'funcstat': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'higrade': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intptlat': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'intptlon': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'lograde': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'lsad': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'mtfcc': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'perimeter': ('django.db.models.fields.FloatField', [], {}),
            'sdtyp': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'statefp': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'statens': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'unsd_field': ('django.db.models.fields.FloatField', [], {}),
            'unsd_id': ('django.db.models.fields.FloatField', [], {}),
            'unsdidfp': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'unsdlea': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'zones.schools': {
            'Meta': {'object_name': 'Schools', 'db_table': "'schools'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'bgrade': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'ctydist': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'egrade': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'enrollment': ('django.db.models.fields.IntegerField', [], {}),
            'facility': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'loc_code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'principal': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'printitle': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'schemail': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'schid': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'schnum': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'teachers': ('django.db.models.fields.FloatField', [], {}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'zones.zipcodes': {
            'Meta': {'object_name': 'ZipCodes', 'db_table': "'zip_codes'"},
            'classfp': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'funcstat': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtfcc': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'zcta5ce': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['zones']
