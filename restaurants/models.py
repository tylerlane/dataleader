#from django.db import models
#GeoDjango support
from django.contrib.gis.db import models
#import datetime
from django.forms import ValidationError
from calls.textutils import clean_address,smart_title
import re

# def clean_address( addr ):
#     """
#     Given an address string, normalizes it to look pretty.

#     >>> clean_address('123 MAIN')
#     '123 Main'
#     >>> clean_address('123 MAIN ST')
#     '123 Main St.'
#     >>> clean_address('123 MAIN ST S')
#     '123 Main St. S.'
#     >>> clean_address('123 AVENUE A')
#     '123 Avenue A'
#     >>> clean_address('2 N ST LAWRENCE PKWY')
#     '2 N. St. Lawrence Pkwy.'
#     >>> clean_address('123 NORTH AVENUE') # Don't abbreviate 'AVENUE'
#     '123 North Avenue'
#     >>> clean_address('123 N. Main St.')
#     '123 N. Main St.'
#     >>> clean_address('  123  N  WABASH  AVE   ')
#     '123 N. Wabash Ave.'
#     >>> clean_address('123 MAIN ST SW')
#     '123 Main St. S.W.'
#     >>> clean_address('123 MAIN ST NE')
#     '123 Main St. N.E.'
#     >>> clean_address('123 NEW YORK ST NE') # Don't punctuate 'NEW' (which contains 'NE')
#     '123 New York St. N.E.'
#     >>> clean_address('123 MAIN St Ne')
#     '123 Main St. N.E.'
#     >>> clean_address('123 MAIN St n.e.')
#     '123 Main St. N.E.'
#     """
#     addr = smart_title(addr)
#     addr = re.sub(r'\b(Ave|Blvd|Bvd|Cir|Ct|Dr|Ln|Pkwy|Pl|Plz|Pt|Pts|Rd|Rte|Sq|Sqs|St|Sts|Ter|Terr|Trl|Wy|N|S|E|W)(?!\.)\b', r'\1.', addr)

#     # Take care of NE/NW/SE/SW.
#     addr = re.sub(r'\b([NSns])\.?([EWew])\b\.?', lambda m: ('%s.%s.' % m.groups()).upper(), addr)

#     addr = re.sub(r'\s\s+', ' ', addr).strip()
#     return addr


STATUS_CHOICES = (
    ('NEW', 'New'),
    ('UPDATED','Updated'),
)


# Create your models here
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=5, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    website = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    last_updated = models.DateTimeField("Last Updated", auto_now=False,
            auto_now_add=False, null=True)
    description = models.TextField(blank=True, null=True)

    #photo
    photo_url = models.URLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    #channel = models.CharField(max_length=25, null=True, blank=True)
    hours = models.CharField(max_length=100, null=True,blank=True)

    #geocoder stuff
    geocoder = models.CharField(max_length=25, null=True,blank=True)
    geom = models.PointField(srid=4326, blank=True,null=True)

    #many to many relationship for cuisines
    cuisine = models.ManyToManyField("Cuisine", related_name="Cuisines", null=True)
    #cuisines = models.CharField(max_length=255, blank=True, null=True)
    #boolean for open/out of business restaurants
    active = models.BooleanField(default=True)

    #ratings support
    rating_sum = models.IntegerField(null=True, blank=True)
    rating_total_votes = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=25,default="NEW",choices=STATUS_CHOICES)
    objects = models.GeoManager()

    def __unicode__(self):
        return u"%s" % self.name

    @models.permalink
    def get_absolute_url(self):
        return ('restaurants.views.detail', self.id )

    def save(self, *args, **kwargs):
        #if total votes is not None, then we calc our rating
        if self.rating_total_votes is not None and self.rating_total_votes > 0:
            self.rating = ( float(self.rating_sum) / float(self.rating_total_votes)  )

        self.address = clean_address(self.address)
        # if self.address is not None:
        #     try:
        #         #try to geocode
        #         place, ( lat, lng ) = g.geocode( self.address + "," + self.city + " " + self.state, exactly_one=False )[0]
        #         #if lat and lgn aren't blank
        #         if ( lng is not None or lng != "" ) and ( lat is not None or lng != "" ):
        #             #set geom for our address
        #             self.geom = fromstr( 'POINT(' + str(lng) + " " + str(lat) +')', srid = 4326 )
        #             self.geocoder = "Google"
        #     except:
        #         #if errors are thrown then we throw an validation error
        #         raise ValidationError     
        
        super(Restaurant, self).save(*args, **kwargs) # Call the "real" save() method.

    class Meta:
        ordering = ("name", "city", )


