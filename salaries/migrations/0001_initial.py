# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Organization'
        db.create_table('salaries_organization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('salaries', ['Organization'])

        # Adding model 'Person'
        db.create_table('salaries_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salaries.Organization'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hire_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('employment_type', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('salaries', ['Person'])

        # Adding model 'Salary'
        db.create_table('salaries_salary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salaries.Person'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('compensation', self.gf('django.db.models.fields.IntegerField')()),
            ('compensation_type', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('salaries', ['Salary'])


    def backwards(self, orm):
        
        # Deleting model 'Organization'
        db.delete_table('salaries_organization')

        # Deleting model 'Person'
        db.delete_table('salaries_person')

        # Deleting model 'Salary'
        db.delete_table('salaries_salary')


    models = {
        'salaries.organization': {
            'Meta': {'object_name': 'Organization'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'salaries.person': {
            'Meta': {'object_name': 'Person'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'employment_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hire_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['salaries.Organization']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'salaries.salary': {
            'Meta': {'object_name': 'Salary'},
            'compensation': ('django.db.models.fields.IntegerField', [], {}),
            'compensation_type': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['salaries.Person']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['salaries']
