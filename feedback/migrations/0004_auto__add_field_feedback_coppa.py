# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Feedback.coppa'
        db.add_column('feedback_feedback', 'coppa', self.gf('django.db.models.fields.CharField')(default='25-34', max_length=15), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Feedback.coppa'
        db.delete_column('feedback_feedback', 'coppa')


    models = {
        'feedback.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'coppa': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'feedback_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'default': "'message goes here'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'time_init': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['feedback']
