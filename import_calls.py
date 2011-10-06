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
from calls.models import CallType,Jurisdiction,Beat,Call

#dict of column names
columns = { 0: "call_time", 1: "event_num", 2: "calltype", 3:"description", 4:"response", 5:"beat", 6:"address",7:"report_num" }

#this will pull in our page.
url = 'http://www.springfieldmo.gov/spd/HowDoI/spd_calls_results.jsp'
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
			#"start_day": "30", 
			#"start_year": "2010",
			#"start_time": "12:00", 
			#"start_apm": "AM",
			"end_month": str( today.strftime( "%m" ) ),
			"end_day": str( today.strftime( "%d" ) ),
			"end_year": str( today.strftime( "%Y" ) ),
			"end_time": str( today.strftime( "%I:%M" ) ),
			"end_apm": str( today.strftime( "%p" ) )
		}
print params
#have to set the refer or it will error out. kind of stupid but whatever.
headers = { "User-Agent" : user_agent, "Referer": "http://www.springfieldmo.gov/spd/HowDoI/spd_calls.jsp" }
data = urllib.urlencode( params )
print data
req = urllib2.Request( url, data, headers )
response = urllib2.urlopen( req )
the_page = response.read()

soup = BeautifulSoup( the_page )

tables = soup.findAll( 'table' )
parse_row_count = 0
calls = []
for table in tables:
	#find the rows in the table
	trs = table.findAll( 'tr' )
	#loop through the rows
	for tr in trs:
		#find the colums in the row
		tds = tr.findAll( 'td' )
		call = {}
		count = 0
		if parse_row_count in [0,1]:
			pass
		else:
			for td in tds:
					if td.find( text=True) is not None:
						#stripping the leading and trailing whitespace from our text.
						call[ columns[ count ] ] = td.find( text=True ).lstrip().rstrip()
					else:
						call[ columns[ count ] ] = td.find( text=True )
					count += 1
			#if we have something in our call dict we put it in our calls dict
			if call is not None:
				calls.append( call )
				#print call
		parse_row_count +=1
		print parse_row_count
#pulling in our jurisdiction object incase we need to set it.
juri = Jurisdiction.objects.get( pk=1 )

