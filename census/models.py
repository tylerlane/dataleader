from django.db import models,IntegrityError
from django.contrib.localflavor.us.us_states import STATE_CHOICES
#geodjango support
from django.contrib.gis.db import models
import datetime


"""STATE_CHOICES = (
	('AR','Arkansas'),
	('IA','Iowa'),
	('IL','Illinois'),
	('KS','Kansas'),
	('KY','Kentucky'),
	('MO','Missouri'),
	('NE','Nebraska'),
	('OK','Oklahoma'),
	('TN','Tennessee'),
	
)"""

#model	
class CountyData( models.Model ):
	#general stuff
	county_name = models.CharField( max_length="200" )
	state = models.CharField( max_length="2", choices=STATE_CHOICES )
	#pop fields
	pop2000 = models.IntegerField( help_text="2000 Population", blank = True, null = True )
	pop2010 = models.IntegerField( help_text="2010 Population", blank = True, null = True )
	pop2000SqMile = models.FloatField( help_text="2000 Population/Square Mile",blank=True, null=True )
	pop2010SqMile = models.FloatField( help_text="2010 Population/Square Mile",blank=True, null=True )
	pctwhite2000 = models.FloatField( help_text="% of Population White - 2000", blank=True, null=True )
	popwhite2000 = models.IntegerField( help_text="2000 Population - White", blank=True, null= True )
	pctwhite2010 = models.FloatField( help_text="% of Population White - 2010", blank=True, null=True  )
	popwhite2010 = models.IntegerField( help_text="2010 Population - White", blank=True, null= True )
	pctblack2000 = models.FloatField( help_text="% of Population Black - 2000", blank=True, null=True  )
	popblack2000 = models.IntegerField( help_text="2000 Population - Black", blank=True, null= True )
	pctblack2010 = models.FloatField( help_text="% of Population Black - 2010", blank=True, null=True  )
	popblack2010 = models.IntegerField( help_text="2010 Population - Black", blank=True, null= True )
	pctamind2000 = models.FloatField( help_text="% of Population American Indian - 2000", blank=True, null=True  )
	popamind2000 = models.IntegerField( help_text="2000 Population - American Indian", blank=True, null= True )
	pctamind2010 = models.FloatField( help_text="% of Population American Indian - 2010", blank=True, null=True  )
	popamind2010 = models.IntegerField( help_text="2010 Population - American Indian", blank=True, null= True )
	pctasian2000 = models.FloatField( help_text="% of Population Asian - 2000", blank=True, null=True  )
	popasian2000 = models.IntegerField( help_text="2000 Population - Asian", blank=True, null= True )
	pctasian2010 = models.FloatField( help_text="% of Population Asian - 2010", blank=True, null=True  )
	popasian2010 = models.IntegerField( help_text="2010 Population - Asian", blank=True, null= True )
	pctnathaw2000 = models.FloatField( help_text="% of Population Native Hawaiian/Other Pacific Islander - 2000", blank=True, null=True  )
	popnathaw2000 = models.IntegerField( help_text="2000 Population - Native Hawaiian/Other Pacific Islander", blank=True, null= True )
	pctnathaw2010 = models.FloatField( help_text="% of Population Native Hawaiian/Other Pacific Islander - 2010", blank=True, null=True  )
	popnathaw2010 = models.IntegerField( help_text="2010 Population - Native Hawaiian/Other Pacific Islander", blank=True, null= True )
	pctother2000 = models.FloatField( help_text="% of Population Some Other Race - 2000", blank=True, null=True  )
	popother2000 = models.IntegerField( help_text="2000 Population - Some Other Race", blank=True, null= True )
	pctother2010 = models.FloatField( help_text="% of Population Some Other Race - 2010", blank=True, null=True  )
	popother2010 = models.IntegerField( help_text="2010 Population - Some Other Race", blank=True, null= True )
	pct2ormore2000 = models.FloatField( help_text="% of Population Two or More Races - 2000", blank=True, null=True  )
	pop2ormore2000 = models.IntegerField( help_text="2000 Population - Two or more Races", blank=True, null= True )
	pct2ormore2010 = models.FloatField( help_text="% of Population Two or More Races - 2010", blank=True, null=True  )
	pop2ormore2010 = models.IntegerField( help_text="2010 Population - Two or More Races", blank=True, null= True )
	pcthisp2000 = models.FloatField( help_text="% of Population Hispanic - 2000", blank=True, null=True  )
	pophisp2000 = models.IntegerField( help_text="2000 Population - Hispanic", blank=True, null= True )
	pcthisp2010 = models.FloatField( help_text="% of Population Hispanic - 2010", blank=True, null=True  )
	pophisp2010 = models.IntegerField( help_text="2010 Population - Hispanic", blank=True, null= True )
	pctnonhisp2000 = models.FloatField( help_text="% of Population Non-Hispanic - 2000", blank=True, null=True  )
	popnonhisp2000 = models.IntegerField( help_text="2000 Population - Non-Hispanic", blank=True, null= True )
	pctnonhisp2010 = models.FloatField( help_text="% of Population Non-Hispanic - 2010", blank=True, null=True  )
	popnonhisp2010 = models.IntegerField( help_text="2010 Population - Non-Hispanic", blank=True, null= True )
	pctwhitenonhisp2000 = models.FloatField( help_text="% of Population White Non-Hispanic - 2000", blank=True, null=True  )
	popwhitenonhisp2000 = models.IntegerField( help_text="2010 Population - White Non-Hispanic", blank=True, null= True )
	pctwhitenonhisp2010 = models.FloatField( help_text="% of Population White Non-Hispanic - 2010", blank=True, null=True  )
	popwhitenonhisp2010 = models.IntegerField( help_text="2010 Population - Asian", blank=True, null= True )
	dividx2000 = models.FloatField( help_text="USA Today Diversity Index - 2000", blank=True, null=True  )
	dividx2010 = models.FloatField( help_text="USA Today Diversity Index - 2010", blank=True, null=True  )
	
	#area
	total_sqmiles = models.FloatField( help_text = "Square Miles", blank=True, null=True  )
	water_sqmiles = models.FloatField( help_text = "Water in Square Miles", blank=True, null=True  )
	land_sqmiles = models.FloatField( help_text = "Land in Square Miles", blank=True, null=True  )
	
	
	objects = models.GeoManager()
	
	def __unicode__( self ):
		return "%s, %s" % ( self.county_name, self.state )
	
	def pop_change_percentage( self ):
		change = float( self.pop2010 ) - float( self.pop2000)
		percent = change / float( self.pop2000 )
		
		return percent * 100
	
	class Meta:
		verbose_name_plural = "County Data"
	
