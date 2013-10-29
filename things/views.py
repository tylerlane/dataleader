from models import Genre, Event, Age, Venue, Time, Photo
import datetime
from django.conf import settings
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Avg, Min, Max, Count, F, Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
import re
import json
from django.core import serializers


def listgenres(request):
	genres = Genre.objects.filter(active=True)
	# for genre in genres:
	# 	genre.app_layout = genre.app_layout.split(",")
	data = serializers.serialize('json', genres)
	return HttpResponse(data, mimetype='application/json')

def genre_by_id(request,genre_id=None):
	if genre_id is not None:
		genre = Genre.objects.get(id=genre_id)
		data = serializers.serialize('json',genre)
		return HttpResponse(data, mimetype='application/json',use_natural_keys=True)

def index(request):
	return HttpResponse("Things Index")

def events_by_genre(request, genre=None):
	if genre is not None:
		genre = Genre.objects.get(name=genre)
		temp_times = []
		events = Event.objects.select_related().filter(genre=genre, active=True,start_date__range=(datetime.date.today(), datetime.date.today() + datetime.timedelta(days=7))).order_by("start_date","start_time")[:20]
		# for event in events:
		# 	times = Time.objects.filter(event=event, active=True)
		# 	for time in times:
		# 		 foo = {"start_time": time.start_time, "end_time": time.end_time}
		# 		 temp_times.append(foo)
		# 	event.times = foo
		# for event in events:
		# 	event.start_time = Time.objects.filter(event=event).order_by("start_time")[0].start_time.strftime("%m/%d/%Y %I:%M")
		# 	tmp_events.append(event)
		data = serializers.serialize('json', events,use_natural_keys=True)
		# data = simplejson.dumps(list(events))
		return HttpResponse(data, mimetype='application/json')

def event_detail(request, event_id):
	event = Event.objects.filter(id=event_id)
	ages = Age.objects.filter(event=event)
	times = Time.objects.filter(event=event)
	# event.venue = Venue.objects.get(venue=event.venue)
	photos = Photo.objects.filter(event=event)
	all_objects = list(event) + list(ages) + list(times) + list(photos)
	data = serializers.serialize('json', all_objects)
	
	return HttpResponse(data, mimetype='application/json')

def event_times(request, event_id):
	event = Event.objects.filter(id=event_id)
	times = Time.objects.filter(event=event)
	data = serializers.serialize('json', times)

	return HttpResponse(data, mimetype='application/json')

def event_search(request, genre=None):
	events = Event.objects.select_related().filter(active=True)
	if genre is not None:
		events = events.filter(genre=Genre.objects.get(name=genre))
	if request.GET.has_key("when"):
		when = request.GET["when"].split("_")[1:]
		when = "_".join(when)
		start_time = None
		end_time   = None
		if when == "7_days":
			#code to filter by date
			start_date = datetime.date.today()
			end_date = start_date + datetime.timedelta(days=7)
		elif when == "tomorrow":
			start_date= datetime.date.today() + datetime.timedelta(days=1)
			end_date = start_date + datetime.timedelta(days=0)
		elif when == "today":
			start_date = datetime.date.today()
			end_date = datetime.date.today()
		elif when == "3_days":
			start_date = datetime.date.today()
			end_date = start_date + datetime.timedelta(days=3)

		events = events.filter(start_date__range=(start_date,end_date))
	if request.GET.has_key("time"):
		event_time = request.GET["time"].split("_")[1:]
		event_time = "_".join(event_time)
		if event_time == "morning":
			events = events.filter(start_time__range=('06:00','11:59'))
		elif event_time == "afternoon":
			events = events.filter(start_time__range=('12:00','17:59'))
		elif event_time == "evening":
			events = events.filter(start_time__range=('18:00','23:59'))
		# elif event_time == "anytime":
		# 	pass

	if request.GET.has_key("where"):
		where = request.GET["where"].split("_")[1:]
		where = "_".join(where)
		if request.GET.has_key("lng") and request.GET.has_key("lat"):
			# if we have Lat and lng and they aren't "null" then we set our point.
			P = Point(float(request.GET['lng']), float(request.GET['lat']))
			if where != "anywhere":
				if where == "half_mile":
					distance = 0.5
				elif where == "one_mile":
					distance = 1.0
				else:
					distance = 5.0
				events = events.filter( geom__distance_lte=( P, D( mi= distance) )).distance(P)
	if request.GET.has_key("name"):
		name_q = Q(name__icontains=request.GET["name"])
		description_q = Q(short_description__icontains=request.GET["name"])
		events = events.filter(name_q|description_q)
		events = events[:20]
	if len(events) == 0:
		if start_time is None:
			foo = {"where": where,"when":when,"event_time":event_time}
			# dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
		else:
			foo = {'start_time': start_time.isoformat(), 'end_time':end_time.isoformat(),"where": where,"when":when,"event_time":event_time,"lat": P.y,"lng":P.x,"query": str(events.query)}
			# dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
		data = json.dumps(foo)
	else:
		data = serializers.serialize('json', events,use_natural_keys=True)
	return HttpResponse(data, mimetype='application/json')



#@login_required	
#@user_passes_test(lambda u: u.is_staff)
def list_exports(request):
	genres = Genre.objects.filter(active=True)


	#return HttpResponse(str(genres))
	return render_to_response('things/exportSelect.html', {'list': genres}, context_instance=RequestContext(request))

def export(request, choice=None):
	if(choice != None):
		genre = Genre.objects.get(name=choice)
	else:
		return HttpResponse('Sorry, that is not a valid genre')


	events = Event.objects.select_related().filter(genre=genre, active=True).order_by("start_date","start_time")[:20]

	

	#return HttpResponse(str(stuff))
	return render_to_response('things/exportDisplay.html', {'events': events}, context_instance=RequestContext(request))