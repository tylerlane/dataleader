# Create your views here.

from calls.models import Call,CallType
from calls.forms import NightClubForm,ReversePubForm
import datetime
from django.conf import settings
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.auth.decorators import login_required,user_passes_test
from django.db.models import Avg,Min,Max,Count,F,Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
import re
import simplejson
from textutils import *
from zones.models import ReversePubZone

def index( request ):
	calls = dict()
	categories = dict()
	today = datetime.datetime.today()
	yesterday = today - datetime.timedelta(days=1)

	calltypes = CallType.objects.values('category').distinct()
	categories = {}
	for calltype in calltypes:
		if calltype["category"] not in categories.keys():
			categories[ calltype["category"] ] = {}
			categories[ calltype["category"] ][ "name" ] = calltype["category"]
	categories2 = []
	#make it readable for my template
	for category in categories:
		if category == "None" or category == None:
			pass
		else:
			categories2.append( categories[category]["name"] )

	return render_to_response( 'calls/index.html', { 
	'calls_content': render_to_string('calls/calls.html', {'calls': calls } ),
	'categories': categories2 ,
	'today': today,
	'yesterday': yesterday,
	'omniture_pagename': 'Data - Police Calls'
	 }, context_instance = RequestContext(request) )

	
def search( request ):
	#defining P so i can do an if against it later.
	P = None
	if request.GET[ 'lng' ] != "null" and request.GET[ 'lat' ] != "null":
		#if we have Lat and lng and they aren't "null" then we set our point.
		P = Point( float( request.GET['lng'] ), float( request.GET['lat'] ) )
	
	#defining my start and end date variables. settign them to None at first
	start_date = None
	end_date = None
	if str( request.GET[ "start_date" ] ) != "":
		start_date_str = str( request.GET[ "start_date" ] ).split( "-" )
		#the start_date is in mm-dd-yy. the python object wants yy,mm,dd
		start_date = datetime.date( int( start_date_str[2] ),int( start_date_str[0] ),int( start_date_str[1] ) )
		start_time = datetime.time(0,0)
		start_date = datetime.datetime.combine(start_date,start_time)
	
	if str( request.GET[ "end_date" ] ) != "":
		#the end_date is in mm-dd-yy. the python object wants yy,mm,dd
		end_date_str = str( request.GET[ "end_date" ] ).split( "-" )
		end_date = datetime.date( int( end_date_str[2] ),int( end_date_str[0] ) , int( end_date_str[1] ) )
		end_time = datetime.time(23,59)
	 	end_date = datetime.datetime.combine(end_date,end_time)
	
	#start with our base object
	calls = Call.objects.all()
	#if we have our start and end date then we filter based on our dates.
	if start_date != None and end_date != None:
		calls = Call.objects.filter( call_time__range=(start_date,end_date) )
	if P != None:
		# if we have a point defined, then we'll filter the results based on the distance from a point.
		#P is our Point. D is the distance function from geodjango
		calls = calls.filter( geom__distance_lt=( P, D( mi= float( request.GET[ "radius" ] ) ) ) ).distance(P).order_by('-call_time')
	if "category" in request.GET.keys():
		if request.GET[ "category" ] != "all":
			#print "category != all"
			calls = calls.filter( calltype__category=request.GET[ "category" ])
	
	if float( request.GET[ "limit_results" ] ) > 0:
		#if we have a limit_results then we'll put a limit on them.
		calls  = calls.order_by('-call_time')[:float( request.GET[ "limit_results" ] )]
	
	if calls.count() > 0:
		calls2 = Call.objects.filter(id__in=calls).order_by('-call_time')
		end = calls2[0].call_time
	
		calls3 = Call.objects.filter(id__in=calls2).order_by('call_time')
		start = calls3[0].call_time
	else:
		end = None
		start = None
	#print calls.query
	calltypes = CallType.objects.filter(call__in=calls).values('category').annotate(count=Count('call')).distinct()
	categories = {}
	for calltype in calltypes:
		if calltype["category"] not in categories.keys():
			categories[ calltype["category"] ] = {}
			categories[ calltype["category"] ][ "name" ] = calltype["category"]
			categories[ calltype["category"] ][ "count" ] = 0
		categories[ calltype["category"] ]["count"] += calltype["count"]

	CallsByID = dict(( x.id, {
		'id' : x.id,
		'description': x.description,
		'event_num': x.event_num,
		'calltype': x.calltype.name,
		'calltype_desc': x.calltype.description,
		'calltype_category': x.calltype.category,
		#this is kind of a hack. but in oder for me to have the path to the icon work on dev and production
		#we are going to string replace our MEDIA_URL variable ala template style with the MEDIA_URL 
		#constant from our settings. and presto-chang-o we have our image paths in the DB work in production AND dev.
		'icon': x.calltype.icon.replace( "{{MEDIA_URL}}", settings.MEDIA_URL ),
		'response': x.response,
		'zip_code': x.zip_code,
		'call_time': x.call_time.strftime('%m-%d-%Y %H:%M:%S'),
		'beat': x.beat.name,
		'address': x.address,
		'lat': x.geom.y,
		'lng': x.geom.x,
		'geocoder': x.geocoder
		}) for x in calls )
	
	categories2 = []
	#make it readable for my template
	for category in categories:
		categories2.append( categories[category] )
	
	
	json = {
		'content' : render_to_string( 'calls/calls.html', { 'calls': calls } ),
		'categories': categories2,
		'details_content': render_to_string( 'calls/map_details.html', {
					'from_date': start, 
					'to_date': end, 
					'total_calls': len( CallsByID ),
					"radius": request.GET[ "radius" ], 
					"limit_results": request.GET[ "limit_results" ],
					"address": request.GET[ "address" ],
		 }),
		'CallsByID': CallsByID,
	}
	
	return HttpResponse( simplejson.dumps( json ) )
	
