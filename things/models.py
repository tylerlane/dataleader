#geodjango support
from django.contrib.gis.db import models
import datetime
from django.forms import ValidationError
from django.contrib.auth.models import User
import re
from django.contrib.gis.geos import fromstr
from geopy import geocoders
import socket
import sys
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/opt/django/data.news-leader.com/dataleader/static/')
templatefs = FileSystemStorage(location='/opt/django/data.news-leader.com/dataleader/templates/trueozarks/')
#seeing which path to use.
if socket.gethostname() == "2155529.pubip.peer1.net":
    sys.path.append('/opt/django/data.news-leader.com')
    g = geocoders.Google('ABQIAAAA2JAd-KesRNeDJwroL49_CxTC4wGmoCeUv8j3n4Pev0Dsu3hwqxS_gg6u4S_FFZd8gO-pLGIZ4Ui7VQ')
else:
    sys.path.append('/Users/tlane2/Code/data/trunk')
    g = geocoders.Google('ABQIAAAA2JAd-KesRNeDJwroL49_CxRMPgAshc9HvuksOF-1hbNeUnHu2RR3TUaykJvxoc7edBwXZYs044EM3w')


class Genre(models.Model):
	name = models.CharField(max_length=255)
	active = models.BooleanField(default=True)
	photo = models.ImageField(default=None,blank=True,null=True,upload_to="things/genre")
	parent = models.ForeignKey("Genre",blank=True,null=True,default=None)
	description = models.TextField(default=None,blank=True,null=True)
	app_layout = models.CharField(max_length=40)
	
	objects = models.Manager()
	
	def __unicode__(self):
		return self.name

class Age(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	age_min = models.IntegerField()
	age_max = models.IntegerField()
	active = models.BooleanField()
	
	objects = models.Manager()
	
	def __unicode__(self):
		return self.name

class Venue(models.Model):
	name = models.CharField(max_length=255)
	address = models.TextField()
	phone = models.CharField(max_length=25)
	website = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	geom = models.PointField(srid=4326,blank=True,null=True)
	geom_area = models.MultiPolygonField(srid=4326,blank=True,null=True)

	place_to_go = models.BooleanField(default=False)

	#contact info
	contact_name = models.CharField(max_length=255)
	contact_address = models.CharField(max_length=255)
	contact_phone = models.CharField(max_length=25)
	contact_email = models.CharField(max_length=200)
	contact_website = models.CharField(max_length=255)

	active = models.BooleanField(default=True)
	objects = models.GeoManager()

	def __unicode__(self):
		return self.name

	def save( self, *args, **kwargs ):
		#overriding the save so i can geocode the address
		if len( self.address ) > 0:
			try:
				#try to geocode
				place, ( lat, lng ) = g.geocode( self.address, exactly_one=False )[0]
				#if lat and lgn aren't blank
				if ( lng is not None or lng != "" ) and ( lat is not None or lng != "" ):
					#set geom for our address
					self.geom = fromstr( 'POINT(' + str(lng) + " " + str(lat) +')', srid = 4326 )
					self.geocoder = "Google"
			except:
				#if errors are thrown then we throw an validation error
				raise ValidationError
			else:
				#else we save our geom
				super(Venue,self).save(*args,**kwargs)
		else:
			#else we save our geom
			super(Venue,self).save(*args,**kwargs)



class Event(models.Model):
	name = models.CharField(max_length=255)
	short_description = models.CharField(max_length=155)
	description = models.TextField()
	parking = models.BooleanField()
	venue = models.ForeignKey(Venue)
	cost = models.FloatField(blank=True,null=True)
	cost_description = models.CharField(max_length=255)
	excitement = models.FloatField()
	main_photo = models.ImageField(upload_to="things/photos")
	age = models.ManyToManyField(Age)
	genre = models.ManyToManyField(Genre)
	#this should work as a foreign key field but i might have to change this.
	#time = models.ManyToManyField(Time)

	#active boolean
	active = models.BooleanField()

	#contact info
	contact_name = models.CharField(max_length=255)
	contact_address = models.CharField(max_length=255)
	contact_phone = models.CharField(max_length=25)
	contact_email = models.CharField(max_length=200)
	contact_website = models.CharField(max_length=255)

	objects = models.Manager()

	def __unicode__(self):
		return self.name

class Time(models.Model):
	event = models.ForeignKey(Event)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	active = models.BooleanField(default=True)

	objects = models.Manager()

	def __unicode__(self):

		return u'From: %s  To: %s' % (self.start_time,self.end_time)


class Photo(models.Model):
	event = models.ForeignKey(Event)
	picture = models.ImageField(upload_to="things/photos")
	description = models.TextField()
	active = models.BooleanField(default=True)

	objects = models.Manager()