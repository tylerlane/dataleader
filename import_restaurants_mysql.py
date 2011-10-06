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
from restaurants.models import Restaurant,Inspection
from lib import * 

#setup the mysql connection
import MySQLdb

#Config variables
if socket.gethostname() == "2155529.pubip.peer1.net":
  db_hostname = "data.news-leader.com"
  db_username = "admin"
  db_password = "php3xtr@5"
  db_name = "restaurantInspections"
else:
  db_hostname = "10.37.74.210"
  db_username = "admin"
  db_password = "php3xtr@5"
  db_name = "restaurantInspections"

#connect to our database 
conn = MySQLdb.connect( host=db_hostname,user=db_username,passwd=db_password,db=db_name,use_unicode=True )
cursor = conn.cursor( MySQLdb.cursors.DictCursor )


query = "SELECT * FROM restaurants INNER JOIN inspections ON restaurants.ID = inspections.ID ORDER BY inspections.inDate ASC"
cursor.execute( query )
rows = cursor.fetchall()
count = 0
for row in rows:
  address_split = row["address"].split("<br />")
  new_address =address_split[0][0:-1]
  if len(address_split) > 1:
    new_city = address_split[1]
  else:
    new_city = "Springfield"
  restaurant,created = Restaurant.objects.get_or_create( name  = row["name"],address=new_address,city=new_city,state="MO")
  restaurant.save()
  
  inspection,created = Inspection.objects.get_or_create( restaurant = restaurant, date = row["inDate"] )
  #setting reinspection
  if row["inType"] == "Reinspection":
    inspection.reinspection = True
  inspection.notes = row["notes"]
  inspection.critical = row["critical"]
  inspection.noncritical = row["noncritical"]
  inspection.critical_violations = row[ "cviolations"]
  inspection.save()

  count +=1
  print "%d: %s: %s" % (count, created, row["name"])




