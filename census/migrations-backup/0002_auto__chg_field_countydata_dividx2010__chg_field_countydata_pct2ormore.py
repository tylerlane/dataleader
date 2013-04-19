# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'CountyData.dividx2010'
        db.alter_column('census_countydata', 'dividx2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pct2ormore2010'
        db.alter_column('census_countydata', 'pct2ormore2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pcthisp2010'
        db.alter_column('census_countydata', 'pcthisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctamind2000'
        db.alter_column('census_countydata', 'pctamind2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.water_sqmiles'
        db.alter_column('census_countydata', 'water_sqmiles', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctnathaw2000'
        db.alter_column('census_countydata', 'pctnathaw2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctwhitenonhisp2000'
        db.alter_column('census_countydata', 'pctwhitenonhisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctother2010'
        db.alter_column('census_countydata', 'pctother2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctblack2010'
        db.alter_column('census_countydata', 'pctblack2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.total_sqmiles'
        db.alter_column('census_countydata', 'total_sqmiles', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctnonhisp2010'
        db.alter_column('census_countydata', 'pctnonhisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctwhite2010'
        db.alter_column('census_countydata', 'pctwhite2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.dividx2000'
        db.alter_column('census_countydata', 'dividx2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pct2ormore2000'
        db.alter_column('census_countydata', 'pct2ormore2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pcthisp2000'
        db.alter_column('census_countydata', 'pcthisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctamind2010'
        db.alter_column('census_countydata', 'pctamind2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctnathaw2010'
        db.alter_column('census_countydata', 'pctnathaw2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctasian2010'
        db.alter_column('census_countydata', 'pctasian2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctwhitenonhisp2010'
        db.alter_column('census_countydata', 'pctwhitenonhisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctother2000'
        db.alter_column('census_countydata', 'pctother2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctblack2000'
        db.alter_column('census_countydata', 'pctblack2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctnonhisp2000'
        db.alter_column('census_countydata', 'pctnonhisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctwhite2000'
        db.alter_column('census_countydata', 'pctwhite2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'CountyData.pctasian2000'
        db.alter_column('census_countydata', 'pctasian2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))


    def backwards(self, orm):
        
        # Changing field 'CountyData.dividx2010'
        db.alter_column('census_countydata', 'dividx2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pct2ormore2010'
        db.alter_column('census_countydata', 'pct2ormore2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pcthisp2010'
        db.alter_column('census_countydata', 'pcthisp2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctamind2000'
        db.alter_column('census_countydata', 'pctamind2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.water_sqmiles'
        db.alter_column('census_countydata', 'water_sqmiles', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctnathaw2000'
        db.alter_column('census_countydata', 'pctnathaw2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctwhitenonhisp2000'
        db.alter_column('census_countydata', 'pctwhitenonhisp2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctother2010'
        db.alter_column('census_countydata', 'pctother2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctblack2010'
        db.alter_column('census_countydata', 'pctblack2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.total_sqmiles'
        db.alter_column('census_countydata', 'total_sqmiles', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctnonhisp2010'
        db.alter_column('census_countydata', 'pctnonhisp2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctwhite2010'
        db.alter_column('census_countydata', 'pctwhite2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.dividx2000'
        db.alter_column('census_countydata', 'dividx2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pct2ormore2000'
        db.alter_column('census_countydata', 'pct2ormore2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pcthisp2000'
        db.alter_column('census_countydata', 'pcthisp2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctamind2010'
        db.alter_column('census_countydata', 'pctamind2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctnathaw2010'
        db.alter_column('census_countydata', 'pctnathaw2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctasian2010'
        db.alter_column('census_countydata', 'pctasian2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctwhitenonhisp2010'
        db.alter_column('census_countydata', 'pctwhitenonhisp2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctother2000'
        db.alter_column('census_countydata', 'pctother2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctblack2000'
        db.alter_column('census_countydata', 'pctblack2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctnonhisp2000'
        db.alter_column('census_countydata', 'pctnonhisp2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctwhite2000'
        db.alter_column('census_countydata', 'pctwhite2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CountyData.pctasian2000'
        db.alter_column('census_countydata', 'pctasian2000', self.gf('django.db.models.fields.IntegerField')())


    models = {
        'census.countydata': {
            'Meta': {'object_name': 'CountyData'},
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'dividx2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dividx2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pct2ormore2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pct2ormore2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctamind2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctamind2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctasian2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctasian2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctblack2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctblack2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pcthisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pcthisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctnathaw2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctnathaw2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctnonhisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctnonhisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctother2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctother2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhite2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhite2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhitenonhisp2000': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctwhitenonhisp2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop2000': ('django.db.models.fields.IntegerField', [], {}),
            'pop2000SqMile': ('django.db.models.fields.IntegerField', [], {}),
            'pop2010': ('django.db.models.fields.IntegerField', [], {}),
            'pop2010SqMile': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'total_sqmiles': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'water_sqmiles': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'census.statedata': {
            'Meta': {'object_name': 'StateData'},
            'dividx2000': ('django.db.models.fields.IntegerField', [], {}),
            'dividx2010': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pct2ormore2000': ('django.db.models.fields.IntegerField', [], {}),
            'pct2ormore2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctamind2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctamind2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctasian2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctasian2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctblack2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctblack2010': ('django.db.models.fields.IntegerField', [], {}),
            'pcthisp2000': ('django.db.models.fields.IntegerField', [], {}),
            'pcthisp2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctnathaw2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctnathaw2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctnonhisp2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctnonhisp2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctother2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctother2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctwhite2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctwhite2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctwhitenonhisp2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctwhitenonhisp2010': ('django.db.models.fields.IntegerField', [], {}),
            'pop2000': ('django.db.models.fields.IntegerField', [], {}),
            'pop2000SqMile': ('django.db.models.fields.IntegerField', [], {}),
            'pop2010': ('django.db.models.fields.IntegerField', [], {}),
            'pop2010SqMile': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'total_sqmiles': ('django.db.models.fields.IntegerField', [], {}),
            'water_sqmiles': ('django.db.models.fields.IntegerField', [], {})
        },
        'census.tractdata': {
            'Meta': {'object_name': 'TractData'},
            'dividx2000': ('django.db.models.fields.IntegerField', [], {}),
            'dividx2010': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pct2ormore2000': ('django.db.models.fields.IntegerField', [], {}),
            'pct2ormore2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctamind2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctamind2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctasian2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctasian2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctblack2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctblack2010': ('django.db.models.fields.IntegerField', [], {}),
            'pcthisp2000': ('django.db.models.fields.IntegerField', [], {}),
            'pcthisp2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctnathaw2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctnathaw2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctnonhisp2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctnonhisp2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctother2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctother2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctwhite2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctwhite2010': ('django.db.models.fields.IntegerField', [], {}),
            'pctwhitenonhisp2000': ('django.db.models.fields.IntegerField', [], {}),
            'pctwhitenonhisp2010': ('django.db.models.fields.IntegerField', [], {}),
            'pop2000': ('django.db.models.fields.IntegerField', [], {}),
            'pop2000SqMile': ('django.db.models.fields.IntegerField', [], {}),
            'pop2010': ('django.db.models.fields.IntegerField', [], {}),
            'pop2010SqMile': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'total_sqmiles': ('django.db.models.fields.IntegerField', [], {}),
            'tract_name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'water_sqmiles': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['census']
