# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CityData'
        db.create_table('census_citydata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city_name', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('state', self.gf('django.db.models.fields.CharField')(max_length='2')),
            ('pop2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pop2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pop2000SqMile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pop2010SqMile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pctwhite2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popwhite2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctwhite2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popwhite2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctblack2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popblack2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctblack2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popblack2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctamind2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popamind2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctamind2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popamind2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctasian2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popasian2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctasian2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popasian2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctnathaw2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popnathaw2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctnathaw2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popnathaw2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctother2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popother2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctother2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popother2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pct2ormore2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pop2ormore2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pct2ormore2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pop2ormore2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pcthisp2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pophisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pcthisp2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pophisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctnonhisp2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popnonhisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctnonhisp2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popnonhisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctwhitenonhisp2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popwhitenonhisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctwhitenonhisp2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popwhitenonhisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dividx2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dividx2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total_sqmiles', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('water_sqmiles', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('land_sqmiles', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('census', ['CityData'])

        # Adding model 'ZipCodeData'
        db.create_table('census_zipcodedata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('state', self.gf('django.db.models.fields.CharField')(max_length='2')),
            ('pop2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pop2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pop2000SqMile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pop2010SqMile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pctwhite2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popwhite2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctwhite2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popwhite2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctblack2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popblack2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctblack2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popblack2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctamind2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popamind2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctamind2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popamind2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctasian2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popasian2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctasian2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popasian2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctnathaw2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popnathaw2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctnathaw2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popnathaw2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctother2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popother2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctother2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popother2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pct2ormore2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pop2ormore2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pct2ormore2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pop2ormore2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pcthisp2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pophisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pcthisp2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pophisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctnonhisp2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popnonhisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctnonhisp2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popnonhisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctwhitenonhisp2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popwhitenonhisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pctwhitenonhisp2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popwhitenonhisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dividx2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dividx2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total_sqmiles', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('water_sqmiles', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('land_sqmiles', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('census', ['ZipCodeData'])


    def backwards(self, orm):
        
        # Deleting model 'CityData'
        db.delete_table('census_citydata')

        # Deleting model 'ZipCodeData'
        db.delete_table('census_zipcodedata')


    models = {
        'census.citydata': {
            'Meta': {'object_name': 'CityData'},
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'dividx2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dividx2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pct2ormore2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pct2ormore2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctamind2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctamind2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctasian2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctasian2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctblack2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctblack2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcthisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcthisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnathaw2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnathaw2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnonhisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnonhisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctother2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctother2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhite2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhite2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhitenonhisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhitenonhisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2000SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2ormore2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2ormore2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popamind2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popamind2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popasian2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popasian2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popblack2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popblack2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pophisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pophisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnathaw2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnathaw2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnonhisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnonhisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popother2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popother2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhite2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhite2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhitenonhisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhitenonhisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'total_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'water_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'census.countydata': {
            'Meta': {'object_name': 'CountyData'},
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'dividx2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dividx2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pct2ormore2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pct2ormore2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctamind2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctamind2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctasian2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctasian2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctblack2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctblack2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcthisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcthisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnathaw2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnathaw2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnonhisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnonhisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctother2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctother2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhite2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhite2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhitenonhisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhitenonhisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2000SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2ormore2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2ormore2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popamind2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popamind2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popasian2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popasian2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popblack2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popblack2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pophisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pophisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnathaw2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnathaw2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnonhisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnonhisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popother2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popother2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhite2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhite2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhitenonhisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhitenonhisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'total_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'water_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'census.statedata': {
            'Meta': {'object_name': 'StateData'},
            'dividx2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dividx2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pct2ormore2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pct2ormore2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctamind2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctamind2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctasian2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctasian2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctblack2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctblack2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcthisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcthisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnathaw2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnathaw2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnonhisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnonhisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctother2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctother2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhite2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhite2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhitenonhisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhitenonhisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2000SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2ormore2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2ormore2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popamind2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popamind2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popasian2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popasian2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popblack2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popblack2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pophisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pophisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnathaw2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnathaw2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnonhisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnonhisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popother2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popother2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhite2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhite2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhitenonhisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhitenonhisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'total_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'water_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'census.tractdata': {
            'Meta': {'object_name': 'TractData'},
            'dividx2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dividx2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pct2ormore2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pct2ormore2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctamind2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctamind2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctasian2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctasian2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctblack2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctblack2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcthisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcthisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnathaw2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnathaw2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnonhisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnonhisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctother2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctother2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhite2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhite2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhitenonhisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhitenonhisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2ormore2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2ormore2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popamind2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popamind2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popasian2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popasian2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popblack2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popblack2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pophisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pophisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnathaw2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnathaw2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnonhisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnonhisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popother2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popother2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhite2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhite2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhitenonhisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhitenonhisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'total_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tract_name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'water_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'census.zipcodedata': {
            'Meta': {'object_name': 'ZipCodeData'},
            'dividx2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dividx2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pct2ormore2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pct2ormore2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctamind2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctamind2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctasian2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctasian2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctblack2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctblack2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcthisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcthisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnathaw2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnathaw2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnonhisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctnonhisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctother2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctother2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhite2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhite2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhitenonhisp2000': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhitenonhisp2010': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2000SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2ormore2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2ormore2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popamind2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popamind2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popasian2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popasian2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popblack2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popblack2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pophisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pophisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnathaw2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnathaw2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnonhisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popnonhisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popother2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popother2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhite2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhite2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhitenonhisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'popwhitenonhisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'total_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'water_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': "'200'"})
        }
    }

    complete_apps = ['census']