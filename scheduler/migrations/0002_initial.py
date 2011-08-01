# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Position'
        db.create_table('scheduler_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('scheduler', ['Position'])

        # Adding model 'Banner'
        db.create_table('scheduler_banner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scheduler.Position'])),
        ))
        db.send_create_signal('scheduler', ['Banner'])

        # Adding model 'Schedule'
        db.create_table('scheduler_schedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('banner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scheduler.Banner'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('scheduler', ['Schedule'])


    def backwards(self, orm):
        
        # Deleting model 'Position'
        db.delete_table('scheduler_position')

        # Deleting model 'Banner'
        db.delete_table('scheduler_banner')

        # Deleting model 'Schedule'
        db.delete_table('scheduler_schedule')


    models = {
        'scheduler.banner': {
            'Meta': {'object_name': 'Banner'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scheduler.Position']"})
        },
        'scheduler.position': {
            'Meta': {'object_name': 'Position'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'scheduler.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scheduler.Banner']"}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['scheduler']