class StateData( models.Model ):
	state = models.CharField( max_length="2", choices=STATE_CHOICES )
	#pop fields
	pop2000 = models.IntegerField( help_text="2000 Population", blank = True, null = True )
	pop2010 = models.IntegerField( help_text="2010 Population", blank = True, null = True )
	pop2000SqMile = models.FloatField( help_text="2000 Population/Square Mile",blank=True, null=True )
	pop2010SqMile = models.FloatField( help_text="2010 Population/Square Mile",blank=True, null=True )
	pctwhite2000 = models.FloatField( help_text="% of Population White - 2000", blank=True, null=True )
	popwhite2000 = models.IntegerField( help_text="2000 Population - White", blank=True, null= True )
	pctwhite2010 = models.FloatField( help_text="% of Population White - 2010", blank=True, null=True  )
	popwhite2010 = models.IntegerField( help_text="2010 Population - White", blank=True, null= True )
	pctblack2000 = models.FloatField( help_text="% of Population Black - 2000", blank=True, null=True  )
	popblack2000 = models.IntegerField( help_text="2000 Population - Black", blank=True, null= True )
	pctblack2010 = models.FloatField( help_text="% of Population Black - 2010", blank=True, null=True  )
	popblack2010 = models.IntegerField( help_text="2010 Population - Black", blank=True, null= True )
	pctamind2000 = models.FloatField( help_text="% of Population American Indian - 2000", blank=True, null=True  )
	popamind2000 = models.IntegerField( help_text="2000 Population - American Indian", blank=True, null= True )
	pctamind2010 = models.FloatField( help_text="% of Population American Indian - 2010", blank=True, null=True  )
	popamind2010 = models.IntegerField( help_text="2010 Population - American Indian", blank=True, null= True )
	pctasian2000 = models.FloatField( help_text="% of Population Asian - 2000", blank=True, null=True  )
	popasian2000 = models.IntegerField( help_text="2000 Population - Asian", blank=True, null= True )
	pctasian2010 = models.FloatField( help_text="% of Population Asian - 2010", blank=True, null=True  )
	popasian2010 = models.IntegerField( help_text="2010 Population - Asian", blank=True, null= True )
	pctnathaw2000 = models.FloatField( help_text="% of Population Native Hawaiian/Other Pacific Islander - 2000", blank=True, null=True  )
	popnathaw2000 = models.IntegerField( help_text="2000 Population - Native Hawaiian/Other Pacific Islander", blank=True, null= True )
	pctnathaw2010 = models.FloatField( help_text="% of Population Native Hawaiian/Other Pacific Islander - 2010", blank=True, null=True  )
	popnathaw2010 = models.IntegerField( help_text="2010 Population - Native Hawaiian/Other Pacific Islander", blank=True, null= True )
	pctother2000 = models.FloatField( help_text="% of Population Some Other Race - 2000", blank=True, null=True  )
	popother2000 = models.IntegerField( help_text="2000 Population - Some Other Race", blank=True, null= True )
	pctother2010 = models.FloatField( help_text="% of Population Some Other Race - 2010", blank=True, null=True  )
	popother2010 = models.IntegerField( help_text="2010 Population - Some Other Race", blank=True, null= True )
	pct2ormore2000 = models.FloatField( help_text="% of Population Two or More Races - 2000", blank=True, null=True  )
	pop2ormore2000 = models.IntegerField( help_text="2000 Population - Two or more Races", blank=True, null= True )
	pct2ormore2010 = models.FloatField( help_text="% of Population Two or More Races - 2010", blank=True, null=True  )
	pop2ormore2010 = models.IntegerField( help_text="2010 Population - Two or More Races", blank=True, null= True )
	pcthisp2000 = models.FloatField( help_text="% of Population Hispanic - 2000", blank=True, null=True  )
	pophisp2000 = models.IntegerField( help_text="2000 Population - Hispanic", blank=True, null= True )
	pcthisp2010 = models.FloatField( help_text="% of Population Hispanic - 2010", blank=True, null=True  )
	pophisp2010 = models.IntegerField( help_text="2010 Population - Hispanic", blank=True, null= True )
	pctnonhisp2000 = models.FloatField( help_text="% of Population Non-Hispanic - 2000", blank=True, null=True  )
	popnonhisp2000 = models.IntegerField( help_text="2000 Population - Non-Hispanic", blank=True, null= True )
	pctnonhisp2010 = models.FloatField( help_text="% of Population Non-Hispanic - 2010", blank=True, null=True  )
	popnonhisp2010 = models.IntegerField( help_text="2010 Population - Non-Hispanic", blank=True, null= True )
	pctwhitenonhisp2000 = models.FloatField( help_text="% of Population White Non-Hispanic - 2000", blank=True, null=True  )
	popwhitenonhisp2000 = models.IntegerField( help_text="2010 Population - White Non-Hispanic", blank=True, null= True )
	pctwhitenonhisp2010 = models.FloatField( help_text="% of Population White Non-Hispanic - 2010", blank=True, null=True  )
	popwhitenonhisp2010 = models.IntegerField( help_text="2010 Population - Asian", blank=True, null= True )
	dividx2000 = models.FloatField( help_text="USA Today Diversity Index - 2000", blank=True, null=True  )
	dividx2010 = models.FloatField( help_text="USA Today Diversity Index - 2010", blank=True, null=True  )
	
	#area
	total_sqmiles = models.FloatField( help_text = "Square Miles", blank=True, null=True  )
	water_sqmiles = models.FloatField( help_text = "Water in Square Miles", blank=True, null=True  )
	land_sqmiles = models.FloatField( help_text = "Land in Square Miles", blank=True, null=True  )
		
	objects = models.GeoManager()
	
	def __unicode__( self ):
		return self.state
		
	class Meta:
		verbose_name_plural = "State Data"		
	
