# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.db.models import Avg,Min,Max,Count,F,Q
from django.conf import settings

#model stuff
from models import Counties,SchoolDistricts,ZipCodes

def index( request ):
	return render_to_response( 'zones/kmltest.html', {
	},context_instance = RequestContext(request) )

def kml_output( request ):
	greene_county = Counties.objects.get( countyname__contains="Greene" )
	dallas_county = SchoolDistricts.objects.get(name__contains="Dallas County" )
 	zipcode = ZipCodes.objects.get( zcta5ce=65804 )

	return render_to_response( "zones/kml_output.html",{'zipcode': zipcode.geom.kml },mimetype="application/vnd.google-earth.kml+xml" )