# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'TractData.pop2010'
        db.alter_column('census_tractdata', 'pop2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'TractData.pop2000'
        db.alter_column('census_tractdata', 'pop2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pop2010'
        db.alter_column('census_countydata', 'pop2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pop2000'
        db.alter_column('census_countydata', 'pop2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'StateData.pop2010'
        db.alter_column('census_statedata', 'pop2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'StateData.pop2000'
        db.alter_column('census_statedata', 'pop2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))


    def backwards(self, orm):
        
        # Changing field 'TractData.pop2010'
        db.alter_column('census_tractdata', 'pop2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pop2000'
        db.alter_column('census_tractdata', 'pop2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pop2010'
        db.alter_column('census_countydata', 'pop2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pop2000'
        db.alter_column('census_countydata', 'pop2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pop2010'
        db.alter_column('census_statedata', 'pop2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pop2000'
        db.alter_column('census_statedata', 'pop2000', self.gf('django.db.models.fields.IntegerField')())


    models = {
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
            'pop2000SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'total_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tract_name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'water_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['census']
