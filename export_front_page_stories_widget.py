#/usr/bin/env python
import datetime
import ftplib
import os
import simplejson
import socket
import sys
import time

#setting my django environment
from django.core.management import setup_environ
import settings
setup_environ(settings)

#django specific modules
from django.db.models import Avg,Min,Max,Count,F,Q
from django.template.loader import render_to_string
from stories.models import Pageview,Story,Keyword

#config variables for uploading the most viewed widget file
UPLOAD_HOST = "ftp3.moc.gbahn.net"
UPLOAD_PATH = "/moc.news-leader.com/home/includes/mostviewed"
UPLOAD_USERNAME = "springfield-cms"
UPLOAD_PASSWORD = "b17biuT$"

#get the featured stories first
featured = Story.objects.filter( featured = True )
now = datetime.datetime.today()
pvs = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( seconds = 2700 ), datetime.datetime.today() ) ).exclude( story__featured = True )
pvs = pvs.values('story').annotate( pageviews = Count( 'id' ) ).order_by( 'story' )

stories = Story.objects.filter( featured=False ).order_by( '-date_published' )[:15]
for pv in pvs:
	pv[ 'story' ] = Story.objects.get( id = pv[ 'story' ] )
	

print "Generating html for most viewed stories front page widget"
widget =  render_to_string( 'stories/front_page_stories_widget.html', {'featured': featured, 'pvs': pvs, 'stories': stories } )

print "Opening file"
fh = open( '/opt/django/data.news-leader.com/dataleader/temp/front_page_stories_widget.html', 'w' )

print "Writing the html to our file"
fh.write( widget )

print "Closing our file handler"
fh.close()


#then we make our FTP connection
print "making our FTP connection"
ftp = ftplib.FTP()
ftp.connect( UPLOAD_HOST, 21 )
ftp.login( UPLOAD_USERNAME, UPLOAD_PASSWORD )
# move to the desired upload directory
ftp.cwd( UPLOAD_PATH )
#opening the file handler
fh = open( '/opt/django/data.news-leader.com/dataleader/temp/front_page_stories_widget.html' , 'rb' )
print "uploading the file to the ftp server"
ftp.storbinary( 'STOR front_page_stories_widget.html', fh )
fh.close()
print "File Uploaded Successfully"
ftp.close()


