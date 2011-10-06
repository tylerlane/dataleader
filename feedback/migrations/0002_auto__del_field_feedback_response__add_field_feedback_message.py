# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Feedback.response'
        db.delete_column('feedback_feedback', 'response')

        # Adding field 'Feedback.message'
        db.add_column('feedback_feedback', 'message', self.gf('django.db.models.fields.TextField')(default='message goes here'), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Feedback.response'
        db.add_column('feedback_feedback', 'response', self.gf('django.db.models.fields.TextField')(default='test'), keep_default=False)

        # Deleting field 'Feedback.message'
        db.delete_column('feedback_feedback', 'message')


    models = {
        'feedback.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'feedback_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'default': "'message goes here'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['feedback']
