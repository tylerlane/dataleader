# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Genre'
        db.create_table('things_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Genre'])),
            ('description', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal('things', ['Genre'])

        # Adding model 'Age'
        db.create_table('things_age', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('age_min', self.gf('django.db.models.fields.IntegerField')()),
            ('age_max', self.gf('django.db.models.fields.IntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('things', ['Age'])

        # Adding model 'Venue'
        db.create_table('things_venue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('geom_area', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(null=True, blank=True)),
            ('place_to_go', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact_address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('contact_email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contact_website', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('things', ['Venue'])

        # Adding model 'Time'
        db.create_table('things_time', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('things', ['Time'])

        # Adding model 'Photo'
        db.create_table('things_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('things', ['Photo'])

        # Adding model 'Event'
        db.create_table('things_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('parking', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Venue'])),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
            ('cost_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('excitement', self.gf('django.db.models.fields.FloatField')()),
            ('main_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Photo'])),
            ('age', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Age'])),
            ('time', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['things.Time'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact_address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('contact_email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contact_website', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('things', ['Event'])

        # Adding M2M table for field genre on 'Event'
        db.create_table('things_event_genre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['things.event'], null=False)),
            ('genre', models.ForeignKey(orm['things.genre'], null=False))
        ))
        db.create_unique('things_event_genre', ['event_id', 'genre_id'])


    def backwards(self, orm):
        
        # Deleting model 'Genre'
        db.delete_table('things_genre')

        # Deleting model 'Age'
        db.delete_table('things_age')

        # Deleting model 'Venue'
        db.delete_table('things_venue')

        # Deleting model 'Time'
        db.delete_table('things_time')

        # Deleting model 'Photo'
        db.delete_table('things_photo')

        # Deleting model 'Event'
        db.delete_table('things_event')

        # Removing M2M table for field genre on 'Event'
        db.delete_table('things_event_genre')


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
            'age': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Age']"}),
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
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Photo']"}),
            'time': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Time']"}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Venue']"})
        },
        'things.genre': {
            'Meta': {'object_name': 'Genre'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['things.Genre']"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'things.photo': {
            'Meta': {'object_name': 'Photo'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
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
