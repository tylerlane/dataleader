# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CarsFeed'
        db.create_table('ads_carsfeed', (
            ('model_year', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('make_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('model_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('trim_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(max_length=22, null=True, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('mileage', self.gf('django.db.models.fields.IntegerField')(max_length=22, null=True, blank=True)),
            ('add_date', self.gf('django.db.models.fields.DateField')()),
            ('vin', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('stock_number', self.gf('django.db.models.fields.IntegerField')()),
            ('engine', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('body_style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('transmission', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('exterior_color', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('interior_color', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('standard_features', self.gf('django.db.models.fields.TextField')(max_length=2000, null=True, blank=True)),
            ('optional_features', self.gf('django.db.models.fields.TextField')(max_length=2000, null=True, blank=True)),
            ('dealer_id', self.gf('django.db.models.fields.IntegerField')(max_length=20, null=True)),
            ('dealer_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.TextField')(max_length=510)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dealer_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('affiliate', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('pub1', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('pub2', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('pub3', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('pub4', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('pub5', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('pub6', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('pa_id', self.gf('django.db.models.fields.IntegerField')(max_length=20, primary_key=True)),
            ('modification_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cpo', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('photo_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=1005, null=True, blank=True)),
            ('original_image', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('ads', ['CarsFeed'])


    def backwards(self, orm):
        
        # Deleting model 'CarsFeed'
        db.delete_table('ads_carsfeed')


    models = {
        'ads.carsfeed': {
            'Meta': {'object_name': 'CarsFeed'},
            'add_date': ('django.db.models.fields.DateField', [], {}),
            'address': ('django.db.models.fields.TextField', [], {'max_length': '510'}),
            'affiliate': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'body_style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cpo': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'dealer_id': ('django.db.models.fields.IntegerField', [], {'max_length': '20', 'null': 'True'}),
            'dealer_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'dealer_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'engine': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'exterior_color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'interior_color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'make_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mileage': ('django.db.models.fields.IntegerField', [], {'max_length': '22', 'null': 'True', 'blank': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'model_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'modification_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1005', 'null': 'True', 'blank': 'True'}),
            'optional_features': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'original_image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pa_id': ('django.db.models.fields.IntegerField', [], {'max_length': '20', 'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'photo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'max_length': '22', 'null': 'True', 'blank': 'True'}),
            'pub1': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'pub2': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'pub3': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'pub4': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'pub5': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'pub6': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'standard_features': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'stock_number': ('django.db.models.fields.IntegerField', [], {}),
            'transmission': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trim_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'vin': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['ads']
