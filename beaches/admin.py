from django.contrib.gis import admin
from models import *

class BeachAdmin( admin.OSMGeoAdmin ):
	field = ( None, { "fields": ( "beachname", "sampletaken","results1","results2" ) } ) 
	field = ( None, { "geom": ( "geom" ) } )
	date_hierarchy = "sampletaken"
	default_lon = 37.214367
	default_lat = -93.29313
	map_width = 700
	map_height = 325
	search_fields = ( "beachname",)
	
admin.site.register( Beach, BeachAdmin )
