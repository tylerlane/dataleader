from django.contrib.gis import admin
from models import *


class StateDataAdmin( admin.ModelAdmin ):
	list_display = ( "state","pop2000","pop2010", )
	
class CountyDataAdmin( admin.ModelAdmin ):
	list_display = ( "county_name","state","pop2000","pop2010", )
	list_filter = ( "state","county_name", )
	search_fields = ( "county_name","state", )
	
	
class TractDataAdmin( admin.ModelAdmin ):
	pass
	
class CityDataAdmin( admin.ModelAdmin ):
	list_display = ( "city_name","pop2000","pop2010")
	list_filter = ( "state","city_name" )
	search_fields = ( "city_name","state", )


	
admin.site.register( StateData, StateDataAdmin )
admin.site.register( CountyData, CountyDataAdmin )
admin.site.register( TractData, TractDataAdmin )
admin.site.register( CityData, CityDataAdmin )