def list( request ):
	#start with our base object
	#this will pull in the last 24 hours worth of calls.
	#putting in geom__isnull cause we ONLY care about calls that have a a lat/lng
	calls = Call.objects.filter(call_time__gte=datetime.datetime.today() - datetime.timedelta(days=1), geom__isnull=False).order_by('-call_time')
	#going to try this. for some reason, there are a few calls that get geocoding WAY outside the city limits. so i'm going to do a search from downtown and limit the distance to 5 or 8 miles.
	# this will include the whole city but not give us our funky calls.
	P = Point( float( -93.292255 ), float(  37.208990 ) )
	calls = calls.filter( geom__distance_lt=( P, D( mi= float( 8 ) ) ) )
	calltypes = CallType.objects.filter(call__in=calls).values('category').annotate(count=Count('call')).distinct()
	categories = {}
	for calltype in calltypes:
		if calltype["category"] not in categories.keys():
			categories[ calltype["category"] ] = {}
			categories[ calltype["category"] ][ "name" ] = calltype["category"]
			categories[ calltype["category"] ][ "count" ] = 0
		categories[ calltype["category"] ]["count"] += calltype["count"]
	
	if "category" in request.GET.keys():
		if request.GET[ "category" ] != "all":
			#print "category != all"
			calls = calls.filter( calltype__category=request.GET[ "category" ])
	

	calls2 = calls.order_by('-call_time')
	end = calls2[0].call_time
	calls3 = calls.order_by('call_time')
	start = calls3[0].call_time

	CallsByID = dict(( x.id, {
		'description': x.description,
		'event_num': x.event_num,
		'calltype': x.calltype.name,
		'response': x.response,
		'zip_code': x.zip_code,
		'call_time': x.call_time.strftime('%m-%d-%Y %H:%M:%S'),
		'calltype_category': x.calltype.category,
		'calltype_desc': x.calltype.description,
		#this is kind of a hack. but in oder for me to have the path to the icon work on dev and production
		#we are going to string replace our MEDIA_URL variable ala template style with the MEDIA_URL 
		#constant from our settings. and presto-chang-o we have our image paths in the DB work in production AND dev.
		'icon': x.calltype.icon.replace( "{{MEDIA_URL}}", settings.MEDIA_URL ),
		'response': x.response,
		'beat': x.beat.name,
		'address': x.address,
		'lat': x.geom.y,
		'lng': x.geom.x,
		'geocoder': x.geocoder
		}) for x in calls[:100] )
	categories2 = []
	#make it readable for my template
	for category in categories:
		categories2.append( categories[category] )
	
	json = {
		'content' : render_to_string( 'calls/calls.html', { 'calls': calls } ),
		'categories': categories2,
		'details_content': render_to_string( 'calls/map_details.html', {'from_date': start, 'to_date': end, 'total_calls': len( CallsByID) }),
		'CallsByID': CallsByID,
		#'graph_string': graph_string,
	}
	
	return HttpResponse( simplejson.dumps( json ) )
	
