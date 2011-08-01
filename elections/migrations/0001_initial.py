# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Office'
        db.create_table('elections_office', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=155)),
            ('length_of_term', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('elections', ['Office'])

        # Adding model 'Election'
        db.create_table('elections_election', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=155)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('election_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('elections', ['Election'])

        # Adding model 'Party'
        db.create_table('elections_party', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('elections', ['Party'])

        # Adding model 'Candidate'
        db.create_table('elections_candidate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elections.Party'])),
        ))
        db.send_create_signal('elections', ['Candidate'])

        # Adding model 'RaceConfig'
        db.create_table('elections_raceconfig', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('election', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elections.Election'])),
            ('office', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elections.Office'])),
            ('number_candidates', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('winning_percentage', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('number_winners', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('elections', ['RaceConfig'])

        # Adding model 'Race'
        db.create_table('elections_race', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elections.RaceConfig'])),
            ('candidate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elections.Candidate'])),
            ('votes', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('elections', ['Race'])

        # Adding model 'BallotInitiative'
        db.create_table('elections_ballotinitiative', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('election', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elections.Election'])),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('yes_votes', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('no_votes', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('elections', ['BallotInitiative'])


    def backwards(self, orm):
        
        # Deleting model 'Office'
        db.delete_table('elections_office')

        # Deleting model 'Election'
        db.delete_table('elections_election')

        # Deleting model 'Party'
        db.delete_table('elections_party')

        # Deleting model 'Candidate'
        db.delete_table('elections_candidate')

        # Deleting model 'RaceConfig'
        db.delete_table('elections_raceconfig')

        # Deleting model 'Race'
        db.delete_table('elections_race')

        # Deleting model 'BallotInitiative'
        db.delete_table('elections_ballotinitiative')


    models = {
        'elections.ballotinitiative': {
            'Meta': {'object_name': 'BallotInitiative'},
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elections.Election']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_votes': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'yes_votes': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'elections.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elections.Party']"})
        },
        'elections.election': {
            'Meta': {'object_name': 'Election'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'election_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '155'})
        },
        'elections.office': {
            'Meta': {'object_name': 'Office'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_of_term': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '155'})
        },
        'elections.party': {
            'Meta': {'object_name': 'Party'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'elections.race': {
            'Meta': {'object_name': 'Race'},
            'candidate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elections.Candidate']"}),
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elections.RaceConfig']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'elections.raceconfig': {
            'Meta': {'object_name': 'RaceConfig'},
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elections.Election']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_candidates': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'number_winners': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elections.Office']"}),
            'winning_percentage': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['elections']