class TractData( models.Model ):
	tract_name = models.CharField( max_length="200" )
	state = models.CharField( max_length="2", choices=STATE_CHOICES )
	#pop fields
	pop2000 = models.IntegerField( help_text="2000 Population", blank = True, null = True )
	pop2010 = models.IntegerField( help_text="2010 Population", blank = True, null = True )
	pctwhite2000 = models.FloatField( help_text="% of Population White - 2000", blank=True, null=True )
	popwhite2000 = models.IntegerField( help_text="2000 Population - White", blank=True, null= True )
	pctwhite2010 = models.FloatField( help_text="% of Population White - 2010", blank=True, null=True  )
	popwhite2010 = models.IntegerField( help_text="2010 Population - White", blank=True, null= True )
	pctblack2000 = models.FloatField( help_text="% of Population Black - 2000", blank=True, null=True  )
	popblack2000 = models.IntegerField( help_text="2000 Population - Black", blank=True, null= True )
	pctblack2010 = models.FloatField( help_text="% of Population Black - 2010", blank=True, null=True  )
	popblack2010 = models.IntegerField( help_text="2010 Population - Black", blank=True, null= True )
	pctamind2000 = models.FloatField( help_text="% of Population American Indian - 2000", blank=True, null=True  )
	popamind2000 = models.IntegerField( help_text="2000 Population - American Indian", blank=True, null= True )
	pctamind2010 = models.FloatField( help_text="% of Population American Indian - 2010", blank=True, null=True  )
	popamind2010 = models.IntegerField( help_text="2010 Population - American Indian", blank=True, null= True )
	pctasian2000 = models.FloatField( help_text="% of Population Asian - 2000", blank=True, null=True  )
	popasian2000 = models.IntegerField( help_text="2000 Population - Asian", blank=True, null= True )
	pctasian2010 = models.FloatField( help_text="% of Population Asian - 2010", blank=True, null=True  )
	popasian2010 = models.IntegerField( help_text="2010 Population - Asian", blank=True, null= True )
	pctnathaw2000 = models.FloatField( help_text="% of Population Native Hawaiian/Other Pacific Islander - 2000", blank=True, null=True  )
	popnathaw2000 = models.IntegerField( help_text="2000 Population - Native Hawaiian/Other Pacific Islander", blank=True, null= True )
	pctnathaw2010 = models.FloatField( help_text="% of Population Native Hawaiian/Other Pacific Islander - 2010", blank=True, null=True  )
	popnathaw2010 = models.IntegerField( help_text="2010 Population - Native Hawaiian/Other Pacific Islander", blank=True, null= True )
	pctother2000 = models.FloatField( help_text="% of Population Some Other Race - 2000", blank=True, null=True  )
	popother2000 = models.IntegerField( help_text="2000 Population - Some Other Race", blank=True, null= True )
	pctother2010 = models.FloatField( help_text="% of Population Some Other Race - 2010", blank=True, null=True  )
	popother2010 = models.IntegerField( help_text="2010 Population - Some Other Race", blank=True, null= True )
	pct2ormore2000 = models.FloatField( help_text="% of Population Two or More Races - 2000", blank=True, null=True  )
	pop2ormore2000 = models.IntegerField( help_text="2000 Population - Two or more Races", blank=True, null= True )
	pct2ormore2010 = models.FloatField( help_text="% of Population Two or More Races - 2010", blank=True, null=True  )
	pop2ormore2010 = models.IntegerField( help_text="2010 Population - Two or More Races", blank=True, null= True )
	pcthisp2000 = models.FloatField( help_text="% of Population Hispanic - 2000", blank=True, null=True  )
	pophisp2000 = models.IntegerField( help_text="2000 Population - Hispanic", blank=True, null= True )
	pcthisp2010 = models.FloatField( help_text="% of Population Hispanic - 2010", blank=True, null=True  )
	pophisp2010 = models.IntegerField( help_text="2010 Population - Hispanic", blank=True, null= True )
	pctnonhisp2000 = models.FloatField( help_text="% of Population Non-Hispanic - 2000", blank=True, null=True  )
	popnonhisp2000 = models.IntegerField( help_text="2000 Population - Non-Hispanic", blank=True, null= True )
	pctnonhisp2010 = models.FloatField( help_text="% of Population Non-Hispanic - 2010", blank=True, null=True  )
	popnonhisp2010 = models.IntegerField( help_text="2010 Population - Non-Hispanic", blank=True, null= True )
	pctwhitenonhisp2000 = models.FloatField( help_text="% of Population White Non-Hispanic - 2000", blank=True, null=True  )
	popwhitenonhisp2000 = models.IntegerField( help_text="2010 Population - White Non-Hispanic", blank=True, null= True )
	pctwhitenonhisp2010 = models.FloatField( help_text="% of Population White Non-Hispanic - 2010", blank=True, null=True  )
	popwhitenonhisp2010 = models.IntegerField( help_text="2010 Population - Asian", blank=True, null= True )
	dividx2000 = models.FloatField( help_text="USA Today Diversity Index - 2000", blank=True, null=True  )
	dividx2010 = models.FloatField( help_text="USA Today Diversity Index - 2010", blank=True, null=True  )
	
	#area
	total_sqmiles = models.FloatField( help_text = "Square Miles", blank=True, null=True  )
	water_sqmiles = models.FloatField( help_text = "Water in Square Miles", blank=True, null=True  )
	land_sqmiles = models.FloatField( help_text = "Land in Square Miles", blank=True, null=True  )
	
	objects = models.GeoManager()
	
	def __unicode__( self ):
		return "%s - %s" % ( self.tract_name, self.state )
		
	class Meta:
		verbose_name_plural = "Tract Data"		


