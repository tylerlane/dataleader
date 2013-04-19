#!/usr/bin/env python
import os
import sys
# import datetime
# import time
# from django.contrib.gis.geos import fromstr
from django.core.urlresolvers import reverse
# from geopy import geocoders
# from lib import bail,log_me,email_message
# import socket
import json as simplejson
#django specific stuff
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from restaurants.models import Restaurant,Attribute,Cuisine,Inspection
import urls


attributes = Attribute.objects.filter(active=True).values("name").distinct("name")

keep = {}
for attribute in attributes:
	attrs = Attribute.objects.filter(name__iexact=attribute["name"],active=True,restaurant__active=True,restaurant__cuisine__isnull=False).values("name","value").distinct("value")
	attributes_list = []

	for attr in attrs:
		#getting a list of values
		attrs_split = attr["value"].split(",")
		for x in attrs_split:
			attributes_list.append(str(x).strip().lower())
	#now that we have the attributes. we remove dups
	last = attributes_list[-1]
	#code to remove duplicates
	seen = set()
	seen_add = seen.add
	attributes_list =  [ x for x in attributes_list if x not in seen and not seen_add(x)]

	keep[attribute["name"]] = {}
	keep[attribute["name"]]["attrs"] = {}

	for attr in attributes_list:
		# print attribute["name"] + " : " + attr
		keep[attribute["name"]]["attrs"][attr] = {}
		keep[attribute["name"]]["attrs"][attr]["name"] = attr
		keep[attribute["name"]]["attrs"][attr]["url"] = reverse('list_restaurants_attribute', kwargs={"attribute": attribute["name"],"value":attr,"page":1})

	# print "---------------------------"

#print repr(keep)
print "saving file"

text_file =  open("/opt/django/data.news-leader.com/dataleader/static/restaurants/restaurant_attribute_values.json","wb")
text_file.write(simplejson.dumps(keep) )
text_file.close()
