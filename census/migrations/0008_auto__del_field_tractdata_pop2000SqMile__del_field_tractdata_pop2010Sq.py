# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'TractData.pop2000SqMile'
        db.delete_column('census_tractdata', 'pop2000SqMile')

        # Deleting field 'TractData.pop2010SqMile'
        db.delete_column('census_tractdata', 'pop2010SqMile')

        # Adding field 'TractData.popwhite2000'
        db.add_column('census_tractdata', 'popwhite2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popwhite2010'
        db.add_column('census_tractdata', 'popwhite2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popblack2000'
        db.add_column('census_tractdata', 'popblack2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popblack2010'
        db.add_column('census_tractdata', 'popblack2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popamind2000'
        db.add_column('census_tractdata', 'popamind2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popamind2010'
        db.add_column('census_tractdata', 'popamind2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popasian2000'
        db.add_column('census_tractdata', 'popasian2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popasian2010'
        db.add_column('census_tractdata', 'popasian2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popnathaw2000'
        db.add_column('census_tractdata', 'popnathaw2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popnathaw2010'
        db.add_column('census_tractdata', 'popnathaw2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popother2000'
        db.add_column('census_tractdata', 'popother2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popother2010'
        db.add_column('census_tractdata', 'popother2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.pop2ormore2000'
        db.add_column('census_tractdata', 'pop2ormore2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.pop2ormore2010'
        db.add_column('census_tractdata', 'pop2ormore2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.pophisp2000'
        db.add_column('census_tractdata', 'pophisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.pophisp2010'
        db.add_column('census_tractdata', 'pophisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popnonhisp2000'
        db.add_column('census_tractdata', 'popnonhisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popnonhisp2010'
        db.add_column('census_tractdata', 'popnonhisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popwhitenonhisp2000'
        db.add_column('census_tractdata', 'popwhitenonhisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.popwhitenonhisp2010'
        db.add_column('census_tractdata', 'popwhitenonhisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popwhite2000'
        db.add_column('census_countydata', 'popwhite2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popwhite2010'
        db.add_column('census_countydata', 'popwhite2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popblack2000'
        db.add_column('census_countydata', 'popblack2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popblack2010'
        db.add_column('census_countydata', 'popblack2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popamind2000'
        db.add_column('census_countydata', 'popamind2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popamind2010'
        db.add_column('census_countydata', 'popamind2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popasian2000'
        db.add_column('census_countydata', 'popasian2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popasian2010'
        db.add_column('census_countydata', 'popasian2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popnathaw2000'
        db.add_column('census_countydata', 'popnathaw2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popnathaw2010'
        db.add_column('census_countydata', 'popnathaw2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popother2000'
        db.add_column('census_countydata', 'popother2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popother2010'
        db.add_column('census_countydata', 'popother2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.pop2ormore2000'
        db.add_column('census_countydata', 'pop2ormore2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.pop2ormore2010'
        db.add_column('census_countydata', 'pop2ormore2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.pophisp2000'
        db.add_column('census_countydata', 'pophisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.pophisp2010'
        db.add_column('census_countydata', 'pophisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popnonhisp2000'
        db.add_column('census_countydata', 'popnonhisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popnonhisp2010'
        db.add_column('census_countydata', 'popnonhisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popwhitenonhisp2000'
        db.add_column('census_countydata', 'popwhitenonhisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'CountyData.popwhitenonhisp2010'
        db.add_column('census_countydata', 'popwhitenonhisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popwhite2000'
        db.add_column('census_statedata', 'popwhite2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popwhite2010'
        db.add_column('census_statedata', 'popwhite2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popblack2000'
        db.add_column('census_statedata', 'popblack2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popblack2010'
        db.add_column('census_statedata', 'popblack2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popamind2000'
        db.add_column('census_statedata', 'popamind2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popamind2010'
        db.add_column('census_statedata', 'popamind2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popasian2000'
        db.add_column('census_statedata', 'popasian2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popasian2010'
        db.add_column('census_statedata', 'popasian2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popnathaw2000'
        db.add_column('census_statedata', 'popnathaw2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popnathaw2010'
        db.add_column('census_statedata', 'popnathaw2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popother2000'
        db.add_column('census_statedata', 'popother2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popother2010'
        db.add_column('census_statedata', 'popother2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.pop2ormore2000'
        db.add_column('census_statedata', 'pop2ormore2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.pop2ormore2010'
        db.add_column('census_statedata', 'pop2ormore2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.pophisp2000'
        db.add_column('census_statedata', 'pophisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.pophisp2010'
        db.add_column('census_statedata', 'pophisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popnonhisp2000'
        db.add_column('census_statedata', 'popnonhisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popnonhisp2010'
        db.add_column('census_statedata', 'popnonhisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popwhitenonhisp2000'
        db.add_column('census_statedata', 'popwhitenonhisp2000', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'StateData.popwhitenonhisp2010'
        db.add_column('census_statedata', 'popwhitenonhisp2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'TractData.pop2000SqMile'
        db.add_column('census_tractdata', 'pop2000SqMile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'TractData.pop2010SqMile'
        db.add_column('census_tractdata', 'pop2010SqMile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Deleting field 'TractData.popwhite2000'
        db.delete_column('census_tractdata', 'popwhite2000')

        # Deleting field 'TractData.popwhite2010'
        db.delete_column('census_tractdata', 'popwhite2010')

        # Deleting field 'TractData.popblack2000'
        db.delete_column('census_tractdata', 'popblack2000')

        # Deleting field 'TractData.popblack2010'
        db.delete_column('census_tractdata', 'popblack2010')

        # Deleting field 'TractData.popamind2000'
        db.delete_column('census_tractdata', 'popamind2000')

        # Deleting field 'TractData.popamind2010'
        db.delete_column('census_tractdata', 'popamind2010')

        # Deleting field 'TractData.popasian2000'
        db.delete_column('census_tractdata', 'popasian2000')

        # Deleting field 'TractData.popasian2010'
        db.delete_column('census_tractdata', 'popasian2010')

        # Deleting field 'TractData.popnathaw2000'
        db.delete_column('census_tractdata', 'popnathaw2000')

        # Deleting field 'TractData.popnathaw2010'
        db.delete_column('census_tractdata', 'popnathaw2010')

        # Deleting field 'TractData.popother2000'
        db.delete_column('census_tractdata', 'popother2000')

        # Deleting field 'TractData.popother2010'
        db.delete_column('census_tractdata', 'popother2010')

        # Deleting field 'TractData.pop2ormore2000'
        db.delete_column('census_tractdata', 'pop2ormore2000')

        # Deleting field 'TractData.pop2ormore2010'
        db.delete_column('census_tractdata', 'pop2ormore2010')

        # Deleting field 'TractData.pophisp2000'
        db.delete_column('census_tractdata', 'pophisp2000')

        # Deleting field 'TractData.pophisp2010'
        db.delete_column('census_tractdata', 'pophisp2010')

        # Deleting field 'TractData.popnonhisp2000'
        db.delete_column('census_tractdata', 'popnonhisp2000')

        # Deleting field 'TractData.popnonhisp2010'
        db.delete_column('census_tractdata', 'popnonhisp2010')

        # Deleting field 'TractData.popwhitenonhisp2000'
        db.delete_column('census_tractdata', 'popwhitenonhisp2000')

        # Deleting field 'TractData.popwhitenonhisp2010'
        db.delete_column('census_tractdata', 'popwhitenonhisp2010')

        # Deleting field 'CountyData.popwhite2000'
        db.delete_column('census_countydata', 'popwhite2000')

        # Deleting field 'CountyData.popwhite2010'
        db.delete_column('census_countydata', 'popwhite2010')

        # Deleting field 'CountyData.popblack2000'
        db.delete_column('census_countydata', 'popblack2000')

        # Deleting field 'CountyData.popblack2010'
        db.delete_column('census_countydata', 'popblack2010')

        # Deleting field 'CountyData.popamind2000'
        db.delete_column('census_countydata', 'popamind2000')

        # Deleting field 'CountyData.popamind2010'
        db.delete_column('census_countydata', 'popamind2010')

        # Deleting field 'CountyData.popasian2000'
        db.delete_column('census_countydata', 'popasian2000')

        # Deleting field 'CountyData.popasian2010'
        db.delete_column('census_countydata', 'popasian2010')

        # Deleting field 'CountyData.popnathaw2000'
        db.delete_column('census_countydata', 'popnathaw2000')

        # Deleting field 'CountyData.popnathaw2010'
        db.delete_column('census_countydata', 'popnathaw2010')

        # Deleting field 'CountyData.popother2000'
        db.delete_column('census_countydata', 'popother2000')

        # Deleting field 'CountyData.popother2010'
        db.delete_column('census_countydata', 'popother2010')

        # Deleting field 'CountyData.pop2ormore2000'
        db.delete_column('census_countydata', 'pop2ormore2000')

        # Deleting field 'CountyData.pop2ormore2010'
        db.delete_column('census_countydata', 'pop2ormore2010')

        # Deleting field 'CountyData.pophisp2000'
        db.delete_column('census_countydata', 'pophisp2000')

        # Deleting field 'CountyData.pophisp2010'
        db.delete_column('census_countydata', 'pophisp2010')

        # Deleting field 'CountyData.popnonhisp2000'
        db.delete_column('census_countydata', 'popnonhisp2000')

        # Deleting field 'CountyData.popnonhisp2010'
        db.delete_column('census_countydata', 'popnonhisp2010')

        # Deleting field 'CountyData.popwhitenonhisp2000'
        db.delete_column('census_countydata', 'popwhitenonhisp2000')

        # Deleting field 'CountyData.popwhitenonhisp2010'
        db.delete_column('census_countydata', 'popwhitenonhisp2010')

        # Deleting field 'StateData.popwhite2000'
        db.delete_column('census_statedata', 'popwhite2000')

        # Deleting field 'StateData.popwhite2010'
        db.delete_column('census_statedata', 'popwhite2010')

        # Deleting field 'StateData.popblack2000'
        db.delete_column('census_statedata', 'popblack2000')

        # Deleting field 'StateData.popblack2010'
        db.delete_column('census_statedata', 'popblack2010')

        # Deleting field 'StateData.popamind2000'
        db.delete_column('census_statedata', 'popamind2000')

        # Deleting field 'StateData.popamind2010'
        db.delete_column('census_statedata', 'popamind2010')

        # Deleting field 'StateData.popasian2000'
        db.delete_column('census_statedata', 'popasian2000')

        # Deleting field 'StateData.popasian2010'
        db.delete_column('census_statedata', 'popasian2010')

        # Deleting field 'StateData.popnathaw2000'
        db.delete_column('census_statedata', 'popnathaw2000')

        # Deleting field 'StateData.popnathaw2010'
        db.delete_column('census_statedata', 'popnathaw2010')

        # Deleting field 'StateData.popother2000'
        db.delete_column('census_statedata', 'popother2000')

        # Deleting field 'StateData.popother2010'
        db.delete_column('census_statedata', 'popother2010')

        # Deleting field 'StateData.pop2ormore2000'
        db.delete_column('census_statedata', 'pop2ormore2000')

        # Deleting field 'StateData.pop2ormore2010'
        db.delete_column('census_statedata', 'pop2ormore2010')

        # Deleting field 'StateData.pophisp2000'
        db.delete_column('census_statedata', 'pophisp2000')

        # Deleting field 'StateData.pophisp2010'
        db.delete_column('census_statedata', 'pophisp2010')

        # Deleting field 'StateData.popnonhisp2000'
        db.delete_column('census_statedata', 'popnonhisp2000')

        # Deleting field 'StateData.popnonhisp2010'
        db.delete_column('census_statedata', 'popnonhisp2010')

        # Deleting field 'StateData.popwhitenonhisp2000'
        db.delete_column('census_statedata', 'popwhitenonhisp2000')

        # Deleting field 'StateData.popwhitenonhisp2010'
        db.delete_column('census_statedata', 'popwhitenonhisp2010')


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
        }
    }

    complete_apps = ['census']
