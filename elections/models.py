from django.db import models
#geodjango support
#from django.contrib.gis.db import models

class Office( models.Model ):
	name = models.CharField( max_length = 155, null = False )
	length_of_term = models.PositiveIntegerField()
	active = models.BooleanField( default = True, null = False )
	
	objects = models.Manager()
	
	def __unicode__( self ):
		return u'%s' % self.name
		
	class Meta:
		verbose_name = 'Office'
		verbose_name_plural = 'Offices'
		ordering = ( 'name', )
		
ELECTION_TYPE_CHOICES = ( 
	('primary','Primary Election'),
	('general','General Election'),
	('special','Special Election'),
	('special2','Presidental Prefererence Election'),
)

class Election( models.Model ):
	name = models.CharField( max_length = 155, null = False )
	date = models.DateField( null = False )
	active = models.BooleanField( default = True, null = False )
	election_type = models.CharField( max_length = 50, choices = ELECTION_TYPE_CHOICES )
	
	objects = models.Manager()
	
	def __unicode__( self ):
		return u'%s' % self.name
		
	class Meta:
		verbose_name = 'Election'
		verbose_name_plural = 'Elections'
		ordering = ( 'date', )
		
class Party( models.Model ):
	name = models.CharField( max_length = 100, null = False, blank = False )
	
	objects = models.Manager()
	
	def __unicode__( self ):
		return u'%s' % self.name 
	
	class Meta:
		verbose_name = 'Political Party'
		verbose_name_plural = 'Political Parties'
		

class Candidate( models.Model ):
	first_name = models.CharField( max_length = 255, null = False )
	middle_name = models.CharField( max_length = 255, null = True, blank = True )
	last_name = models.CharField( max_length = 255, null = False )
	dob = models.DateField( blank = True, null = True )
	party = models.ForeignKey( Party )
	
	objects = models.Manager()
	
	def __unicode__( self ):
		return u'%s %s' % ( self.first_name, self.last_name )
		
	class Meta:
		verbose_name = 'Candidate'
		verbose_name_plural = 'Candidates'
		ordering = ( 'last_name','first_name' )
		


class RaceConfig( models.Model ):
	election = models.ForeignKey( Election )
	office = models.ForeignKey( Office )
	number_candidates = models.PositiveIntegerField( "Number of Candidates" )
	winning_percentage = models.PositiveIntegerField( "Winning Percentage" )
	number_winners = models.PositiveIntegerField( "Number of Winners" )
	
	objects = models.Manager()
	
	def __unicode__( self ):
		return u'%s - %s (%s)' % ( self.election.name, self.office.name, self.election.election_type  )
		
	class Meta:
		verbose_name = 'Race Config'
		verbose_name_plural = 'Race Configs'
		
class Race( models.Model ):
	config = models.ForeignKey( RaceConfig )
	candidate = models.ForeignKey( Candidate )
	votes = models.PositiveIntegerField( blank = True,null = True )
	
	objects = models.Manager()
	
	def __unicode__( self ):
		return u'%s %s %s %s' % ( self.config.election.name, self.candidate.first_name, self.candidate.middle_name, self.candidate.last_name )
	
	class Meta:
		verbose_name = 'Race'
		verbose_name_plural = 'Races'
		
class BallotInitiative( models.Model ):
	election = models.ForeignKey( Election )
	question = models.TextField( blank = False )
	yes_votes = models.PositiveIntegerField()
	no_votes = models.PositiveIntegerField()
	
	objects = models.Manager()
	
	def __unicode__( self ):
		return u'%s' % self.question
	
	class Meta:
		verbose_name = 'Ballot Initiative'
		verbose_name_plural = 'Ballot Initiatives'	
