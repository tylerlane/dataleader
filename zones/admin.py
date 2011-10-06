from django.contrib.gis import admin
from models import *



class SchoolsAdmin( admin.OSMGeoAdmin ):
	field = ( None, { "fields": ("facility" ) } ) 
	field = ( None, { "geom": ("geom" ) } )
	
	list_display = ( "facility","geom" )
	list_filter = ( "facility", )
	search_fields  = ("facility",)
	default_lon = 37.214367
	default_lat = -93.29313

	
class SchoolDistrictsAdmin( admin.OSMGeoAdmin ):
	field = ( None, { "fields": ( "name" ) } ) 
	list_display = ( "name", )
	list_filter = ( "name", )
	search_fields  = ("name",)
	default_lon = 37.214367
	default_lat = -93.29313
	
class CountiesAdmin( admin.OSMGeoAdmin ):
	field = ( None, { "fields": ( "countyname" ) } ) 
	list_display = ( "countyname","cnty_seat","pop_2000","co_class", )
	list_filter = ( "co_class","countyname" )
	search_fields  = ("countyname",)
	default_lon = 37.214367
	default_lat = -93.29313


class ZipCodesAdmin( admin.OSMGeoAdmin ):
	list_display = ( "zcta5ce", )
	search_fields = ( "zcta5ce", )
	default_lon = 37.214367
	default_lat = -93.29313


class ReversePubZoneAdmin( admin.OSMGeoAdmin ):
	list_display = ( 'name', )
	
admin.site.register( Schools, SchoolsAdmin )
admin.site.register( SchoolDistricts, SchoolDistrictsAdmin )
admin.site.register( Counties, CountiesAdmin )
admin.site.register( ZipCodes, ZipCodesAdmin )
admin.site.register( ReversePubZone, ReversePubZoneAdmin )