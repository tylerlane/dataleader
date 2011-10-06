from django.contrib import admin
from models import Warrant,Court


class WarrantAdmin( admin.ModelAdmin ):
	list_display = ( "name", "age", "warrant_type", "court","warrant_number", "active", "time_init", )
	date_hierarchy = "time_init"
	list_filter = ( "warrant_type","court","active" )
	search_fields = ( "name", )
	
class CourtAdmin( admin.ModelAdmin ):
	list_display = ( "name","description","active", )
	
admin.site.register( Warrant, WarrantAdmin )
admin.site.register( Court, CourtAdmin )