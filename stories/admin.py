from django.contrib.gis import admin
from models import Story,Pageview,Keyword
from django.contrib import databrowse


class StoryAdmin( admin.ModelAdmin ):
	list_display = ( "headline","date_published","active" )
	search_fields = ("headline",)
	list_filter = ( "date_published", )
	date_hierarchy = "date_published"
	ordering = ( "-date_published", )
	
class PageviewAdmin( admin.ModelAdmin ):
	list_display = ( "story", "time_init",)

class KeywordAdmin( admin.ModelAdmin ):
	list_display = ( "story", "keyword",)


	
admin.site.register( Story, StoryAdmin )
admin.site.register( Pageview, PageviewAdmin )
admin.site.register( Keyword, KeywordAdmin )
