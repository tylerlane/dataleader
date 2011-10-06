# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'AYPDetail.comm_white_prof'
        db.alter_column('schools_aypdetail', 'comm_white_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_hispanic_prof'
        db.alter_column('schools_aypdetail', 'comm_hispanic_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_low_income_prof'
        db.alter_column('schools_aypdetail', 'comm_low_income_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_black_prof'
        db.alter_column('schools_aypdetail', 'comm_black_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_asian_prof'
        db.alter_column('schools_aypdetail', 'comm_asian_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_white_prof'
        db.alter_column('schools_aypdetail', 'math_white_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_other_prof'
        db.alter_column('schools_aypdetail', 'math_other_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_indian_prof'
        db.alter_column('schools_aypdetail', 'math_indian_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_asian_prof'
        db.alter_column('schools_aypdetail', 'math_asian_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_low_english_prof'
        db.alter_column('schools_aypdetail', 'math_low_english_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.graduation_pct'
        db.alter_column('schools_aypdetail', 'graduation_pct', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_hispanic_prof'
        db.alter_column('schools_aypdetail', 'math_hispanic_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_school_total'
        db.alter_column('schools_aypdetail', 'comm_school_total', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_black_prof'
        db.alter_column('schools_aypdetail', 'math_black_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_indian_prof'
        db.alter_column('schools_aypdetail', 'comm_indian_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_low_english_prof'
        db.alter_column('schools_aypdetail', 'comm_low_english_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_special_ed_prof'
        db.alter_column('schools_aypdetail', 'comm_special_ed_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_special_ed_prof'
        db.alter_column('schools_aypdetail', 'math_special_ed_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.attendance_pct'
        db.alter_column('schools_aypdetail', 'attendance_pct', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_low_income_prof'
        db.alter_column('schools_aypdetail', 'math_low_income_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_other_prof'
        db.alter_column('schools_aypdetail', 'comm_other_prof', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_school_total'
        db.alter_column('schools_aypdetail', 'math_school_total', self.gf('django.db.models.fields.FloatField')(max_length=5, null=True, blank=True))


    def backwards(self, orm):
        
        # Changing field 'AYPDetail.comm_white_prof'
        db.alter_column('schools_aypdetail', 'comm_white_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_hispanic_prof'
        db.alter_column('schools_aypdetail', 'comm_hispanic_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_low_income_prof'
        db.alter_column('schools_aypdetail', 'comm_low_income_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_black_prof'
        db.alter_column('schools_aypdetail', 'comm_black_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_asian_prof'
        db.alter_column('schools_aypdetail', 'comm_asian_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_white_prof'
        db.alter_column('schools_aypdetail', 'math_white_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_other_prof'
        db.alter_column('schools_aypdetail', 'math_other_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_indian_prof'
        db.alter_column('schools_aypdetail', 'math_indian_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_asian_prof'
        db.alter_column('schools_aypdetail', 'math_asian_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_low_english_prof'
        db.alter_column('schools_aypdetail', 'math_low_english_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.graduation_pct'
        db.alter_column('schools_aypdetail', 'graduation_pct', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_hispanic_prof'
        db.alter_column('schools_aypdetail', 'math_hispanic_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_school_total'
        db.alter_column('schools_aypdetail', 'comm_school_total', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_black_prof'
        db.alter_column('schools_aypdetail', 'math_black_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_indian_prof'
        db.alter_column('schools_aypdetail', 'comm_indian_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_low_english_prof'
        db.alter_column('schools_aypdetail', 'comm_low_english_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_special_ed_prof'
        db.alter_column('schools_aypdetail', 'comm_special_ed_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_special_ed_prof'
        db.alter_column('schools_aypdetail', 'math_special_ed_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.attendance_pct'
        db.alter_column('schools_aypdetail', 'attendance_pct', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_low_income_prof'
        db.alter_column('schools_aypdetail', 'math_low_income_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.comm_other_prof'
        db.alter_column('schools_aypdetail', 'comm_other_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))

        # Changing field 'AYPDetail.math_school_total'
        db.alter_column('schools_aypdetail', 'math_school_total', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True))


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
            'add_ind_status': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'comm_arts_status': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'math_status': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
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
