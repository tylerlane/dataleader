# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'AYPSummary.add_ind_status'
        db.alter_column('schools_aypsummary', 'add_ind_status', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True))

        # Changing field 'AYPSummary.math_status'
        db.alter_column('schools_aypsummary', 'math_status', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True))

        # Changing field 'AYPSummary.comm_arts_status'
        db.alter_column('schools_aypsummary', 'comm_arts_status', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True))


    def backwards(self, orm):
        
        # Changing field 'AYPSummary.add_ind_status'
        db.alter_column('schools_aypsummary', 'add_ind_status', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'AYPSummary.math_status'
        db.alter_column('schools_aypsummary', 'math_status', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'AYPSummary.comm_arts_status'
        db.alter_column('schools_aypsummary', 'comm_arts_status', self.gf('django.db.models.fields.BooleanField')(blank=True))


    models = {
        'schools.aypdetail': {
            'Meta': {'object_name': 'AYPDetail'},
            'attendance_pct': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_asian_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_black_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_hispanic_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_indian_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_low_english_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_low_income_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_other_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_school_total': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_special_ed_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_white_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.District']"}),
            'graduation_pct': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'math_asian_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_black_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_hispanic_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_indian_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_low_english_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_low_income_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_other_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_school_total': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_special_ed_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_white_prof': ('django.db.models.fields.FloatField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.School']", 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        'schools.aypsummary': {
            'Meta': {'object_name': 'AYPSummary'},
            'add_ind_status': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'comm_arts_status': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'math_status': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.School']", 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        'schools.district': {
            'Meta': {'object_name': 'District'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'schools.school': {
            'Meta': {'object_name': 'School'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school_type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['schools']