class Inspection(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    date = models.DateTimeField("Inspection Date", auto_now=False,
            auto_now_add=False)
    reinspection = models.NullBooleanField()
    notes = models.TextField(null=True, blank=True)
    critical = models.IntegerField(null=True, blank=True)
    noncritical = models.IntegerField(null=True, blank=True)
    critical_violations = models.TextField(null=True, blank=True)

    objects = models.Manager()

    def __unicode__(self):
        return u"%s - %s" % (self.restaurant.name, self.date)

    class Meta:
        ordering = ("-date", )


class Cuisine(models.Model):
    name = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=150, null=True, blank=True)

    objects = models.Manager()

    def __unicode__(self):
        return u"%s" % self.label


class Attribute(models.Model):
    #detail must belong to a restaurant
    restaurant = models.ForeignKey('Restaurant')
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    #use this to see if i need to explode the data in value as a list or not
    comma_delimited = models.BooleanField(default=False)

    objects = models.Manager()

    def __unicode__(self):
        return u"%s" % self.name

    def clean(self, *args, **kwargs):
        valid_attrs = ["alcohol", "atmosphere","average entree price","carryout","delivery","dress code","early bird specials",
        "family friendly","happy hour","kids eat free","kids menu","live entertainment","outdoor seating","payment methods accepted","reservations","smoking","wheelchair accessible","wifi"]

        if self.name not in valid_attrs:
            raise ValidationError('Attribute name not in the list! Please fix')

        super(Attribute, self).clean(*args,**kwargs)

    def full_clean(self, *args, **kwargs):
        return self.clean(*args,**kwargs)

    def save(self, *args, **kwargs):
        #override the save function on attributes and make sure that all are lowercase.
        if self.name is not None:
            self.name = self.name.lower().strip()
        if self.value is not None:
            self.value = self.value.lower().strip()

        super(Attribute, self).save(*args, **kwargs) # Call the "real" save() method.


class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    geom = models.PolygonField(blank=True,null=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return u"%s" % self.name


class Featured(models.Model):
    restaurant = models.ForeignKey('Restaurant')
    external_url = models.URLField()
    photo_url = models.URLField()
    title = models.CharField(max_length=100)
    summary = models.TextField()
    date = models.DateTimeField("Date", auto_now=True,
            auto_now_add=True)
    objects = models.Manager()

    def __unicode__(self):
        return u"%s" % self.restaurant.name


class Gallery(models.Model):
    restaurant = models.ForeignKey('Restaurant')
    gallery_url = models.URLField()
    thumbnail_url = models.URLField()
    date = models.DateTimeField("Date", auto_now=True, auto_now_add=True)

    objects = models.Manager()

    def __unicode__(self):
        return u"%s - Gallery: %s" % ( self.restaurant.name, self.date)


class Pageview( models.Model ):
    restaurant = models.ForeignKey( Restaurant, null=True, blank=True )
    time_init = models.DateTimeField( auto_now_add=True, blank=False )

    objects = models.Manager()

    class Meta:
       ordering = ("-restaurant","-time_init",)


class Contest(models.Model):
   name = models.CharField(max_length=255)
   email = models.EmailField(max_length=200)
   time_init = models.DateTimeField( auto_now_add=True, blank=False)
   phone_number = models.CharField(max_length=25)
   address = models.CharField(max_length=200)
   city = models.CharField(max_length=50)
   state = models.CharField(max_length=2)
   zip_code = models.CharField(max_length=12)
   dob = models.DateField(blank=False)

   objects = models.Manager()

   class Meta:
       ordering = ("-time_init",)
