#/usr/bin/env python
from BeautifulSoup import BeautifulSoup
import simplejson
import urllib
import sys,os
import datetime
import time
import socket
#my library functions. put in a seperate file for ease
from lib import bail, email_message, log_me, get_sql_var
if socket.gethostname() == "2155529.pubip.peer1.net":
	sys.path.append('/opt/django/data.news-leader.com/')
else:
	#sys.path.append('/Users/tlane2/Code/data/trunk')
	sys.path.append('/Users/tylerlane/Code/news-leader/data/trunk')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from beaches.models import Beach
from django.contrib.gis.geos import fromstr



soup = BeautifulSoup( urllib.urlopen( ' http://mostateparks.com/beaches/index.asp' ) )

#find the first javascript tag, take text from it, replace the new lines and carriage returns with nothing. and then split the string into parts based on the = 
data = soup.find('script',{'type':'text/javascript'}).find( text=True ).replace( "\r\n", "").split( "=" )
#parse the second element of data as a string with simplejson
samples = simplejson.loads( str( data[1] ) )

for sample in samples:
	beach = Beach()
	beach.parkname = sample["parkname"]
	beach.geom = fromstr( 'POINT(' + str(sample["longitude"]) + " " + str(sample["latitude"]) +')', srid = 4326 )
	beach.beach_id = sample["ID"]
	beach.openclosed = sample["openclosed"]
	beach.results1 = sample[ "results1" ]
	beach.results2 = sample[ "results2" ]
	date = sample["sampletaken"].split( "/" )
	beach.sampletaken = datetime.date( int( date[2] ), int( date[0] ), int( date[1] ) )
	beach.save() 





