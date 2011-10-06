# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Jurisdiction'
        db.create_table('jurisdiction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('time_init', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('calls', ['Jurisdiction'])

        # Adding model 'CallType'
        db.create_table('call_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('time_init', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('jurisdiction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calls.Jurisdiction'])),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=150, null=True)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('reversepub', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('calls', ['CallType'])

        # Adding model 'Beat'
        db.create_table('beat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('jurisdiction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calls.Jurisdiction'])),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('calls', ['Beat'])

        # Adding model 'Call'
        db.create_table('call', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('call_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('response', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('event_num', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('report_num', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('calltype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calls.CallType'])),
            ('beat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calls.Beat'])),
            ('jurisdiction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calls.Jurisdiction'])),
            ('geocoder', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
        ))
        db.send_create_signal('calls', ['Call'])


    def backwards(self, orm):
        
        # Deleting model 'Jurisdiction'
        db.delete_table('jurisdiction')

        # Deleting model 'CallType'
        db.delete_table('call_type')

        # Deleting model 'Beat'
        db.delete_table('beat')

        # Deleting model 'Call'
        db.delete_table('call')


    models = {
        'calls.beat': {
            'Meta': {'object_name': 'Beat', 'db_table': "'beat'"},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurisdiction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['calls.Jurisdiction']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'calls.call': {
            'Meta': {'object_name': 'Call', 'db_table': "'call'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'beat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['calls.Beat']"}),
            'call_time': ('django.db.models.fields.DateTimeField', [], {}),
            'calltype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['calls.CallType']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'event_num': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'geocoder': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurisdiction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['calls.Jurisdiction']"}),
            'report_num': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'calls.calltype': {
            'Meta': {'object_name': 'CallType', 'db_table': "'call_type'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurisdiction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['calls.Jurisdiction']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reversepub': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'time_init': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'calls.jurisdiction': {
            'Meta': {'object_name': 'Jurisdiction', 'db_table': "'jurisdiction'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'time_init': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['calls']
