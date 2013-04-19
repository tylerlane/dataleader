from django.db import models

# Create your models here.

class CarsFeed( models.Model ):
	model_year = models.IntegerField( max_length = 4, null = False, blank = False, help_text = "Enter year in YYYY format please. eg. 1998" )
	make_name = models.CharField( max_length = 255, null = False, blank = False, help_text = "eg. Mercedes-Benz" )
	model_name = models.CharField( max_length = 255, null = False, blank = False, help_text = "eg. S-Class" )
	trim_name = models.CharField( max_length = 255, null = True, blank = True, help_text = " eg. S320" )
	price = models.IntegerField( max_length = 22, null = True, blank = True, help_text = "Enter the price without the comma, eg. 24995" )
	phone_number = models.CharField( max_length = 16, null = True, blank = True, help_text = "Enter the phone number in the following format XXX-XXX-XXXX" )
	mileage = models.IntegerField( max_length = 22, null = True, blank = True, help_text = "Enter mileage without commas, eg. 68000" )
	add_date = models.DateField( null = False, blank = False, help_text = "Date entered inventory" )
	vin = models.CharField( max_length = 20, null = True, blank = True, help_text = "eg. WDBGA32G2WA400537" )
	stock_number = models.IntegerField( null = False, blank = False, help_text = "cars.com inventory id. unique per dealer. eg. 1035" )
	engine = models.CharField( max_length = 50, null = True, blank = True, help_text = "eg. V8" )
	body_style = models.CharField( max_length = 255, null = True, blank = True, help_text = "eg. Sedan" )
	transmission = models.CharField( max_length = 50, null = True, blank = True, help_text = "eg. Auto" )
	exterior_color = models.CharField( max_length = 50, null = True, blank = True, help_text = "eg. DK Gray" )
	interior_color = models.CharField( max_length = 50, null = True, blank = True, help_text = "eg. Lt Gray" )
	standard_features = models.TextField( max_length = 2000, null = True, blank = True )
	optional_features = models.TextField( max_length = 2000, null = True, blank = True, help_text = "eg. ABS, Air Conditioning, Alloy Wheels, Cassette Radio, Cruise Control, Driver-Side Airbag, Heated Seats, Leather Interior,Passenger-Side Airbag, Power Seats, Sun Roof, Tilt Wheel" )
	dealer_id = models.IntegerField( max_length = 20, blank = False, null = True, help_text = "cars.com dealer id. eg. 8180" )
	dealer_name = models.CharField( max_length = 20, blank = False, null = False, help_text = "eg. Star Motorworks" )
	address = models.TextField( max_length = 510, blank = False, null = False, help_text = "eg. 1723 W. Ogden Ave" )
	city = models.CharField( max_length = 50, blank = False, null = False, help_text = "eg. Downers Grove" )
	state = models.CharField( max_length = 50, blank = False, null = False, help_text = "eg. IL" )
	zip_code = models.CharField( max_length = 50, blank = False, null = False, help_text = "eg. 60515" )
	dealer_url = models.URLField( blank = True, null = True, help_text=" eg, http://www.starmotorworks.com" )
	affiliate = models.CharField( max_length = 40, blank = False, null = False, help_text = "eg. Chicago Tribune" )
	pub1 = models.BooleanField( blank = False, null = False )
	pub2 = models.BooleanField( blank = False, null = False )
	pub3 = models.BooleanField( blank = False, null = False )
	pub4 = models.BooleanField( blank = False, null = False )
	pub5 = models.BooleanField( blank = False, null = False )
	pub6 = models.BooleanField( blank = False, null = False )
	pa_id = models.IntegerField( "PA ID", max_length = 20, null = False, blank = False, primary_key = True, help_text = "Cars.com unique identifier. eg. 176685458" )
	modification_date = models.DateField( null = True, blank = True )
	cpo = models.BooleanField( blank = False, null = False )
	photo_url = models.URLField( null = True, blank = True, help_text = "Photo URL for image that appears on cars.com" )
	notes = models.TextField( max_length = 1005, blank = True, null = True, help_text = "The \"Seller's Note\" field as it appears on the front end cars.com site." )
	original_image = models.URLField( null = True, blank = True, help_text = "Original image sent by dealer or 3rd party before being resized for the cars.com site. In most cases will be a larger image. No standard size." )
	
	objects = models.Manager()
	
	def __unicode__( self ):
		return u'%s - %s (%s) - %s' % ( self.make_name, self.model_name, self.model_year, self.stock_number )
	
	
	class Meta:
		verbose_name = "Car"
		verbose_name_plural = "Cars"