class CityData( models.Model ):
	#general stuff
	city_name = models.CharField( max_length="200" )
	state = models.CharField( max_length="2", choices=STATE_CHOICES )
	#pop fields
	pop2000 = models.IntegerField( help_text="2000 Population", blank = True, null = True )
	pop2010 = models.IntegerField( help_text="2010 Population", blank = True, null = True )
	pop2000SqMile = models.FloatField( help_text="2000 Population/Square Mile",blank=True, null=True )
	pop2010SqMile = models.FloatField( help_text="2010 Population/Square Mile",blank=True, null=True )
	pctwhite2000 = models.FloatField( help_text="% of Population White - 2000", blank=True, null=True )
	popwhite2000 = models.IntegerField( help_text="2000 Population - White", blank=True, null= True )
	pctwhite2010 = models.FloatField( help_text="% of Population White - 2010", blank=True, null=True  )
	popwhite2010 = models.IntegerField( help_text="2010 Population - White", blank=True, null= True )
	pctblack2000 = models.FloatField( help_text="% of Population Black - 2000", blank=True, null=True  )
	popblack2000 = models.IntegerField( help_text="2000 Population - Black", blank=True, null= True )
	pctblack2010 = models.FloatField( help_text="% of Population Black - 2010", blank=True, null=True  )
	popblack2010 = models.IntegerField( help_text="2010 Population - Black", blank=True, null= True )
	pctamind2000 = models.FloatField( help_text="% of Population American Indian - 2000", blank=True, null=True  )
	popamind2000 = models.IntegerField( help_text="2000 Population - American Indian", blank=True, null= True )
	pctamind2010 = models.FloatField( help_text="% of Population American Indian - 2010", blank=True, null=True  )
	popamind2010 = models.IntegerField( help_text="2010 Population - American Indian", blank=True, null= True )
	pctasian2000 = models.FloatField( help_text="% of Population Asian - 2000", blank=True, null=True  )
	popasian2000 = models.IntegerField( help_text="2000 Population - Asian", blank=True, null= True )
	pctasian2010 = models.FloatField( help_text="% of Population Asian - 2010", blank=True, null=True  )
	popasian2010 = models.IntegerField( help_text="2010 Population - Asian", blank=True, null= True )
	pctnathaw2000 = models.FloatField( help_text="% of Population Native Hawaiian/Other Pacific Islander - 2000", blank=True, null=True  )
	popnathaw2000 = models.IntegerField( help_text="2000 Population - Native Hawaiian/Other Pacific Islander", blank=True, null= True )
	pctnathaw2010 = models.FloatField( help_text="% of Population Native Hawaiian/Other Pacific Islander - 2010", blank=True, null=True  )
	popnathaw2010 = models.IntegerField( help_text="2010 Population - Native Hawaiian/Other Pacific Islander", blank=True, null= True )
	pctother2000 = models.FloatField( help_text="% of Population Some Other Race - 2000", blank=True, null=True  )
	popother2000 = models.IntegerField( help_text="2000 Population - Some Other Race", blank=True, null= True )
	pctother2010 = models.FloatField( help_text="% of Population Some Other Race - 2010", blank=True, null=True  )
	popother2010 = models.IntegerField( help_text="2010 Population - Some Other Race", blank=True, null= True )
	pct2ormore2000 = models.FloatField( help_text="% of Population Two or More Races - 2000", blank=True, null=True  )
	pop2ormore2000 = models.IntegerField( help_text="2000 Population - Two or more Races", blank=True, null= True )
	pct2ormore2010 = models.FloatField( help_text="% of Population Two or More Races - 2010", blank=True, null=True  )
	pop2ormore2010 = models.IntegerField( help_text="2010 Population - Two or More Races", blank=True, null= True )
	pcthisp2000 = models.FloatField( help_text="% of Population Hispanic - 2000", blank=True, null=True  )
	pophisp2000 = models.IntegerField( help_text="2000 Population - Hispanic", blank=True, null= True )
	pcthisp2010 = models.FloatField( help_text="% of Population Hispanic - 2010", blank=True, null=True  )
	pophisp2010 = models.IntegerField( help_text="2010 Population - Hispanic", blank=True, null= True )
	pctnonhisp2000 = models.FloatField( help_text="% of Population Non-Hispanic - 2000", blank=True, null=True  )
	popnonhisp2000 = models.IntegerField( help_text="2000 Population - Non-Hispanic", blank=True, null= True )
	pctnonhisp2010 = models.FloatField( help_text="% of Population Non-Hispanic - 2010", blank=True, null=True  )
	popnonhisp2010 = models.IntegerField( help_text="2010 Population - Non-Hispanic", blank=True, null= True )
	pctwhitenonhisp2000 = models.FloatField( help_text="% of Population White Non-Hispanic - 2000", blank=True, null=True  )
	popwhitenonhisp2000 = models.IntegerField( help_text="2010 Population - White Non-Hispanic", blank=True, null= True )
	pctwhitenonhisp2010 = models.FloatField( help_text="% of Population White Non-Hispanic - 2010", blank=True, null=True  )
	popwhitenonhisp2010 = models.IntegerField( help_text="2010 Population - Asian", blank=True, null= True )
	dividx2000 = models.FloatField( help_text="USA Today Diversity Index - 2000", blank=True, null=True  )
	dividx2010 = models.FloatField( help_text="USA Today Diversity Index - 2010", blank=True, null=True  )

	#area
	total_sqmiles = models.FloatField( help_text = "Square Miles", blank=True, null=True  )
	water_sqmiles = models.FloatField( help_text = "Water in Square Miles", blank=True, null=True  )
	land_sqmiles = models.FloatField( help_text = "Land in Square Miles", blank=True, null=True  )


	objects = models.GeoManager()

	def __unicode__( self ):
		return "%s, %s" % ( self.city_name, self.state )

	def _pop_change_percentage( self ):
		change = self.pop2010 / self.pop2000
		percent = change * 100
		return percent

	class Meta:
		verbose_name_plural = "City Data"


