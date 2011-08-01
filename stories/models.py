from django.db import models
#geodjango support
from django.contrib.gis.db import models

# Create your models here.

class Story( models.Model ):
	id = models.IntegerField( unique = True,blank = False,primary_key = True  )
	short_url = models.URLField( blank = True )
	long_url = models.URLField( blank = True, null = True)
	date_published = models.DateTimeField( auto_now = False, auto_now_add = False, blank = False )
	date_removed = models.DateTimeField( auto_now = False, auto_now_add = False, blank = True, null = True )
	active = models.BooleanField( default = True, blank = False )
	category = models.CharField( max_length = 255, blank = True, null = True )
	headline = models.CharField( max_length = 255, blank = True)
	summary = models.TextField( blank = True )
	byline = models.CharField( max_length = 255, blank = True, null = True )
	address = models.TextField( blank = True, null = True)
	geom = models.PointField( srid = 4326, blank = True, null = True )
	images = models.TextField( blank = True, null = True )
	
	featured = models.BooleanField( default=False, blank=False )
	
	objects = models.GeoManager()
	
	
	def __unicode__( self ):
		return self.headline
	
	class Meta:
		db_table = "story"
		verbose_name = "Story"
		verbose_name_plural = "Stories"
		ordering = ( "-id", )

class Pageview( models.Model ):
	story = models.ForeignKey( Story, null = True, blank = True )
	time_init = models.DateTimeField( auto_now_add = True, blank = False )
	
	objects = models.Manager()
	
	class Meta:
		db_table = "pageview"
		verbose_name = "Page View"
		verbose_name_plural = "Page Views"
		ordering = ("-story","-time_init",)
	
class Keyword( models.Model ):
	story = models.ForeignKey( Story )
	keyword = models.CharField( max_length = 255, blank = False )
	
	objects = models.Manager()
	
	class Meta:
		db_table = "keyword"
		verbose_name = "Keyword"
		verbose_name_plural = "Keywords"
		ordering = ("-story","keyword",)
		