error_list = []
success_list = []
geocode_error_list = []
google_count = 0
yahoo_count = 0
geocoder_count = 0
skip_count = 0
update_count = 0
row_count = 0
for call in calls:
	if len(call.keys()) == 0:
		pass
	else:
		#print call
		try:
			if call[ "beat" ] == None:
				call[ "beat" ] = ""
				print "Setting beat to an empty string instead of None"
			beat = Beat.objects.get( name__iexact = str( call[ "beat" ] ) )
			print "FOUND beat: %s" % call[ "beat" ]
		except:
			bail()
			print "No Beat found for %s" % call[ "beat" ]
			beat = Beat()
			beat.name = call[ "beat" ]
			beat.jurisdiction = juri
			beat.save()
		
		try:
			calltype = CallType.objects.get( name__iexact = str( call[ "calltype" ] ) )
			print "FOUND calltype: %s" % call[ "calltype" ]
		except:
			bail()
			print "didn't find a calltype for %s" % call[ "calltype" ]
			calltype = CallType( name = call[ "calltype" ], jurisdiction = juri, active = True )
			calltype.save()
		
		try:
			new_call = Call.objects.get( event_num__iexact = str( call[ "event_num" ] ) )
			print "FOUND call: %s" % call[ "event_num" ]
			#print "Checking to see if response or report has changed"
			#
			#updated = False
			#if( ( new_call.response == None or new_call.response == "" ) and ( call[ "response" ] != None or call[ "response" ] != "" ) ):
				#print "Response changed! db record is %s, website record is %s" % new_call.reponse, call[ "response" ]
				#new_call.response = call[ "response" ]
				#updated = True
			#if( (new_call.report_num == None or new_call.report_num == "" ) and ( call[ "report_num" ] != None or call[ "report_num" ] != "" ) ):
				#print "Report_num changed! db record is %s, website record is %s" % new_call.report_num, call[ "report_num" ]
				#new_call.report_num = call[ "report_num" ]
				#updated = True
			#if updated is True:
				#new_call.save()
				#print "UPDATING call: %s" % call[ "event_num" ]
				#update_count += 1
			#else:
			skip_count +=1 
			print "SKIPPING call: %s" % call[ "event_num" ]

		except:
			try:
				new_call = Call()
				print "creating call for " + call[ "event_num" ]
				#call was created. lets set all our shit about it
				new_call.calltype = calltype
				new_call.beat = beat
				new_call.jurisdiction = juri
				new_call.event_num = call[ "event_num" ]
				new_call.response = call[ "response" ]
				new_call.description = call[ "description" ]
				if call[ "address" ] != "" and call[ "address" ] is not None:
					call[ "address" ] = call[ "address" ].replace( "&", " & ")
					call[ "address" ] = call[ "address" ].replace( "US65", "US 65" )
					call[ "address" ] = call[ "address" ].replace( "JRF","James River Freeway" )
					#for some reason there is a bunch of addresses that are like "N; Boonville instead of just N Boonville"
					call[ "address" ] = call[ "address" ].replace( ";", "" )
				
				new_call.address = call[ "address" ]
				
				new_call.report_num = call[ "report_num" ]
				call_time = time.strptime(call[ "call_time" ],"%m/%d/%y %I:%M:%S %p")
				new_call.call_time = time.strftime("%Y-%m-%d %H:%M:%S",call_time)
				try:
					place, ( lat, lng ) = g.geocode( call[ "address" ] + " Springfield, MO",exactly_one=True )
				except:
					print "google geocode failed. trying yahoo"
					try:
						place, (lat,lng ) = y.geocode( call[ "address" ] + " Springfield, MO",exactly_one=True)
					except:
						print "yahoo geocode failed! trying geocoder.us"
						try:
							place, (lat,lng ) = us.geocode( call[ "address" ] + " Springfield, MO", exactly_one=True)
						except:
							print "Geocoder.us failed!!"
							
						else:
							print "using Geocoder.us lat/lng"
							geocoder_count += 1
							new_call.geocoder = "geocoder.us"
					else:
						print "using Yahoo lat/lng"
						yahoo_count += 1
						new_call.geocoder = "yahoo"
				else:
					print "using google lat/lng"
					google_count += 1
					new_call.geocoder = "google"
					
				if ( lng is not None or lng != "" ) and ( lat is not None or lng != "" ):
					try:
						new_call.geom = fromstr( 'POINT(' + str(lng) + " " + str(lat) +')', srid = 4326 )
					except:
						print "ERROR! setting the lat/lng for this call"
						new_call.geocoder = None
						geocode_error_list.append( call[ "event_num" ] )
				new_call.save()
				#it saved so we'll put it in our success dict
				success_list.append( call[ "event_num" ] )
			except:
				error_list.append( call[ "event_num" ] )
				bail()


output = "================================================="
output += "\r              Summary of Calls Imported          "
output += "\r"
output += "\rTotal Calls Parsed: %d" % ( parse_row_count -2 )
output += "\rTotal Calls Inserted: %d" % len( success_list )
#output += "\rTotal Calls Updated: %d" % update_count
output += "\rTotal Calls Skipped: %d" % skip_count
output += "\rCalls geocoded using Google: %d" % google_count
output += "\rCalls geocoded using Yahoo: %d" % yahoo_count
output += "\rCalls geocoded using Geocoder.us: %d" % geocoder_count
output += "\r================================================="
if len( geocode_error_list ) > 0:
	output += "\rThese calls had errors on geocoding. ( Please look at and fix them!)"
	for error in geocode_error_list:
		output += "\r" + error
	output += "\r"
	output += "\r================================================="
if len( error_list ) > 0:
	output += "\rThese  calls had errors saving to the database. ( Please look at and fix them!)"
	for error in error_list:
		output += "\r" + error
	output += "\r================================================="
		
print output

email_message('Online Staff','tlane@news-leader.com','911 Calls Importer','python@nolongervalid.com','911 Calls Import: ' + today.strftime("%m-%d-%Y %I:%M %p"), output)



