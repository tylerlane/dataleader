#/usr/bin/env python
import datetime
import ftplib
#import os
#import sys
#import time
import random
#setting my django environment
from django.core.management import setup_environ
import settings
setup_environ(settings)

#django specific modules
#from django.db.models import Avg,Min,Max,Count,F,Q
from django.template.loader import render_to_string
from scheduler.models import Position,Banner, Schedule

#config variables for uploading the most viewed widget file
UPLOAD_HOST = "ftp3.moc.gbahn.net"
UPLOAD_PATH = "/moc.news-leader.com/home/includes/scheduler"
UPLOAD_USERNAME = "springfield-cms"
UPLOAD_PASSWORD = "b17biuT$"


#then we make our FTP connection
print "making our FTP connection"
ftp = ftplib.FTP()
ftp.connect( UPLOAD_HOST, 21 )
ftp.login( UPLOAD_USERNAME, UPLOAD_PASSWORD )
# move to the desired upload directory
ftp.cwd( UPLOAD_PATH )

#get our positions first
positions = Position.objects.all()
for position in positions: 
	
	banners = Banner.objects.filter( position = position )

	display_banner = False

	now = datetime.datetime.today()
	temp = []
	for banner in banners:
		schedules = Schedule.objects.filter( banner = banner, start_time__lte = now, end_time__gte = now )
	
		if len( schedules ) >= 	1:
			temp.append( banner )
		
	if len( temp ) > 0:
		banner = temp[ random.randrange( 0, len( temp ) ) ]
	else:
		banner = Banner()
		banner.content = "<!-- This space intentionally left blank....... -->"
	
	
	print "Generating html for banner @ position: %s " % position
	banner = render_to_string("scheduler/banner.html", {'banner': banner } )
	
	print "Opening file"
	file_name = position.file_name
	fh = open( '/opt/django/data.news-leader.com/dataleader/temp/%s' % file_name, 'w' )
	
	print "Writing the html to our file"
	fh.write( banner )
	
	print "Closing our file handler"
	fh.close()
	
	#opening the file handler
	fh = open( '/opt/django/data.news-leader.com/dataleader/temp/%s' % file_name , 'rb' )
	print "uploading the file to the ftp server"
	ftp.storbinary( 'STOR %s' % position.file_name, fh )
	fh.close()
	print "File Uploaded Successfully"
#closing the ftp connection
ftp.close()
