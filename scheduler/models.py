import datetime
from django.db import models


# Create your models here.
class Position( models.Model ):
	name = models.CharField( max_length = 255 )
	active = models.BooleanField( default = True )
	file_name = models.CharField( max_length = 255 )
	
	def __unicode__( self ):
		return u'%s' % self.name

class Banner( models.Model ):
	name = models.CharField( max_length = 255 )
	active = models.BooleanField( default = True )
	content = models.TextField( blank = False )
	position = models.ForeignKey( Position )
	
	def __unicode__( self ):
		return u'%s' % self.name
	class Meta:
		ordering = [ '-active','id' ]	

class Schedule( models.Model ):
	banner = models.ForeignKey( Banner )
	start_time = models.DateTimeField( blank = False )
	end_time = models.DateTimeField( blank = False )

	def position( self ):
		return self.banner.position
	
	def __unicode__( self ):
		return u'%s  - %s to %s' % (self.banner.name, self.start_time,self.end_time )