def crimeline( request ):
	#this is kind of not clean. but basically we get a datetime object and then we include everything AFTER the beginning
	#and exclude everything AFTER the end ( which we get by using datetime.timedelta)
	now = datetime.datetime.today()
	if len(request.GET["start_time"]) == 4:
		start_hours = request.GET["start_time"][1:2]
	else:
		start_hours = request.GET["start_time"][1:3]
	
	if len(request.GET["end_time"]) == 4:
		end_hours = request.GET["end_time"][1:2]
	else:
		end_hours = request.GET["end_time"][1:3]
	
	
	start = now - datetime.timedelta( seconds = ( int( start_hours ) * 60 * 60 ) )
	#if end_time is 0 then we want to use now
	if int( request.GET["end_time"] ) == 0:
		end = now
	else:
		end = now - datetime.timedelta( seconds = ( int( end_hours ) * 60 * 60 ) ) 
	#also adding the geom__isnull = false to make sure we get no records without a geometry.
	calls = Call.objects.order_by('-call_time').filter(call_time__gte=start,geom__isnull=False).exclude(call_time__gte=end)
	#going to try this. for some reason, there are a few calls that get geocoding WAY outside the city limits. so i'm going to do a search from downtown and limit the distance to 5 or 8 miles.
	# this will include the whole city but not give us our funky calls.
	P = Point( float( -93.292255 ), float(  37.208990 ) )
	calls = calls.filter( geom__distance_lt=( P, D( mi= float( 8 ) ) ) )
	calltypes = CallType.objects.filter(call__in=calls).values('category').annotate(count=Count('call')).distinct()
	categories = {}
	for calltype in calltypes:
		if calltype["category"] not in categories.keys():
			categories[ calltype["category"] ] = {}
			categories[ calltype["category"] ][ "name" ] = calltype["category"]
			categories[ calltype["category"] ][ "count" ] = 0
		categories[ calltype["category"] ]["count"] += calltype["count"]
		
	CallsByID = dict(( x.id, {
		'description': x.description,
		'event_num': x.event_num,
		'calltype': x.calltype.name,
		'response': x.response,
		'zip_code': x.zip_code,
		'call_time': x.call_time.strftime('%m-%d-%Y %H:%M:%S'),
		'calltype_category': x.calltype.category,
		'calltype_desc': x.calltype.description,
		#this is kind of a hack. but in oder for me to have the path to the icon work on dev and production
		#we are going to string replace our MEDIA_URL variable ala template style with the MEDIA_URL 
		#constant from our settings. and presto-chang-o we have our image paths in the DB work in production AND dev.
		'icon': x.calltype.icon.replace( "{{MEDIA_URL}}", settings.MEDIA_URL ),
		'response': x.response,
		'beat': x.beat.name,
		'address': x.address,
		'lat': x.geom.y,
		'lng': x.geom.x,
		'geocoder': x.geocoder
		}) for x in calls )

	categories2 = []
	#make it readable for my template
	for category in categories:
		categories2.append( categories[category] )
	
	
	json = {
		'content' : render_to_string( 'calls/calls.html', { 'calls': calls } ),
		'categories': categories2,
		'from_date': start.strftime("%m-%d-%y %I:%M %p"), 
		'to_date': end.strftime("%m-%d-%y %I:%M %p"), 
		'total_calls': len( CallsByID),
		'details_content': render_to_string( 'calls/map_details.html', {'from_date': start, 'to_date': end, 'total_calls': len( CallsByID) }),
		'CallsByID': CallsByID,
	}
	
	return HttpResponse( simplejson.dumps( json ) )
	
@login_required
@user_passes_test(lambda u: u.is_staff)
def nightclub_calls( request ):
	if request.method == "POST":
		form = NightClubForm( request.POST )
		calls = Call.objects.filter(call_time__gte=form.data["begin_date"], call_time__lte=form.data["end_date"])
		clubs = [ "311 S PATTON", "307 PARK CENTRAL", "504 W COLLEGE","317 PARK CENTRAL","3626 S CAMPBELL","321 SOUTH","219 W OLIVE","2526 S CAMPBELL","312 SOUTH", "1773 S GLENSTONE" ]
		#q object to hold our searches
		q = Q()
		for club in clubs:
			#this will loop through our clubs and make queries for them
			tmp = Q( address__icontains=club)
			q |= tmp
		#and then filter our calls with the queries
		calls = calls.filter(q)
		#this will loop through the calls and stick in the nightclub into the call object
		for call in calls:
			if call.address == "311 S PATTON AVE" or call.address =="311 S PATTON":
				call.nightclub = "Zan Nightclub"
			elif call.address == "307 PARK CENTRAL EAST" or call.address == "307 PARK CENTRAL":
				call.nightclub = "Icon"
			elif call.address == "504 W COLLEGE ST" or call.address == "504 W COLLEGE":
				call.nightclub = "Rokbar"
			elif call.address == "317 PARK CENTRAL EAST" or call.address == "317 PARK CENTRAL":
				call.nightclub = "Tonic Ultralounge"
			elif call.address == "3626 S CAMPBELL AVE" or call.address == "3626 S CAMPBELL":
				call.nightclub = "Electric Cowboy"
			elif call.address == "321 SOUTH AVE" or call.address == "321 SOUTH":
				call.nightclub = "The Boogie/Bubbles"
			elif call.address == "219 W OLIVE ST" or call.address == "219 W OLIVE":
				call.nightclub = "Martha's Vineyard"
			elif call.address == "2526 S CAMPBELL AVE" or call.address == "2526 S CAMPBELL":
				call.nightclub = "Latin Vibe"
			elif call.address == "312 SOUTH AVE" or call.address == "312 SOUTH":
				call.nightclub = "Ernie Biggs' Piano Bar"
			elif call.address == "1773 S GLENSTONE AVE" or call.address == "1773 S GLENSTONE": 
				call.nightclub = "Midnight Rodeo"
	else:
		form = NightClubForm()
		calls = None
	return render_to_response( 'calls/nightclub.html', {'calls': calls, 'form': form }, context_instance=RequestContext(request) )
	
