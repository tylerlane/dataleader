#from django.db import models
#GeoDjango support
from django.contrib.gis.db import models
#import datetime


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
    hours = models.CharField(max_length=100, null=True)

    #geocoder stuff
    geocoder = models.CharField(max_length=25, null=True)
    geom = models.PointField(srid=4326, null=True)

    #many to many relationship for cuisines
    cuisine = models.ManyToManyField("Cuisine", related_name="Cuisines", null=True)
    #cuisines = models.CharField(max_length=255, blank=True, null=True)
    #boolean for open/out of business restaurants
    active = models.BooleanField(default=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return u"%s" % self.name

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
        return u"%s" % self.name


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
