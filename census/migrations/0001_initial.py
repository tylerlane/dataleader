# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CountyData'
        db.create_table('census_countydata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('county_name', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('state', self.gf('django.db.models.fields.CharField')(max_length='2')),
            ('pop2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2000SqMile', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2010SqMile', self.gf('django.db.models.fields.IntegerField')()),
            ('pctwhite2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctwhite2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctblack2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctblack2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctamind2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctamind2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctasian2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctasian2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctnathaw2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctnathaw2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctother2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctother2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pct2ormore2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pct2ormore2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pcthisp2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pcthisp2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctnonhisp2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctnonhisp2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctwhitenonhisp2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctwhitenonhisp2010', self.gf('django.db.models.fields.IntegerField')()),
            ('dividx2000', self.gf('django.db.models.fields.IntegerField')()),
            ('dividx2010', self.gf('django.db.models.fields.IntegerField')()),
            ('total_sqmiles', self.gf('django.db.models.fields.IntegerField')()),
            ('water_sqmiles', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('census', ['CountyData'])

        # Adding model 'StateData'
        db.create_table('census_statedata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length='2')),
            ('pop2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2000SqMile', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2010SqMile', self.gf('django.db.models.fields.IntegerField')()),
            ('pctwhite2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctwhite2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctblack2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctblack2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctamind2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctamind2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctasian2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctasian2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctnathaw2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctnathaw2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctother2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctother2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pct2ormore2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pct2ormore2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pcthisp2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pcthisp2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctnonhisp2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctnonhisp2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctwhitenonhisp2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctwhitenonhisp2010', self.gf('django.db.models.fields.IntegerField')()),
            ('dividx2000', self.gf('django.db.models.fields.IntegerField')()),
            ('dividx2010', self.gf('django.db.models.fields.IntegerField')()),
            ('total_sqmiles', self.gf('django.db.models.fields.IntegerField')()),
            ('water_sqmiles', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('census', ['StateData'])

        # Adding model 'TractData'
        db.create_table('census_tractdata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tract_name', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('state', self.gf('django.db.models.fields.CharField')(max_length='2')),
            ('pop2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2000SqMile', self.gf('django.db.models.fields.IntegerField')()),
            ('pop2010SqMile', self.gf('django.db.models.fields.IntegerField')()),
            ('pctwhite2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctwhite2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctblack2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctblack2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctamind2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctamind2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctasian2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctasian2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctnathaw2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctnathaw2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctother2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctother2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pct2ormore2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pct2ormore2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pcthisp2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pcthisp2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctnonhisp2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctnonhisp2010', self.gf('django.db.models.fields.IntegerField')()),
            ('pctwhitenonhisp2000', self.gf('django.db.models.fields.IntegerField')()),
            ('pctwhitenonhisp2010', self.gf('django.db.models.fields.IntegerField')()),
            ('dividx2000', self.gf('django.db.models.fields.IntegerField')()),
            ('dividx2010', self.gf('django.db.models.fields.IntegerField')()),
            ('total_sqmiles', self.gf('django.db.models.fields.IntegerField')()),
            ('water_sqmiles', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('census', ['TractData'])


    def backwards(self, orm):
        
        # Deleting model 'CountyData'
        db.delete_table('census_countydata')

        # Deleting model 'StateData'
        db.delete_table('census_statedata')

        # Deleting model 'TractData'
        db.delete_table('census_tractdata')


    models = {
        'census.countydata': {
            'Meta': {'object_name': 'CountyData'},
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
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
