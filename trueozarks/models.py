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
#seeing which path to use.
if socket.gethostname() == "2155529.pubip.peer1.net":
    sys.path.append('/opt/django/data.news-leader.com')
    g = geocoders.Google('ABQIAAAA2JAd-KesRNeDJwroL49_CxTC4wGmoCeUv8j3n4Pev0Dsu3hwqxS_gg6u4S_FFZd8gO-pLGIZ4Ui7VQ')
else:
    sys.path.append('/Users/tlane2/Code/data/trunk')
    g = geocoders.Google('ABQIAAAA2JAd-KesRNeDJwroL49_CxRMPgAshc9HvuksOF-1hbNeUnHu2RR3TUaykJvxoc7edBwXZYs044EM3w')

PullQuoteChoices = (
	('LEFT','Left'),
	('RIGHT','Right'),
	('CENTER','Center'),
)

InfoBoxChoices = (
	('LEFT','Left'),
	('RIGHT','Right'),
)

class Layout(models.Model):
	name = models.CharField(max_length=255)
	active = models.BooleanField(default=True)
	template = models.FileField(default=None, blank=True, null=True, upload_to="trueozarks/layouts/")
	active = models.BooleanField(default=True)

	objects = models.Manager()

	def __unicode__(self):
		return u"%s" % self.name

class Tag( models.Model):
	name= models.CharField(max_length=255)
	active = models.BooleanField(default=True)
	time_init = models.DateTimeField( "Date Added", auto_now =  False, auto_now_add = True )
	last_updated = models.DateTimeField("Last Updated", auto_now=True,
            auto_now_add=False, null=True)

	address = models.CharField(max_length=255)
	geocoder = models.CharField(max_length=25, null=True,blank=True)
	geom = models.PointField(srid=4326, blank=True,null=True)
	
	objects = models.GeoManager()

	def save(self, *args, **kwargs ):
		#overriding the save so i can geocode the address
		if self.address is not None:
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
				super(Tag,self).save(*args,**kwargs)

	def __unicode__(self):
		return u"%s" % self.name


class Profile(models.Model):
	name = models.CharField(max_length=255,blank=False)
	headline = models.CharField(blank=False,max_length=255)
	main_photo = models.ImageField(default=None, blank=True, null=True, upload_to="trueozarks/images/")
	summary = models.TextField(null=True)
	user = models.ForeignKey(User,editable=False)
	time_init = models.DateTimeField( "Date Added", auto_now =  False, auto_now_add = True )
	last_updated = models.DateTimeField("Last Updated", auto_now=True,
            auto_now_add=False, null=True)
	tags = models.ManyToManyField(Tag)
	address = models.CharField(max_length=255)
	geocoder = models.CharField(max_length=25, null=True,blank=True)
	geom = models.PointField(srid=4326, blank=True,null=True)
	layout = models.ForeignKey(Layout)
	active = models.BooleanField(default=True)
	objects = models.GeoManager()

	def save(self, *args, **kwargs ):
		#overriding the save so i can geocode the address
		if self.address is not None:
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
				super(Profile,self).save(*args,**kwargs)

	
	def __unicode__( self ):
		return u"%s" % self.name


class Story(models.Model):
	profile = models.OneToOneField(Profile)
	text = models.TextField()
	headline = models.CharField(max_length=255)
	subheadline = models.CharField(max_length=255)
	byline = models.CharField(max_length=255)
	#photo = models.ImageField()
	user = models.ForeignKey(User,editable=False)
	time_init = models.DateTimeField( "Date Added", auto_now =  False, auto_now_add = True )
	last_updated = models.DateTimeField("Last Updated", auto_now=True,
            auto_now_add=False, null=True)
	tags = models.ManyToManyField(Tag)
	address = models.CharField(max_length=255)
	geocoder = models.CharField(max_length=25, null=True,blank=True)
	geom = models.PointField(srid=4326, blank=True,null=True)

	objects = models.GeoManager()
	
	def save(self, *args, **kwargs ):
		#overriding the save so i can geocode the address
		if self.address is not None:
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
				super(Story,self).save(*args,**kwargs)


	def __unicode__( self ):
		return u"%s" %( self.profile + " - " + self.headline) 

class PullQuote(models.Model):
	story = models.ForeignKey(Story)
	text = models.CharField(max_length=255)
	style = models.CharField(choices=PullQuoteChoices,max_length=100)
	position = models.IntegerField()
	active = models.BooleanField(default=True)

	objects = models.Manager()

	def __unicode__(self):
		return u"%s" % self.text

class InfoBox(models.Model):
	story = models.ForeignKey(Story)
	headline = models.CharField(max_length=255)
	text = models.TextField()
	style = models.CharField(choices=InfoBoxChoices,max_length=100)
	position = models.IntegerField()
	active = models.BooleanField(default=True)

	objects = models.Manager()

	def __unicode__(self):
		return u"%s" % self.headline




# class Gallery( models.Model):
# 	profile = models.ForeignKey(Profile)
# 	name = models.CharField(max_length=255)
# 	user = models.ForeignKey(User,editable=False)
# 	time_init = models.DateTimeField( "Date Added", auto_now =  False, auto_now_add = True )
# 	last_updated = models.DateTimeField("Last Updated", auto_now=True,
#             auto_now_add=False, null=True)
# 	tags = models.ManyToManyField(Tag)
# 	address = models.CharField()
# 	geocoder = models.CharField(max_length=25, null=True,blank=True)
# 	geom = models.PointField(srid=4326, blank=True,null=True)
	
# 	objects = models.GeoManager()

# 	def save(self, *args, **kwargs ):
# 		#overriding the save so i can geocode the address
# 		if self.address is not None:
# 			try:
# 				#try to geocode
# 				place, ( lat, lng ) = g.geocode( self.address, exactly_one=False )[0]
# 				#if lat and lgn aren't blank
# 				if ( lng is not None or lng != "" ) and ( lat is not None or lng != "" ):
# 					#set geom for our address
# 					self.geom = fromstr( 'POINT(' + str(lng) + " " + str(lat) +')', srid = 4326 )
# 					self.geocoder = "Google"
# 			except:
# 				#if errors are thrown then we throw an validation error
# 				raise ValidationError
# 			else:
# 				#else we save our geom
# 				super(Model,self).save(*args,**kwargs)
	
# 	def __unicode__(self):
# 		return u"%s" % (self.name)

class Photo( models.Model):
	profile = models.ForeignKey(Profile)
	picture = models.ImageField(default=None, blank=True, null=True, upload_to="trueozarks/images/")
	cutline = models.TextField()
	credit = models.CharField(max_length=255)
	order = models.IntegerField()
	position = models.IntegerField()
	style = models.CharField(max_length=100)
	tags = models.ManyToManyField(Tag)
	address = models.CharField(max_length=255)
	geocoder = models.CharField(max_length=25, null=True,blank=True)
	geom = models.PointField(srid=4326, blank=True,null=True)
	

	time_init = models.DateTimeField( "Date Added", auto_now =  False, auto_now_add = True )
	last_updated = models.DateTimeField("Last Updated", auto_now=True,
            auto_now_add=False, null=True)

	objects = models.GeoManager()

	def save(self, *args, **kwargs ):
		#overriding the save so i can geocode the address
		if self.address is not None:
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
				super(Photo,self).save(*args,**kwargs)
	
	def __unicode__(self):
		return u"%s" % (self.picture)



