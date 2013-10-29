#!/usr/bin/env python
import os
import sys
import socket

if socket.gethostname() == "2155529.pubip.peer1.net":
	sys.path.append('/opt/django/data.news-leader.com/')
else:
	sys.path.append('/Users/tlane2/Code/')
	
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.contrib.gis.geos import fromstr
from django.core.files import File
from django.conf import settings
from things.models import Event,Venue
import datetime
#from lib import * 

fields = [	"name",
			"short_description",
			"description",
			"parking", 
			"venue" ,
			"cost" ,
			"cost_description" ,
			"excitement" ,
			"main_photo" ,
			# "age",
			# "genre" ,
			"active" ,
			"contact_name" ,
			"contact_address",
			"contact_phone",
			"contact_email",
			"contact_website",
			"start_date",
			"start_time",
			"end_date",
			"end_time",
			"geom",
		]

events = Event.objects.filter(active=True)
for event in events:
	print "copying Event %s" % event.name
	new_event = Event(name=event.name)
	for field in fields:
		print "setting field: %s" % field
		if field not in [ "start_date", "end_date" ]:
			setattr(new_event, field, getattr(event,field))
		else:			
			#setattr(new_event, field, getattr(event,field + datetime.timedelta(days=1)))
			if field == "start_date":
				new_event.start_date = event.start_date + datetime.timedelta(days)
			elif field == "end_date":
				new_event.end_date = event.end_date	+ datetime.timedelta(days=5)
	print "saving the new record"			
	new_event.save()