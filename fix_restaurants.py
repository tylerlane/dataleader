#!/usr/bin/env python
from django.core.management import setup_environ
import settings
setup_environ( settings )
from restaurants.models import Restaurant,Cuisine,Attribute
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.db.models import Avg,Min,Max,Count,F,Q
from django.contrib.gis import geos
from geopy import geocoders
from geopy.distance import distance as geopy_distance
import sys,traceback


P = Point( float( -93.292255 ), float(  37.208990 ) )
restaurants = Restaurant.objects.filter(cuisine__isnull=False, geom__distance_gt=( P, D( mi= float( 8 ) )),active=True,city="Springfield").distinct("id")
g = geocoders.Google('ABQIAAAA2JAd-KesRNeDJwroL49_CxTC4wGmoCeUv8j3n4Pev0Dsu3hwqxS_gg6u4S_FFZd8gO-pLGIZ4Ui7VQ')
for restaurant in restaurants:
	try: 
		place, ( lat, lng ) = g.geocode( restaurant.address + " " + restaurant.city + ", MO", exactly_one=False )[0]
		new_point =  geos.fromstr( 'POINT(' + str(lng)+ " " + str(lat) +')', srid = 4326)
		restaurant.geom = new_point
		restaurant.save()
	except Exception, e:
		print "%s didn't geocode properly" % restaurant.name
		print e
		
	else:
		print "%s properly geocoded" % restaurant.name
