from django.db import models

# Create your models here.
class Court(models.Model):
	name = models.CharField( max_length=50 )
	description = models.CharField( max_length=255 )
	active = models.BooleanField( default = True )
	
	objects = models.Manager()

	def __unicode__( self ):
		return self.description

	
class Warrant( models.Model ):
	name = models.CharField( max_length=255 )
	age = models.IntegerField( null = True, blank = True )
	warrant_type = models.CharField( max_length=255,blank = True, null = True )
	bond = models.CharField( max_length=255, blank = True, null = True )
	warrant_number = models.CharField( max_length=255 )
	violation_desc = models.CharField( max_length=255, blank = True, null = True )
	release_cond = models.CharField( max_length=255, blank = True,null = True )  
	court = models.ForeignKey( Court )
	active = models.BooleanField( default = True )
	time_init = models.DateTimeField( "Date Added", auto_now = False, auto_now_add = True, null=False, blank = False )
	time_finished = models.DateTimeField( "Date Finished", auto_now = False, auto_now_add = False, null = True, blank = True )
	
	objects = models.Manager()

	def __unicode__( self ):
		return self.warrant_number
		
	class Meta:
		db_table = "warrant"
		verbose_name = "Warrant"
		verbose_name_plural = "Warrants"
