from django.contrib.gis import admin
from models import *


class RestaurantAdmin( admin.OSMGeoAdmin ):
  field = ( None, { "fields": ("name" ) } ) 
  field = ( None, { "fields": ("address" ) } )
  field = ( None, { "geom": ("geom" ) } )
  list_display = ( "name","address","city" )
  list_filter = ( "channel","city" )
  default_lon = 37.214367
  default_lat = -93.29313
  order_by = ("name", "address" )
  search_fields = ("name", )
class InspectionAdmin( admin.ModelAdmin ):
  list_display = ("restaurant","date","reinspection",)
  list_filter = ("critical","noncritical","reinspection",)
	
admin.site.register( Restaurant, RestaurantAdmin )
admin.site.register( Inspection, InspectionAdmin )

