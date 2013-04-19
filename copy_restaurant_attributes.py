#!/usr/bin/env python
import os
import sys
import datetime
import time
from django.contrib.gis.geos import fromstr
from geopy import geocoders
from lib import bail,log_me,email_message
import socket

#django specific stuff
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from restaurants.models import Restaurant,Attribute,Cuisine

# from django.contrib.gis.geos import Point
# from django.contrib.gis.measure import D
# from django.db.models import Avg,Min,Max,Count,F,Q
# from django.contrib.gis import geos

orig_restaurant_id = 7755 

to_restaurants = [ 8160 ]

orig_restaurant = Restaurant.objects.get(id=orig_restaurant_id)
print "Pulling original restaurant: %s" % orig_restaurant.name
orig_restaurant_attribs = Attribute.objects.filter(restaurant=orig_restaurant)

#loop through all of the restaurants we will be copying attributs TO
for restaurant in to_restaurants:
	to_restaurant = Restaurant.objects.get(id=restaurant)
	print "Pulling restaurant record: %s" % to_restaurant.name
	#delete the attributes
	to_attribs = Attribute.objects.filter(restaurant=to_restaurant)
	for attr in to_attribs:
		print "deleting attribute: %s - %s"  % (to_restaurant.name, attr.name)
		attr.delete()

	#now we make our new attributes
	for attr in orig_restaurant_attribs:
		new_attr = Attribute(restaurant=to_restaurant,name=attr.name,value=attr.value,active = attr.active)
		print "copying attribute: %s - %s for %s" % (attr.name,attr.value,to_restaurant.name)
		new_attr.save()

	for cuisine in orig_restaurant.cuisine.all():
		print cuisine
		to_restaurant.cuisine.add(cuisine)



