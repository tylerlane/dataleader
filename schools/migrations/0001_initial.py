# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'District'
        db.create_table('schools_district', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('schools', ['District'])

        # Adding model 'School'
        db.create_table('schools_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.District'])),
            ('school_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('schools', ['School'])

        # Adding model 'AYPSummary'
        db.create_table('schools_aypsummary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.School'], null=True, blank=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.District'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('comm_arts_status', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('math_status', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('add_ind_status', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('schools', ['AYPSummary'])

        # Adding model 'AYPDetail'
        db.create_table('schools_aypdetail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.School'], null=True, blank=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.District'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('school_total', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('comm_asian_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('comm_black_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('comm_hispanic_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('comm_indian_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('comm_white_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('comm_other_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('comm_low_income_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('comm_special_ed_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('comm_low_english_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('math_asian_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('math_black_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('math_hispanic_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('math_indian_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('math_white_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('math_other_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('math_low_income_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('math_special_ed_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('math_low_english_prof', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('attendance_pct', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('graduation_pct', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
        ))
        db.send_create_signal('schools', ['AYPDetail'])


    def backwards(self, orm):
        
        # Deleting model 'District'
        db.delete_table('schools_district')

        # Deleting model 'School'
        db.delete_table('schools_school')

        # Deleting model 'AYPSummary'
        db.delete_table('schools_aypsummary')

        # Deleting model 'AYPDetail'
        db.delete_table('schools_aypdetail')


    models = {
        'schools.aypdetail': {
            'Meta': {'object_name': 'AYPDetail'},
            'attendance_pct': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_asian_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_black_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_hispanic_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_indian_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_low_english_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_low_income_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_other_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_special_ed_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'comm_white_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.District']"}),
            'graduation_pct': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'math_asian_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_black_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_hispanic_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_indian_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_low_english_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_low_income_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_other_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_special_ed_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'math_white_prof': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.School']", 'null': 'True', 'blank': 'True'}),
            'school_total': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
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
