#!/usr/bin/env python
import os
import sys
import datetime
import time
from django.contrib.gis.geos import fromstr
from geopy import geocoders
from lib import bail,log_me,email_message
import socket

#seeing which path to use.
if socket.gethostname() == "2155529.pubip.peer1.net":
    sys.path.append('/opt/django/data.news-leader.com')
    g = geocoders.Google('ABQIAAAA2JAd-KesRNeDJwroL49_CxTC4wGmoCeUv8j3n4Pev0Dsu3hwqxS_gg6u4S_FFZd8gO-pLGIZ4Ui7VQ')
else:
    sys.path.append('/Users/tlane2/Code/data/trunk')
    g = geocoders.Google('ABQIAAAA2JAd-KesRNeDJwroL49_CxRMPgAshc9HvuksOF-1hbNeUnHu2RR3TUaykJvxoc7edBwXZYs044EM3w')



#django specific stuff
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from restaurants.models import Restaurant

restaurants = Restaurant.objects.filter(geom__isnull=False).exclude(address__isnull=True,city__isnull=True,state__isnull=True)
count = 0
for restaurant in restaurants:
  count += 1
  print "Trying to geocode %s" % restaurant.name
  try:
    if restaurant.name == "Hultgren Grocery":
      raise ValueError
    place, ( lat, lng ) = g.geocode( restaurant.address + " " + restaurant.city + "," + restaurant.state, exactly_one=True )
    if ( lng is not None or lng != "" ) and ( lat is not None or lng != "" ):
      try:
        restaurant.geom = fromstr( 'POINT(' + str(lng) + " " + str(lat) +')', srid = 4326 )
        print "Setting lat: %s and lng: %s" % ( str( lng ), str( lat ) )
        restaurant.save()
        print "Saving %d" % count
      except:
        print "ERROR!!"
    else:
      print "unable to geocode"
  except ValueError:
    print restaurant.name  + " multiple places!"

  print "Sleeping a second"
  time.sleep(1)
  print "====="

