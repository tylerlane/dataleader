#!/usr/bin/env python
from django.core.management import setup_environ
import settings
setup_environ( settings )
from django.contrib.gis import geos
from django.contrib.gis.measure import D

from restaurants.models import Restaurant,Inspection
from datetime import *
#import time
from lib import bail
from BeautifulSoup import BeautifulSoup
from calls.textutils import clean_address
from geopy import geocoders
from geopy.distance import distance as geopy_distance
import feedparser
import string
#seeing which path to use.
import socket
if socket.gethostname() == "2155529.pubip.peer1.net":
	g = geocoders.Google('ABQIAAAA2JAd-KesRNeDJwroL49_CxTC4wGmoCeUv8j3n4Pev0Dsu3hwqxS_gg6u4S_FFZd8gO-pLGIZ4Ui7VQ')
else:
	g = geocoders.Google('ABQIAAAA2JAd-KesRNeDJwroL49_CxRMPgAshc9HvuksOF-1hbNeUnHu2RR3TUaykJvxoc7edBwXZYs044EM3w')


inspections_url = "http://apps.springfieldmo.gov/food/rss.aspx"
feed = feedparser.parse(inspections_url)

# print feed

for entry in feed.entries:
	# print "title = " + entry.title
	title_split = entry.title.split( " - " )
	name = title_split[0].replace( "&amp;", "&").replace( "&lt;", "<").replace( "&gt;", ">")
	address = title_split[-1]
	#now to split off the address and city
	#this is going to be very hackish
	address_split = address.split(" ")
	city = address_split[-1]
	address = address[:-len(city)]
	inspection_date = entry.published

	#print "name = " + name
	#print "address = " + address
	#print "city = " + city
	#print "summary_detail = " + entry.summary_detail.value
	#print "Inspection Date = " + inspection_date 
	inspection_date_year = inspection_date.split("/")[2]
	inspection_date_month = inspection_date.split("/")[0]
	inspection_date_day = inspection_date.split("/")[1]
	inspection_date = inspection_date_year + "-" + inspection_date_month + "-" + inspection_date_day
	# today = datetime.today()
	# inspection_date_new = datetime.strptime(inspection_date, )
	# if inspection_date_new > today.date():
	# 	print "Inspection can NOT be in the future!! broken!!!!"
	# 	break

	summary_detail_split = entry.summary_detail.value.split( "<ol>" )
	# print summary_detail_split
	critical_violations = summary_detail_split[0][26:]
	noncritical_violations = summary_detail_split[1].split("</ol>")[1][30:]
	
	#print "critical_violations = " + critical_violations
	#print "noncritical_violations = " + noncritical_violations
	#entry.summary_detail.value.split( "<ol>" )[0][26:]
	critical_violations_text = ""
	noncritical_violations_text = ""
	#if we have critical violations lets get them
	if critical_violations > 0:
		#loop through the critical violations
		for li in entry.summary_detail.value.split("Critical Violations Found:")[1].split("Noncritical Violations Found:")[0].split("<li>")[1:]:
			#use beautifulsoup to get just the text of the li.
			soup = BeautifulSoup(li)
			# print soup
			critical_violations_text += str( soup ) + ", "
		#checking to see if the last char is a comma
		if critical_violations_text.strip()[-1:] == ",":
			#remove the comma
			critical_violations_text = critical_violations_text.strip()[:-1]

		#print "critical_violations_text = " + str( critical_violations_text )
	#if we have noncritical violations lets get them
	if noncritical_violations > 0:
		#loop through the non critical violations
		for li in entry.summary_detail.value.split( "Noncritical Violations Found:")[1].split("<li>")[1:]:
			#beautiful soup to get just the text of the li
			soup = BeautifulSoup(li)
			# print soup
			noncritical_violations_text += str( soup ) + ", "
		#checking for a comma to remove
		if noncritical_violations_text.strip()[-1:] == ",":
			noncritical_violations_text = noncritical_violations_text.strip()[:-1]

		#print "noncritical_violations_text = " + str( noncritical_violations_text )
	
	print "-----------------------"

	#now that we have the info broke out.. lets try to match it to a restaurant.
	print "name = " + name
	print "address = " + address
	print "trying to find an entry for this restaurant"
	#query for the restaurant based on name and address. 
	#i need to come up with a secondary way of searching for the restaurant as well. too easy to miss the restaurant due to slight changes.
 	temp_restaurant,created = Restaurant.objects.get_or_create(name__iexact=name,address__iexact=clean_address(address))
	#get all the restaurants that match the name a filter through them
	#if we create the restaurant, we need to set some vars
	if created is True:
		print "*********************************** CREATED NEW RESTAURANT **********************************"
		#setting various vars for the restaurant
		temp_restaurant.name = name
		temp_restaurant.address = clean_address(address)
		temp_restaurant.city = city
		temp_restaurant.state = "MO"
		temp_restaurant.hours = None
		temp_restaurant.geocoder = None
		temp_restaurant.active = True
		#get the geometry
		print "geocoding restaurant since it isn't tagged"
		try:
			#try to geocode the restaurant. using the first result returned from google
			place, ( lat, lng ) = g.geocode( address + " " + city + ", MO", exactly_one=False )[0]
			#get our lat and lng and put it into a GEOS point
			new_point =  geos.fromstr( 'POINT(' + str(lng)+ " " + str(lat) +')', srid = 4326)
			#save that point into our geometry field.
			temp_restaurant.geom = new_point
		except:
			print "error geocoding"
			temp_restaurant.geom = None
		print "saving restaurant: %s" % name
		temp_restaurant.save()
	else:
		print "Restaurnat %s was already in the system. " % name
	
	print "this is the point we make the inspections"
	#now we try to create aninspection
	inspection,created = Inspection.objects.get_or_create( restaurant = temp_restaurant, date = inspection_date )
	#setting reinspection to be false for now. not sure how we will set this for the new system of restrauant inspections yet.
	inspection.reinspection = False
	inspection.notes = noncritical_violations_text
	inspection.critical = int(critical_violations)
	inspection.noncritical = int(noncritical_violations)
	inspection.critical_violations = critical_violations_text
	#saving inspection even if it was already there.
	inspection.save()
	print "Created/Updated inspection for %s on %s" % (name, inspection_date )

	print "-----------------------"

