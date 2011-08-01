# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'TractData.land_sqmiles'
        db.add_column('census_tractdata', 'land_sqmiles', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Changing field 'TractData.dividx2010'
        db.alter_column('census_tractdata', 'dividx2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pct2ormore2010'
        db.alter_column('census_tractdata', 'pct2ormore2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pcthisp2010'
        db.alter_column('census_tractdata', 'pcthisp2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctamind2000'
        db.alter_column('census_tractdata', 'pctamind2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.water_sqmiles'
        db.alter_column('census_tractdata', 'water_sqmiles', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctasian2000'
        db.alter_column('census_tractdata', 'pctasian2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctwhitenonhisp2000'
        db.alter_column('census_tractdata', 'pctwhitenonhisp2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pop2000SqMile'
        db.alter_column('census_tractdata', 'pop2000SqMile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctother2010'
        db.alter_column('census_tractdata', 'pctother2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctblack2010'
        db.alter_column('census_tractdata', 'pctblack2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctnonhisp2010'
        db.alter_column('census_tractdata', 'pctnonhisp2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctwhite2010'
        db.alter_column('census_tractdata', 'pctwhite2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.dividx2000'
        db.alter_column('census_tractdata', 'dividx2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pct2ormore2000'
        db.alter_column('census_tractdata', 'pct2ormore2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.total_sqmiles'
        db.alter_column('census_tractdata', 'total_sqmiles', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctamind2010'
        db.alter_column('census_tractdata', 'pctamind2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctnathaw2010'
        db.alter_column('census_tractdata', 'pctnathaw2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctasian2010'
        db.alter_column('census_tractdata', 'pctasian2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctwhitenonhisp2010'
        db.alter_column('census_tractdata', 'pctwhitenonhisp2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pop2010SqMile'
        db.alter_column('census_tractdata', 'pop2010SqMile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctother2000'
        db.alter_column('census_tractdata', 'pctother2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pcthisp2000'
        db.alter_column('census_tractdata', 'pcthisp2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctblack2000'
        db.alter_column('census_tractdata', 'pctblack2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctnonhisp2000'
        db.alter_column('census_tractdata', 'pctnonhisp2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctwhite2000'
        db.alter_column('census_tractdata', 'pctwhite2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'TractData.pctnathaw2000'
        db.alter_column('census_tractdata', 'pctnathaw2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Adding field 'StateData.land_sqmiles'
        db.add_column('census_statedata', 'land_sqmiles', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Changing field 'StateData.dividx2010'
        db.alter_column('census_statedata', 'dividx2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pct2ormore2010'
        db.alter_column('census_statedata', 'pct2ormore2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pcthisp2010'
        db.alter_column('census_statedata', 'pcthisp2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctamind2000'
        db.alter_column('census_statedata', 'pctamind2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.water_sqmiles'
        db.alter_column('census_statedata', 'water_sqmiles', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctasian2000'
        db.alter_column('census_statedata', 'pctasian2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctwhitenonhisp2000'
        db.alter_column('census_statedata', 'pctwhitenonhisp2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pop2000SqMile'
        db.alter_column('census_statedata', 'pop2000SqMile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctother2010'
        db.alter_column('census_statedata', 'pctother2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctblack2010'
        db.alter_column('census_statedata', 'pctblack2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.total_sqmiles'
        db.alter_column('census_statedata', 'total_sqmiles', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctnonhisp2010'
        db.alter_column('census_statedata', 'pctnonhisp2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctwhite2010'
        db.alter_column('census_statedata', 'pctwhite2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.dividx2000'
        db.alter_column('census_statedata', 'dividx2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pct2ormore2000'
        db.alter_column('census_statedata', 'pct2ormore2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pcthisp2000'
        db.alter_column('census_statedata', 'pcthisp2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctamind2010'
        db.alter_column('census_statedata', 'pctamind2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctnathaw2010'
        db.alter_column('census_statedata', 'pctnathaw2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctasian2010'
        db.alter_column('census_statedata', 'pctasian2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctwhitenonhisp2010'
        db.alter_column('census_statedata', 'pctwhitenonhisp2010', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pop2010SqMile'
        db.alter_column('census_statedata', 'pop2010SqMile', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctother2000'
        db.alter_column('census_statedata', 'pctother2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctblack2000'
        db.alter_column('census_statedata', 'pctblack2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctnonhisp2000'
        db.alter_column('census_statedata', 'pctnonhisp2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctwhite2000'
        db.alter_column('census_statedata', 'pctwhite2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'StateData.pctnathaw2000'
        db.alter_column('census_statedata', 'pctnathaw2000', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))


    def backwards(self, orm):
        
        # Deleting field 'TractData.land_sqmiles'
        db.delete_column('census_tractdata', 'land_sqmiles')

        # Changing field 'TractData.dividx2010'
        db.alter_column('census_tractdata', 'dividx2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pct2ormore2010'
        db.alter_column('census_tractdata', 'pct2ormore2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pcthisp2010'
        db.alter_column('census_tractdata', 'pcthisp2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctamind2000'
        db.alter_column('census_tractdata', 'pctamind2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.water_sqmiles'
        db.alter_column('census_tractdata', 'water_sqmiles', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctasian2000'
        db.alter_column('census_tractdata', 'pctasian2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctwhitenonhisp2000'
        db.alter_column('census_tractdata', 'pctwhitenonhisp2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pop2000SqMile'
        db.alter_column('census_tractdata', 'pop2000SqMile', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctother2010'
        db.alter_column('census_tractdata', 'pctother2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctblack2010'
        db.alter_column('census_tractdata', 'pctblack2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctnonhisp2010'
        db.alter_column('census_tractdata', 'pctnonhisp2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctwhite2010'
        db.alter_column('census_tractdata', 'pctwhite2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.dividx2000'
        db.alter_column('census_tractdata', 'dividx2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pct2ormore2000'
        db.alter_column('census_tractdata', 'pct2ormore2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.total_sqmiles'
        db.alter_column('census_tractdata', 'total_sqmiles', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctamind2010'
        db.alter_column('census_tractdata', 'pctamind2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctnathaw2010'
        db.alter_column('census_tractdata', 'pctnathaw2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctasian2010'
        db.alter_column('census_tractdata', 'pctasian2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctwhitenonhisp2010'
        db.alter_column('census_tractdata', 'pctwhitenonhisp2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pop2010SqMile'
        db.alter_column('census_tractdata', 'pop2010SqMile', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctother2000'
        db.alter_column('census_tractdata', 'pctother2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pcthisp2000'
        db.alter_column('census_tractdata', 'pcthisp2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctblack2000'
        db.alter_column('census_tractdata', 'pctblack2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctnonhisp2000'
        db.alter_column('census_tractdata', 'pctnonhisp2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctwhite2000'
        db.alter_column('census_tractdata', 'pctwhite2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'TractData.pctnathaw2000'
        db.alter_column('census_tractdata', 'pctnathaw2000', self.gf('django.db.models.fields.IntegerField')())

        # Deleting field 'StateData.land_sqmiles'
        db.delete_column('census_statedata', 'land_sqmiles')

        # Changing field 'StateData.dividx2010'
        db.alter_column('census_statedata', 'dividx2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pct2ormore2010'
        db.alter_column('census_statedata', 'pct2ormore2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pcthisp2010'
        db.alter_column('census_statedata', 'pcthisp2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctamind2000'
        db.alter_column('census_statedata', 'pctamind2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.water_sqmiles'
        db.alter_column('census_statedata', 'water_sqmiles', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctasian2000'
        db.alter_column('census_statedata', 'pctasian2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctwhitenonhisp2000'
        db.alter_column('census_statedata', 'pctwhitenonhisp2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pop2000SqMile'
        db.alter_column('census_statedata', 'pop2000SqMile', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctother2010'
        db.alter_column('census_statedata', 'pctother2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctblack2010'
        db.alter_column('census_statedata', 'pctblack2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.total_sqmiles'
        db.alter_column('census_statedata', 'total_sqmiles', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctnonhisp2010'
        db.alter_column('census_statedata', 'pctnonhisp2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctwhite2010'
        db.alter_column('census_statedata', 'pctwhite2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.dividx2000'
        db.alter_column('census_statedata', 'dividx2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pct2ormore2000'
        db.alter_column('census_statedata', 'pct2ormore2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pcthisp2000'
        db.alter_column('census_statedata', 'pcthisp2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctamind2010'
        db.alter_column('census_statedata', 'pctamind2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctnathaw2010'
        db.alter_column('census_statedata', 'pctnathaw2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctasian2010'
        db.alter_column('census_statedata', 'pctasian2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctwhitenonhisp2010'
        db.alter_column('census_statedata', 'pctwhitenonhisp2010', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pop2010SqMile'
        db.alter_column('census_statedata', 'pop2010SqMile', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctother2000'
        db.alter_column('census_statedata', 'pctother2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctblack2000'
        db.alter_column('census_statedata', 'pctblack2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctnonhisp2000'
        db.alter_column('census_statedata', 'pctnonhisp2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctwhite2000'
        db.alter_column('census_statedata', 'pctwhite2000', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'StateData.pctnathaw2000'
        db.alter_column('census_statedata', 'pctnathaw2000', self.gf('django.db.models.fields.IntegerField')())


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
            'pop2000': ('django.db.models.fields.IntegerField', [], {}),
            'pop2000SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010': ('django.db.models.fields.IntegerField', [], {}),
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
            'pop2000': ('django.db.models.fields.IntegerField', [], {}),
            'pop2000SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010': ('django.db.models.fields.IntegerField', [], {}),
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
            'pop2000': ('django.db.models.fields.IntegerField', [], {}),
            'pop2000SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop2010': ('django.db.models.fields.IntegerField', [], {}),
            'pop2010SqMile': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'total_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tract_name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'water_sqmiles': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['census']
