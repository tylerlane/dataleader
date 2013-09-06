from models import Genre,Event,Age,Venue,Time,Photo
import datetime
from django.conf import settings
# from django.contrib.gis.geos import Point
# from django.contrib.gis.measure import D
from django.contrib.auth.decorators import login_required,user_passes_test
from django.db.models import Avg,Min,Max,Count,F,Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
import re
from django.utils import simplejson
from django.core import serializers


def listgenres(request):
	genres = Genre.objects.filter(active=True)
	# for genre in genres:
	# 	genre.app_layout = genre.app_layout.split(",")
	data = serializers.serialize('json', genres)
	return HttpResponse(data, mimetype='application/json')

def index(request):
	return HttpResponse("Things Index")

def events_by_genre(request,genre=None):
	if genre is not None:
		genre = Genre.objects.get(name=genre)
		tmp_events = []
		events = Event.objects.select_related().filter(genre=genre,active=True)
		#for event in events:
		#	event.start_time = Time.objects.filter(event=event).order_by("start_time")[0].start_time.strftime("%m/%d/%Y %I:%M")
		#	tmp_events.append(event)
		data = serializers.serialize('json',events)
		#data = simplejson.dumps(list(events))
		return HttpResponse(data,mimetype='application/json')

def event_detail(request,event_id):
	event = Event.objects.filter(id=event_id)
	ages = Age.objects.filter(event=event)
	times = Time.objects.filter(event=event)
	#event.venue = Venue.objects.get(venue=event.venue)
	photos = Photo.objects.filter(event=event)
	all_objects = list( event ) + list( ages ) + list( times ) + list( photos )
	data = serializers.serialize('json',all_objects)
	
	return HttpResponse(data,mimetype='application/json')

def event_times(request,event_id):
	event = Event.objects.filter(id=event_id)
	times = Time.objects.filter(event=event)
	data = serializers.serialize('json',times)

	return HttpResponse(data,mimetype='application/json')