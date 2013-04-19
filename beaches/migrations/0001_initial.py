# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Beach'
        db.create_table('beaches_beach', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beach_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('openclosed', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('parkname', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('results1', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('results2', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('sampletaken', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('beaches', ['Beach'])


    def backwards(self, orm):
        
        # Deleting model 'Beach'
        db.delete_table('beaches_beach')


    models = {
        'beaches.beach': {
            'Meta': {'object_name': 'Beach'},
            'beach_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'openclosed': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'parkname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'results1': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'results2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'sampletaken': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['beaches']
