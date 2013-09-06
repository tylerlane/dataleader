# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Venue.active'
        db.add_column('things_venue', 'active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Venue.active'
        db.delete_column('things_venue', 'active')


    models = {
        'things.age': {
            'Meta': {'object_name': 'Age'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'age_max': ('django.db.models.fields.IntegerField', [], {}),
            'age_min': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'things.event': {
            'Meta': {'object_name': 'Event'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'age': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['things.Age']", 'symmetrical': 'False'}),
            'contact_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'contact_website': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'cost_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'excitement': ('django.db.models.fields.FloatField', [], {}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['things.Genre']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parking': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'time': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['things.Time']", 'symmetrical': 'False'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Venue']"})
        },
        'things.genre': {
            'Meta': {'object_name': 'Genre'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['things.Genre']", 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'things.photo': {
            'Meta': {'object_name': 'Photo'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'things.time': {
            'Meta': {'object_name': 'Time'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        'things.venue': {
            'Meta': {'object_name': 'Venue'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'contact_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'contact_website': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'geom_area': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'place_to_go': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['things']