class ZipCodeData( models.Model ):
	#general stuff
	zip_code = models.CharField( max_length="200" )
	state = models.CharField( max_length="2", choices=STATE_CHOICES )
	#pop fields
	pop2000 = models.IntegerField( help_text="2000 Population", blank = True, null = True )
	pop2010 = models.IntegerField( help_text="2010 Population", blank = True, null = True )
	pop2000SqMile = models.FloatField( help_text="2000 Population/Square Mile",blank=True, null=True )
	pop2010SqMile = models.FloatField( help_text="2010 Population/Square Mile",blank=True, null=True )
	pctwhite2000 = models.FloatField( help_text="% of Population White - 2000", blank=True, null=True )
	popwhite2000 = models.IntegerField( help_text="2000 Population - White", blank=True, null= True )
	pctwhite2010 = models.FloatField( help_text="% of Population White - 2010", blank=True, null=True  )
	popwhite2010 = models.IntegerField( help_text="2010 Population - White", blank=True, null= True )
	pctblack2000 = models.FloatField( help_text="% of Population Black - 2000", blank=True, null=True  )
	popblack2000 = models.IntegerField( help_text="2000 Population - Black", blank=True, null= True )
	pctblack2010 = models.FloatField( help_text="% of Population Black - 2010", blank=True, null=True  )
	popblack2010 = models.IntegerField( help_text="2010 Population - Black", blank=True, null= True )
	pctamind2000 = models.FloatField( help_text="% of Population American Indian - 2000", blank=True, null=True  )
	popamind2000 = models.IntegerField( help_text="2000 Population - American Indian", blank=True, null= True )
	pctamind2010 = models.FloatField( help_text="% of Population American Indian - 2010", blank=True, null=True  )
	popamind2010 = models.IntegerField( help_text="2010 Population - American Indian", blank=True, null= True )
	pctasian2000 = models.FloatField( help_text="% of Population Asian - 2000", blank=True, null=True  )
	popasian2000 = models.IntegerField( help_text="2000 Population - Asian", blank=True, null= True )
	pctasian2010 = models.FloatField( help_text="% of Population Asian - 2010", blank=True, null=True  )
	popasian2010 = models.IntegerField( help_text="2010 Population - Asian", blank=True, null= True )
	pctnathaw2000 = models.FloatField( help_text="% of Population Native Hawaiian/Other Pacific Islander - 2000", blank=True, null=True  )
	popnathaw2000 = models.IntegerField( help_text="2000 Population - Native Hawaiian/Other Pacific Islander", blank=True, null= True )
	pctnathaw2010 = models.FloatField( help_text="% of Population Native Hawaiian/Other Pacific Islander - 2010", blank=True, null=True  )
	popnathaw2010 = models.IntegerField( help_text="2010 Population - Native Hawaiian/Other Pacific Islander", blank=True, null= True )
	pctother2000 = models.FloatField( help_text="% of Population Some Other Race - 2000", blank=True, null=True  )
	popother2000 = models.IntegerField( help_text="2000 Population - Some Other Race", blank=True, null= True )
	pctother2010 = models.FloatField( help_text="% of Population Some Other Race - 2010", blank=True, null=True  )
	popother2010 = models.IntegerField( help_text="2010 Population - Some Other Race", blank=True, null= True )
	pct2ormore2000 = models.FloatField( help_text="% of Population Two or More Races - 2000", blank=True, null=True  )
	pop2ormore2000 = models.IntegerField( help_text="2000 Population - Two or more Races", blank=True, null= True )
	pct2ormore2010 = models.FloatField( help_text="% of Population Two or More Races - 2010", blank=True, null=True  )
	pop2ormore2010 = models.IntegerField( help_text="2010 Population - Two or More Races", blank=True, null= True )
	pcthisp2000 = models.FloatField( help_text="% of Population Hispanic - 2000", blank=True, null=True  )
	pophisp2000 = models.IntegerField( help_text="2000 Population - Hispanic", blank=True, null= True )
	pcthisp2010 = models.FloatField( help_text="% of Population Hispanic - 2010", blank=True, null=True  )
	pophisp2010 = models.IntegerField( help_text="2010 Population - Hispanic", blank=True, null= True )
	pctnonhisp2000 = models.FloatField( help_text="% of Population Non-Hispanic - 2000", blank=True, null=True  )
	popnonhisp2000 = models.IntegerField( help_text="2000 Population - Non-Hispanic", blank=True, null= True )
	pctnonhisp2010 = models.FloatField( help_text="% of Population Non-Hispanic - 2010", blank=True, null=True  )
	popnonhisp2010 = models.IntegerField( help_text="2010 Population - Non-Hispanic", blank=True, null= True )
	pctwhitenonhisp2000 = models.FloatField( help_text="% of Population White Non-Hispanic - 2000", blank=True, null=True  )
	popwhitenonhisp2000 = models.IntegerField( help_text="2010 Population - White Non-Hispanic", blank=True, null= True )
	pctwhitenonhisp2010 = models.FloatField( help_text="% of Population White Non-Hispanic - 2010", blank=True, null=True  )
	popwhitenonhisp2010 = models.IntegerField( help_text="2010 Population - Asian", blank=True, null= True )
	dividx2000 = models.FloatField( help_text="USA Today Diversity Index - 2000", blank=True, null=True  )
	dividx2010 = models.FloatField( help_text="USA Today Diversity Index - 2010", blank=True, null=True  )

	#area
	total_sqmiles = models.FloatField( help_text = "Square Miles", blank=True, null=True  )
	water_sqmiles = models.FloatField( help_text = "Water in Square Miles", blank=True, null=True  )
	land_sqmiles = models.FloatField( help_text = "Land in Square Miles", blank=True, null=True  )


	objects = models.GeoManager()

	def __unicode__( self ):
		return "%s, %s" % ( self.county_name, self.state )

	def _pop_change_percentage( self ):
		change = self.pop2010 / self.pop2000
		percent = change * 100
		return percent

	class Meta:
		verbose_name_plural = "Zip Code Data"
