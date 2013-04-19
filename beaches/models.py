from django.db import models,IntegrityError
#geodjango support
from django.contrib.gis.db import models

# Create your models here.
#"ID":"01","latitude":"40.095049","longitude":"-93.662526","openclosed":"N","parkname":"Crowder State Park Public Beach","results1":"N/S","results2":"N/S","sampletaken":"5/3/2010"},

class Beach( models.Model ):
	beach_id = models.IntegerField(null=True,blank=True)
	geom = models.PointField(srid=4326,null=True,blank=True)
	openclosed = models.CharField( max_length=5,null=True,blank=True )
	parkname = models.CharField( max_length=255,null=True,blank=True )
	results1 = models.CharField( max_length=20,null=True,blank=True )
	results2 = models.CharField( max_length=20,null=True,blank=True )
	sampletaken = models.DateField( auto_now_add=False, auto_now=False,null=True,blank=True )
	
	
	objects = models.GeoManager()
		
	def __unicode__( self ):
		return self.parkname
		
	class Meta:
		verbose_name = "Beach"
		verbose_name_plural = "Beaches"