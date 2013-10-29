#!/usr/bin/env python
import os
import sys
import socket
import datetime
if socket.gethostname() == "2155529.pubip.peer1.net":
	sys.path.append('/opt/django/data.news-leader.com/')
else:
	sys.path.append('/Users/tlane2/Code/')
	
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.contrib.gis.geos import fromstr
from django.core.files import File
from django.conf import settings
from things.models import Event,Venue,Genre
#from lib import * 


#setup the mysql connection
import MySQLdb

db_hostname = "localhost"
db_username = "admin"
db_password = "php3xtr@5"
db_name = "Calendar"

#connect to our database 
conn = MySQLdb.connect( host=db_hostname,user=db_username,passwd=db_password,db=db_name,use_unicode=True )
cursor = conn.cursor( MySQLdb.cursors.DictCursor )

#query = "SELECT * from event_info JOIN event_dates ON (event_info.EventID = event_dates.EventID) WHERE event_dates.Dates > NOW() AND CompleteEntry ='YES' LIMIT 150"
query = """SELECT * from event_info JOIN event_dates ON (event_info.EventID = event_dates.EventID) JOIN event_location on ( event_info.LocationID = event_location.LocationID) JOIN event_photos ON (event_info.EventID = event_photos.EventID ) JOIN event_extras on (event_info.EventID=event_extras.EventID) WHERE event_dates.Dates > NOW() AND CompleteEntry ='YES' LIMIT 150"""

cursor.execute( query )
rows = cursor.fetchall()
count = 0

for row in rows:
	print row["EventName"]
	print row["Dates"]
	print "----------------------------"

	# venue = Ventue
	venue, created = Venue.objects.get_or_create(
		name=row["LocationName"], 
		address=row["LocationAddress"],
		contact_name=row["LocationName"],
		contact_address=row["LocationAddress"],
		active=True, 
	)
	if created:
		print "Venue Created"
		#saving the venue if it's a new record
		venue.save()

	#now to make the event
	event,created = Event.objects.get_or_create(
		name=row["EventName"],
		description=row["PrintDesc"],
		short_description=row["PrintDesc"][0:155],
		#start_date = datetime.datetime.strptime(row["Dates"], '%Y-%m-%d'),
		start_date = row["Dates"],
		#end_date = datetime.datetime.strptime(row["Dates"], '%Y-%m-%d'),
		end_date = row["Dates"],
		venue=venue,
		active=True
	)
	if row["PhotoID"] != "":
		event.main_photo = "/www/domains/php.news-leader.com/Calendar-Ody/EventImages/Photos/" + str(row["PhotoID"]) + ".jpg"
	print row["Dates"]

	# if row["Dates"]:
	# 	#event.start_date = row["Dates"]
		
		
	# 	#event.end_date = row["Dates"]
	# else:
	# 	event.start_date = datetime.datetime.today()
	# 	event.end_date = datetime.datetime.today()
	event.cost_description = row["Admission"] + " " + row[ "Price1"] + " " + row["Price2"] + " " + row["Price3"] + " " + row["Price4"]  + " " + row["Price5"]
 	event.contact_name = venue.name
	event.contact_address = venue.address
	event.contact_website = row["EventURL"]
	event.contact_email = row[ "Email"]
	event.contact_phone = row["Phone"] + " " + row["Phone2"]
	event.genre.add(Genre.objects.order_by('?')[0])
	event.save()
