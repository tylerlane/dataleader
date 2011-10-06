from django.db import models
#geodjango support
from django.contrib.gis.db import models

# Create your models here.
class Schools(models.Model):
	ctydist = models.CharField(max_length=12)
	schnum = models.CharField(max_length=254)
	schid = models.CharField(max_length=15)
	facility = models.CharField(max_length=100)
	address = models.CharField(max_length=60)
	address2 = models.CharField(max_length=50)
	city = models.CharField(max_length=35)
	state = models.CharField(max_length=2)
	zip_code = models.CharField(max_length=15)
	county = models.CharField(max_length=15)
	phone = models.CharField(max_length=25)
	fax = models.CharField(max_length=25)
	bgrade = models.CharField(max_length=4)
	egrade = models.CharField(max_length=4)
	principal = models.CharField(max_length=254)
	printitle = models.CharField(max_length=25)
	teachers = models.FloatField()
	enrollment = models.IntegerField()
	schemail = models.CharField(max_length=35)
	latitude = models.FloatField()
	longitude = models.FloatField()
	loc_code = models.CharField(max_length=6)
	geom = models.PointField(srid=4326)
	
	objects = models.GeoManager()
	
	class Meta:
		db_table = "schools"
		verbose_name = "Schools"
		verbose_name_plural = "Schools"
		ordering = ( "facility", )
		
		
class SchoolDistricts(models.Model):
	area = models.FloatField()
	perimeter = models.FloatField()
	unsd_field = models.FloatField()
	unsd_id = models.FloatField()
	statefp = models.CharField(max_length=2)
	statens = models.CharField(max_length=8)
	unsdlea = models.CharField(max_length=5)
	unsdidfp = models.CharField(max_length=7)
	name = models.CharField(max_length=100)
	lsad = models.CharField(max_length=2)
	lograde = models.CharField(max_length=2)
	higrade = models.CharField(max_length=2)
	mtfcc = models.CharField(max_length=5)
	sdtyp = models.CharField(max_length=1)
	funcstat = models.CharField(max_length=1)
	aland = models.FloatField()
	awater = models.FloatField()
	intptlat = models.CharField(max_length=11)
	intptlon = models.CharField(max_length=12)
	geom = models.PolygonField(srid=4326)
	objects = models.GeoManager()
	
	
	
	class Meta:
		db_table = "school_districts"
		verbose_name = "School Districts"
		verbose_name_plural = "School Districts"
		ordering = ( "name", );



class Counties(models.Model):
	countyname = models.CharField(max_length=35)
	countyfips = models.CharField(max_length=3)
	countygnis = models.CharField(max_length=6)
	name_ucase = models.CharField(max_length=35)
	pop_1990 = models.IntegerField()
	pop_2000 = models.IntegerField()
	acres = models.FloatField()
	sq_miles = models.FloatField()
	cnty_seat = models.CharField(max_length=35)
	co_class = models.IntegerField()
	geom = models.MultiPolygonField(srid=4326)
	objects = models.GeoManager()

	class Meta:
		db_table = "counties"
		verbose_name = "Counties"
		verbose_name_plural = "Counties"
		ordering = ( "countyname", );
		
		
class ZipCodes(models.Model):
	zcta5ce = models.CharField(max_length=5)
	classfp = models.CharField(max_length=2)
	mtfcc = models.CharField(max_length=5)
	funcstat = models.CharField(max_length=1)
	geom = models.MultiPolygonField(srid=4326)
	objects = models.GeoManager()
	
	
	class Meta:
		db_table = "zip_codes"
		verbose_name = "Zip Codes"
		verbose_name_plural = "Zip Codes"
		ordering = ( "zcta5ce", );


class ReversePubZone( models.Model ):
	name = models.CharField( max_length=100 )
	active = models.BooleanField( default=True )
	geom = models.MultiPolygonField( srid=4326 )
	objects = models.GeoManager()
	
	
	def __unicode__( self ):
		return self.name
		
	class Meta:
		db_table = "reversepub_zone"
		verbose_name = "Reverse Pub Zone"
		verbose_name_plural = "Reverse Pub Zone"
		