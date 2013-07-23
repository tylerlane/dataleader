from django.contrib.gis import admin
from models import Layout,Tag,Profile,Story,PullQuote,InfoBox,Photo
from django.forms import SelectMultiple
from django.db import models
class PullQuoteInline(admin.TabularInline):
	model = PullQuote

class InfoBoxInline(admin.TabularInline):
	model = InfoBox

class StoryInline(admin.TabularInline):
	model = Story

class TagInline(admin.StackedInline):
	model = Tag

class TagAdmin(admin.OSMGeoAdmin):
	field = (None,{'fields':('name')})
	field = (None,{'fields':('active')})
	field = (None,{'fields':('address')})
	field = (None,{'geom': ('geom')})
	list_display = ('name','active','address','geom',)
	list_filter = ('active',)
	default_lon = 37.214367
	default_lat = -93.29313
	order_by = ('name', 'active')
	search_fields = ('name', )

class PullQuoteAdmin(admin.ModelAdmin):
	list_display = ('profile','text','style','position','active',)
	list_filter = ('style','position','active',)
	search_fields = ('profile','text',)

class InfoBoxAdmin(admin.ModelAdmin):
	list_display = ('profile','headline','style','position','active',)
	list_filter = ('style','position','active',)
	search_fields = ('profile','text','headline',)

class StoryAdmin(admin.ModelAdmin):
	list_display = ('profile','headline','subheadline','byline',)
	# list_filter = ('profile__active',)
	order_by = ('profile', 'byline')
	search_fields = ('profile','headline','subheadline','text','byline', )
	# inlines = [PullQuoteInline,InfoBoxInline,]

class PhotoAdmin(admin.OSMGeoAdmin):
	field = (None,{'fields':('profile')})
	field = (None,{'fields':('picture')})
	field = (None,{'fields':('cutline')})
	field = (None,{'fields':('credit')})
	field = (None,{'fields':('position')})
	field = (None,{'fields':('order')})
	field = (None,{'fields':('in_story')})
	field = (None,{'fields':('in_gallery')})
	field = (None,{'geom': ('geom')})
	list_display = ('profile','picture','credit','cutline','position','order','in_story','in_gallery',)
	list_filter = ('credit','profile','in_story','in_gallery',)
	default_lon = 37.214367
	default_lat = -93.29313
	order_by = ('profile', 'byline')
	search_fields = ('profile','picture','credit','cutline' )

class PhotoInline(admin.TabularInline):
	model = Photo
	formfield_overrides = { models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'10'})}, }

class ProfileAdmin(admin.OSMGeoAdmin):
	field = (None,{'fields':('name')})
	field = (None,{'fields':('headline')})
	field = (None,{'fields':('summary')})
	field = (None,{'fields':('active')})
	field = (None,{'fields':('most_popular')})
	field = (None,{'geom': ('geom')})
	list_display = ('name','headline','summary','active','most_popular')
	list_filter = ('active','most_popular',)
	default_lon = 37.214367
	default_lat = -93.29313
	order_by = ('name', 'active','most_popular,')
	search_fields = ('name','summary', )
	formfield_overrides = { models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'12'})}, }

	inlines = [StoryInline,PullQuoteInline,InfoBoxInline,PhotoInline]


class LayoutAdmin(admin.ModelAdmin):
	list_display = ('name','active','template',)
	list_filter = ('active',)

admin.site.register(Photo,PhotoAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Story,StoryAdmin)
admin.site.register(PullQuote,PullQuoteAdmin)
admin.site.register(InfoBox,InfoBoxAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Layout,LayoutAdmin)