# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Court'
        db.create_table('warrants_court', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('warrants', ['Court'])

        # Adding model 'Warrant'
        db.create_table('warrant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('warrant_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bond', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('warrant_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('violation_desc', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('release_cond', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('court', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['warrants.Court'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('time_init', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_finished', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('warrants', ['Warrant'])


    def backwards(self, orm):
        
        # Deleting model 'Court'
        db.delete_table('warrants_court')

        # Deleting model 'Warrant'
        db.delete_table('warrant')


    models = {
        'warrants.court': {
            'Meta': {'object_name': 'Court'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'warrants.warrant': {
            'Meta': {'object_name': 'Warrant', 'db_table': "'warrant'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bond': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'court': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['warrants.Court']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'release_cond': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_finished': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_init': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'violation_desc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'warrant_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'warrant_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['warrants']
