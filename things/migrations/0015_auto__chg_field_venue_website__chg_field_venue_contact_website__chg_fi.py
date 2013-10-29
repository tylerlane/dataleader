# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Venue.website'
        db.alter_column('things_venue', 'website', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Changing field 'Venue.contact_website'
        db.alter_column('things_venue', 'contact_website', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Changing field 'Venue.phone'
        db.alter_column('things_venue', 'phone', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True))

        # Changing field 'Venue.contact_address'
        db.alter_column('things_venue', 'contact_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Changing field 'Venue.contact_email'
        db.alter_column('things_venue', 'contact_email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True))

        # Changing field 'Venue.contact_name'
        db.alter_column('things_venue', 'contact_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Changing field 'Venue.contact_phone'
        db.alter_column('things_venue', 'contact_phone', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True))

        # Changing field 'Venue.email'
        db.alter_column('things_venue', 'email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Changing field 'Event.excitement'
        db.alter_column('things_event', 'excitement', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))

        # Changing field 'Event.description'
        db.alter_column('things_event', 'description', self.gf('django.db.models.fields.TextField')(null=True, blank=True))

        # Changing field 'Event.start_time'
        db.alter_column('things_event', 'start_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True))

        # Changing field 'Event.contact_address'
        db.alter_column('things_event', 'contact_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Changing field 'Event.contact_email'
        db.alter_column('things_event', 'contact_email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True))

        # Changing field 'Event.end_time'
        db.alter_column('things_event', 'end_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True))

        # Changing field 'Event.contact_name'
        db.alter_column('things_event', 'contact_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))

        # Changing field 'Event.contact_phone'
        db.alter_column('things_event', 'contact_phone', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True))

        # Changing field 'Event.contact_website'
        db.alter_column('things_event', 'contact_website', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))


    def backwards(self, orm):
        
        # Changing field 'Venue.website'
        db.alter_column('things_venue', 'website', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Venue.contact_website'
        db.alter_column('things_venue', 'contact_website', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Venue.phone'
        db.alter_column('things_venue', 'phone', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'Venue.contact_address'
        db.alter_column('things_venue', 'contact_address', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Venue.contact_email'
        db.alter_column('things_venue', 'contact_email', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Venue.contact_name'
        db.alter_column('things_venue', 'contact_name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Venue.contact_phone'
        db.alter_column('things_venue', 'contact_phone', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'Venue.email'
        db.alter_column('things_venue', 'email', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Event.excitement'
        db.alter_column('things_event', 'excitement', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Event.description'
        db.alter_column('things_event', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Event.start_time'
        db.alter_column('things_event', 'start_time', self.gf('django.db.models.fields.TimeField')())

        # Changing field 'Event.contact_address'
        db.alter_column('things_event', 'contact_address', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Event.contact_email'
        db.alter_column('things_event', 'contact_email', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Event.end_time'
        db.alter_column('things_event', 'end_time', self.gf('django.db.models.fields.TimeField')())

        # Changing field 'Event.contact_name'
        db.alter_column('things_event', 'contact_name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Event.contact_phone'
        db.alter_column('things_event', 'contact_phone', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'Event.contact_website'
        db.alter_column('things_event', 'contact_website', self.gf('django.db.models.fields.CharField')(max_length=255))


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
            'age': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['things.Age']", 'null': 'True', 'blank': 'True'}),
            'contact_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'contact_website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cost_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'excitement': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['things.Genre']", 'symmetrical': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parking': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '155'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Venue']"})
        },
        'things.genre': {
            'Meta': {'object_name': 'Genre'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'app_layout': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
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
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        'things.venue': {
            'Meta': {'object_name': 'Venue'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'contact_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'contact_website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'geom_area': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'place_to_go': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['things']
