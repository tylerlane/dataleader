#from django.db import models, IntegrityError
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
    subheadline = models.CharField(max_length=255, blank=True, null=True)
    brief = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)

    #photo
    channel = models.CharField(max_length=25)
    #geocoder stuff
    geocoder = models.CharField(max_length=25, null=True)
    geom = models.PointField(srid=4326, null=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

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
