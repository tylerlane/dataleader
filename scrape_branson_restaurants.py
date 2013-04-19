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

y = geocoders.Yahoo('yo5Br93V34F8u7tt5HOgIsJNIco6b05JjDvzH..nhkLwiKPMJ9ohnxJOBff0uiuiOrU-' )
us = geocoders.GeocoderDotUS()
from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
#django specific stuff
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
#from calls.models import CallType,Jurisdiction,Beat,Call

#dict of column names
#columns = { 0: "call_time", 1: "event_num", 2: "calltype", 3:"description", 4:"response", 5:"beat", 6:"address",7:"report_num" }

#this will pull in our page.
url = 'http://www.taneycohealth.org/showestablishments.php?s=240&q=all'

domain = "http://www.taneycohealth.org"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#parameters to pass to the page.
today = time.time()
yesterday = today - 86400
#yesterday = today - 172800
today = datetime.datetime.fromtimestamp(today )
yesterday = datetime.datetime.fromtimestamp( yesterday )

params = {
			"start_month": str( yesterday.strftime( "%m" ) ), 
			"start_day": str( yesterday.strftime( "%d" ) ), 
			"start_year": str( yesterday.strftime( "%Y" ) ),
			"start_time": str( yesterday.strftime( "%I:%M" ) ), 
			"start_apm": str( yesterday.strftime( "%p" ) ),
			#"start_month": "03", 
			#"start_day": "11", 
			#"start_year": "2010",
			#"start_time": "12:00", 
			#"start_apm": "AM",
			"end_month": str( today.strftime( "%m" ) ),
			"end_day": str( today.strftime( "%d" ) ),
			"end_year": str( today.strftime( "%Y" ) ),
			"end_time": str( today.strftime( "%I:%M" ) ),
			"end_apm": str( today.strftime( "%p" ) )
		}
#print params
#have to set the refer or it will error out. kind of stupid but whatever.
headers = { "User-Agent" : user_agent, "Referer": "http://www.taneycohealth.org/showestablishments.php?q=all" }
data = urllib.urlencode( params )
#print data
req = urllib2.Request( url, data, headers )
response = urllib2.urlopen( req )
the_page = response.read()

soup = BeautifulSoup( the_page )

tables = soup.findAll( 'table' )
count = 0
#find the rows in the table
trs = tables[1].findAll( 'td',{'valign': 'top'} )
#loop through the rows
for tr in trs:
	#find the colums in the row
	tds = tr.findAll( 'a' )
	for td in tds:
		if td["href"].split(".")[0] == "showinspections":
			count +=1
			#print "pulling info from " + domain + "/" + td["href"]
			if count <= 60:
				inspection_url = domain + "/" + td["href"]
				req = urllib2.Request( inspection_url, data, headers )
				response = urllib2.urlopen( req )
				the_page = response.read()

				inspection_page = BeautifulSoup( the_page )
				h3 = inspection_page.findAll('h3')
				print "%s - Restaurant Name: %s" % (count, h3[0].contents[0] )
				#print inspection_page
				address = inspection_page.findAll('td', {'valign':'top'} )
				print address[3].contents[9]
				print address[3].contents[11]
				print address[3].contents[13]
				print address[3].contents[15]
				print "---------------------"





