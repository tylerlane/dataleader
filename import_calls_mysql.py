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
from django.conf import settings
from calls.models import CallType
from calls.models import Jurisdiction
from calls.models import Beat
from calls.models import Call
from lib import * 

#setup the mysql connection
import MySQLdb

#Config variables
if socket.gethostname() == "2155529.pubip.peer1.net":
	db_hostname = "localhost"
	db_username = "admin"
	db_password = "php3xtr@5"
	db_name = "PoliceCalls"
else:
	db_hostname = "10.37.74.212"
	db_username = "tlane"
	db_password = "nof<jat"
	db_name = "crime"

#connect to our database 
conn = MySQLdb.connect( host=db_hostname,user=db_username,passwd=db_password,db=db_name,use_unicode=True )
cursor = conn.cursor( MySQLdb.cursors.DictCursor )


query = "SELECT * FROM calls ORDER BY CallID DESC"
cursor.execute( query )
rows = cursor.fetchall()
count = 0
#can do jurisdiction outside of the loop cause it won't change.
juri = Jurisdiction.objects.get( pk=1 )
for row in rows:
	try:
		beat = Beat.objects.get(name=str( row[ "Beat" ] ) )
	except:
		print "No Beat found for %s" % row[ "Beat" ]
		beat = Beat()
		beat.name = row[ "Beat" ]
		beat.jurisdiction = juri
		beat.save()
	try:
		call_type = CallType.objects.get( name__iexact=row[ "CallType" ].strip().upper() )
		#print "FOUND call_type: %s" % call_type
	except:
		print bail()
	
	try:
		call = Call.objects.get( event_num__iexact = row[ "EventNum" ].strip() )
		action = "UPDATE"
	except:
		call = Call()
		action = "INSERT"
		
	call.description = row[ "Description" ]
	call.event_num = row[ "EventNum" ]
	call.report_num = row[ "ReportNum" ]
	call.response = row[ "Response" ]
	call.address = row[ "Address" ]
	call.zip_code = row[ "Zip" ]
	call.call_time = row[ "CallTime" ]
	call.call_type = call_type
	call.calltype_id = call_type.id
	call.beat = beat
	if ( row[ "Lng" ] is not None or row[ "Lng" ] != "" ) and ( row[ "Lat" ] is not None or row[ "Lng" ] != "" ):
		try:
			call.geom = fromstr('POINT(' + row[ "Lng"] + " " + row[ "Lat" ] +')', srid=4326)
		except:
			print "ERROR setting the geometry! for %s" % row[ "EventNum" ]


	call.jurisdiction = juri
	
	call.save()
	#print dir( call )
	count +=1
	print "%d: %s: %s" % (count, action, row["EventNum"])
