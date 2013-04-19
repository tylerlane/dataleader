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
from restaurants.models import Restaurant,Attribute,Cuisine,Inspection

# from django.contrib.gis.geos import Point
# from django.contrib.gis.measure import D
# from django.db.models import Avg,Min,Max,Count,F,Q
# from django.contrib.gis import geos




merge_restaurants_list = [8355]
keep_restaurant_id = 8356
main_restaurant = Restaurant.objects.get(id=keep_restaurant_id)

for restaurant_id in merge_restaurants_list:
    if restaurant_id != keep_restaurant_id:
        #find the restaurant
        restaurant = Restaurant.objects.get(id=restaurant_id)
        #now find all of the inspections
        inspections = Inspection.objects.filter(restaurant=restaurant)
        #loop through them
        for inspection in inspections:
            #set the restaurant to the new restaurant
            inspection.restaurant = main_restaurant
            #save the inspection
            inspection.save()
        #now we delete the old restaurant
        restaurant.delete()
