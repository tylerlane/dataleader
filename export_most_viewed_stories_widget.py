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

#need 4 different query sets.
#stories from today
today = datetime.datetime.today()
today_stories = Pageview.objects.filter( time_init__year = today.strftime( "%Y" ), time_init__month=today.strftime( "%m" ), time_init__day=today.strftime( "%d" ) )
today_stories = today_stories.values( 'story' ).annotate( pageviews=Count('id')).order_by('story')
for story in today_stories:
	story['story'] = Story.objects.get( id = story[ 'story' ] )


#stories from yesterday
yesterday = datetime.datetime.today() - datetime.timedelta( days=1 )
yesterday_stories = Pageview.objects.filter( time_init__year = yesterday.strftime( "%Y" ), time_init__month=yesterday.strftime( "%m" ), time_init__day=yesterday.strftime( "%d" ) )	
#yesterday_stories = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( days = 2 ), datetime.datetime.today() - datetime.timedelta( days = 1 ) ) )
yesterday_stories = yesterday_stories.values( 'story' ).annotate( pageviews=Count('id')).order_by('story')
for story in yesterday_stories:
	story['story'] = Story.objects.get( id = story[ 'story' ] )


#stories from the week
week_stories = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( days = 7 ),datetime.datetime.today() ) )
week_stories = week_stories.values( 'story' ).annotate( pageviews=Count('id')).order_by('story')
for story in week_stories:
	story['story'] = Story.objects.get( id = story[ 'story' ] )


#stories from the month
month_stories = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( days = 30 ), datetime.datetime.today() ) )
month_stories = month_stories.values( 'story' ).annotate( pageviews=Count('id')).order_by('story')
for story in month_stories:
	story['story'] = Story.objects.get( id = story[ 'story' ] )


print "Generating html for most viewed stories"
widget =  render_to_string( 'stories/pageviews_widget.html', { 'today_stories': today_stories, 'yesterday_stories': yesterday_stories, 'week_stories': week_stories, 'month_stories': month_stories } )

print "Opening file"
fh = open( '/opt/django/data.news-leader.com/dataleader/temp/mostviewed_widget.html', 'w' )

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
fh = open( '/opt/django/data.news-leader.com/dataleader/temp/mostviewed_widget.html' , 'rb' )
print "uploading the file to the ftp server"
ftp.storbinary( 'STOR mostviewed_widget.html', fh )
fh.close()
print "File Uploaded Successfully"
ftp.close()


