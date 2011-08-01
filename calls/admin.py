from django.contrib.gis import admin
from models import *


class BeatAdmin( admin.OSMGeoAdmin ):
	field = ( None, { "fields": ("name" ) } ) 
	field = ( None, { "fields": ("jurisdiction" ) } )
	field = ( None, { "geom": ("geom" ) } )
	
	list_display = ( "name","jurisdiction","geom" )
	list_filter = ( "name", "jurisdiction" )
	default_lon = 37.214367
	default_lat = -93.29313
	
class JurisdictionAdmin( admin.ModelAdmin ):
	list_display =( "name","active","time_init", )

class CallTypeAdmin( admin.ModelAdmin ):
	list_display = ( "name", "description", "jurisdiction", "active","reversepub","time_init",)
	

class CallAdmin( admin.OSMGeoAdmin ):
	field = ( None, { "fields": ( "description" ) } ) 
	field = ( None, { "geom": ( "geom" ) } )
	date_hierarchy = "call_time"
	list_display = ( "description","call_time","event_num","response","report_num","beat","calltype","address","zip_code", )
	list_filter = ("response","calltype",)
	search_fields = ( "address", "event_num",)
	
	
admin.site.register( Beat, BeatAdmin )
admin.site.register( Jurisdiction, JurisdictionAdmin )
admin.site.register( CallType, CallTypeAdmin )
admin.site.register( Call, CallAdmin)

