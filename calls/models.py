from django.db import models,IntegrityError
#geodjango support
from django.contrib.gis.db import models
import datetime


# Create your models here.
class Jurisdiction( models.Model ):
	name = models.CharField( max_length = 150 )
	active = models.BooleanField()
	time_init = models.DateTimeField( "Date Added", auto_now =  False, auto_now_add = True )
	
	objects = models.Manager()
	
	def __unicode__( self ):
		return self.name
		
	class Meta:
		db_table = "jurisdiction"
		verbose_name = "Jurisdiction"
		verbose_name_plural = "Jurisdictions"
		ordering = ( "name","active", "time_init", )

#calltype model		
class CallType( models.Model ):
	name = models.CharField( max_length = 50 )
	description = models.CharField( max_length = 150 )
	active = models.BooleanField()
	time_init = models.DateTimeField( "Date Added", auto_now = False, auto_now_add = True )
	jurisdiction = models.ForeignKey( Jurisdiction )
	category = models.CharField( max_length=150,null=True )
	icon = models.CharField( max_length=255,null=True )
	reversepub = models.BooleanField( "Reverse Pub", default=True )
	objects = models.Manager()
	
	def __unicode__( self ):
		return self.name
		
	class Meta:
		db_table = "call_type"
		verbose_name = "Call Type"
		verbose_name_plural = "Call Types"
		ordering = ( "name","description","active","time_init", )

#beat model
class Beat( models.Model ):
	name = models.CharField( max_length = 25 )
	jurisdiction = models.ForeignKey( Jurisdiction )
	geom = models.MultiPolygonField()

	models.GeoManager()

	def __unicode__( self ):
		return self.name
	class Meta:
		db_table = "beat"
		verbose_name = "Beat"
		verbose_name_plural = "Beats"
		ordering = ( "name","jurisdiction", "geom", )

#call model	
class Call( models.Model ):
	call_time = models.DateTimeField( "Call Time", auto_now = False, auto_now_add = False )
	description = models.CharField( max_length = 150 )
	response = models.CharField( max_length = 50 )
	event_num = models.CharField( max_length = 20 )
	report_num = models.CharField( max_length = 20 )
	address = models.CharField( max_length = 150 )
	zip_code = models.CharField( max_length = 10 )
	geom = models.PointField(srid=4326)
	calltype = models.ForeignKey(CallType)
	beat = models.ForeignKey(Beat)
	jurisdiction = models.ForeignKey(Jurisdiction)
	geocoder = models.CharField( max_length = 25,null=True )
	
	objects = models.GeoManager()
	
	class Meta:
		db_table = "call"
		verbose_name = ( "Call" )
		verbose_name_plural = ( "Calls" )
		ordering = ( "-call_time", )


