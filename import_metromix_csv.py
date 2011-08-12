#setting my django environment
from django.core.management import setup_environ
import settings
setup_environ( settings )

from restaurants.models import Restaurant 
from lib import bail
import datetime
import time
import csv
rows = csv.reader( open( "metromix_restaurants.csv" ) )

count = 0
for row in rows:
  #print "%d %s" % ( count, row )
  if count != 0 and row[4] =="Live":
    #
    restaurant,rest_created  = Restaurant.objects.get_or_create( name=row[3],address=row[9] )
    if rest_created is True:
      print "Creating Restaurant for %s " % row[3]
      print "%d %s" % ( count, row )
    else:
      print "Updating Restaurant for %s " % row[3]
      print "%d %s" % ( count, row )
    restaurant.name = row[3]
    restaurant.address = row[9]
    restaurant.city = row[10]
    restaurant.state = "MO"
    restaurant.zip_code = row[11]
    restaurant.website = row[12]
    restaurant.phone = row[13]
    restaurant.channel = row[5]
    #othershit
    print row[15].split("by")
    last_updated = time.strptime(row[15].split(" by ")[0],"%b %d, %Y ")
    restaurant.subheadline = row[16]
    restaurant.brief = row[17]
    restaurant.long_description = row[18]

    print "saving..."
    restaurant.save()

  count = count + 1
