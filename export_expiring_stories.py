#/usr/bin/env python
import datetime
import os
import simplejson
import socket
import sys
import time
from lib import email_message
#setting my django environment
from django.core.management import setup_environ
import settings
setup_environ(settings)

#django specific modules
from django.db.models import Avg,Min,Max,Count,F,Q
from django.template.loader import render_to_string
from stories.models import Pageview,Story,Keyword



#get the featured stories first
pvs = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( days = 15 ), datetime.datetime.today() - datetime.timedelta( days = 13 ) ) ).exclude( story__featured = True )

pvs = pvs.values('story').annotate( pageviews = Count( 'id' ) ).order_by( '-pageviews' )[:15]


for pv in pvs:
	pv[ 'story' ] = Story.objects.get( id = pv[ 'story' ] )
	


#for pv in pvs:
#	print pv

#put in code for emailing here.
start = datetime.datetime.today() - datetime.timedelta( days = 14 )
start = start.strftime( "%m-%d-%Y")

message = "Here are the top 15 stories on %s. Please look and evergreen stories as needed.\r\n\r\n" % ( start )
count = 1
for pv in pvs: 
	print repr( pv["story"] )
	message += "%d: Story: %s\r\n  Date Published: %s, Pageviews: %d \r\n URL: %s \r\n\r\n" % ( count,  pv["story"].headline, pv["story"].date_published.strftime("%m-%d-%Y"), pv["pageviews"],pv["story"].short_url )
	count += 1

print message
email_message( "Online","data@news-leader.com","Data Server","tlane@news-leader.com", "Expiring Story Pageview Report", message )