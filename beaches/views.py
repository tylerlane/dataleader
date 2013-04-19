from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.template import RequestContext
from django.db.models import Avg,Min,Max,Count,F,Q
from models import Beach


def index( request ):
	base_url = "http://maps.google.com/maps/api/staticmap?"
	center = "Buffalo, MO"
	zoom = 8
	height = 480
	width = 480
	sensor = "false"
	
	#http://maps.google.com/maps/api/staticmap?center=Williamsburg,Brooklyn,NY&zoom=13&size=400x400&markers=color:blue|label:S|11211|11206|11222&sensor=true_or_false
	image = base_url + "center=" + center
	image += "&zoom=" + str( zoom )
	image += "&size=" + str( height ) + "x" + str( width )
	image += "&sensor=" + sensor

	beaches = Beach.objects.all()
	for beach in beaches:
			if beach.openclosed == "N":
				image += "&markers=color:blue"
			elif beach.openclosed == "B":	
				image += "&markers=color:yellow"
			elif beach.openclosed == "C":
				image += "&markers=color:red"
			elif beach.openclosed == "O":
				image += "&markers=color:green"
			image += "|" + str( beach.geom.y ) + "," + str( beach.geom.x )
	
	return render_to_response( "beaches/index.html", {"image": image } )
	