@login_required	
@user_passes_test( lambda u: u.is_staff )
def categories_summary( request ):
	#define today and yesterday
	today = datetime.datetime.today()
	yesterday = today - datetime.timedelta(days=1)
	#get all the calls that happened between yesterdy 4pm and today 4pm
	calls = Call.objects.filter( call_time__gte="%d-%d-%d 16:00:00" % ( yesterday.year,yesterday.month,yesterday.day ), call_time__lte="%d-%d-%d 16:00:00" % ( today.year,today.month,today.day))
	
	#get all the calltypes for those calls
	calltypes = CallType.objects.filter(call__in=calls).values('category').annotate(count=Count('call')).distinct()
	categories = {}
	#build a dict for them so i can get a count etc
	for calltype in calltypes:
		if calltype["category"] not in categories.keys():
			categories[ calltype["category"] ] = {}
			categories[ calltype["category"] ][ "name" ] = calltype["category"]
			categories[ calltype["category"] ][ "count" ] = 0
		categories[ calltype["category"] ]["count"] += calltype["count"]
	
	total = 0
	categories2 = []
	#make it readable for my template
	for category in categories:
		categories2.append( categories[category] )
		total += categories[ category ][ "count" ]

	
	return render_to_response( 'calls/categories_summary.html', {'categories': categories2, "total": total,"today": "%d-%d-%d" % (today.month,today.day,today.year), "yesterday":"%d-%d-%d" % (yesterday.month,yesterday.day,yesterday.year) }, context_instance=RequestContext(request) )

@login_required
@user_passes_test( lambda u: u.is_staff )
def reversepub_calls( request ):
	#post means form was submitted
	if request.method == "POST":
		#pass the post request to my Form
		form = ReversePubForm( request.POST )
		
		#first thing is we figure out how many days we are doing this for
		begin_date = form.data["begin_date"].split("-")
		begin_date = datetime.date(  int( begin_date[0] ) , int( begin_date[ 1 ] ) , int( begin_date[ 2 ] ) )
		end_date = form.data["end_date"].split("-")
		end_date = datetime.date( int( end_date[0] ) , int( end_date[ 1 ] ) , int( end_date[ 2 ] ) )
		
		
		#getting our zone before i loop through the days
		zone = ReversePubZone.objects.get( id = form.data[ "zone" ] )
		
		#getting all the calls between these dates and that the calltype is reversepub-able
		#and order them by call_time ascending
		calls = Call.objects.filter( call_time__range = ( begin_date, end_date ), calltype__reversepub = True ).order_by( 'call_time' )
		
		#and then seeing if the call geometory is covered by our zone geometry
		calls = calls.filter( geom__coveredby = zone.geom )
		
		for call in calls:
			#kind of an long chain here but using the address to block to give us the 2100 block of Whatever St.
			#cleaning the address up some and i'm doing a string replace of & to " & " - with spaces around it. 
			#to make it easier to read
			#also changing JRF to James River Fwy and US65 to US 65. and / - &
			call.pretty_address = address_to_block( clean_address( call.address.replace( "JRF", "James River Fwy").replace( "US65", "US 65") ) )
			#replacing & with and on this line so that clean_address doesn't capitalize the A in and
			call.pretty_address = call.pretty_address.replace( "&"," and " ).replace( "/"," and " ).replace( "Us 65", "US 65" )
			call.date = call.call_time.strftime( "%m-%d-%y")
	else:
		#display my form
		form = ReversePubForm()
		calls = None
	
	return render_to_response( 'calls/reversepub.html', {'calls': calls, 'form': form }, context_instance = RequestContext( request ) )

