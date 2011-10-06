# Create your views here.
import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from models import Position,Banner, Schedule
import random

#function to display banner ads
def display_banner( request, position=None ):
 	if position is None:
		#if no position has been set, then set it to "default" - may need to change this later
		position = "default"
		
	position = Position.objects.get( name__iexact = position )
	
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
		
	
	return render_to_response("scheduler/banner.html", {'banner': banner }, context_instance = RequestContext( request ) )
	
def display_banner_preview( request, banner ):
	banner_obj = Banner.objects.get( name__iexact = banner )
	return render_to_response("scheduler/banner.html", {'banner': banner_obj }, context_instance = RequestContext( request ) )
		
