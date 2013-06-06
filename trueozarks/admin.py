from django.contrib.gis import admin
from models import Layout,Tag,Profile,Story,PullQuote,InfoBox,Photo

class PullQuoteInline(admin.TabularInline):
	model = PullQuote

class InfoBoxInline(admin.TabularInline):
	model = InfoBox

class StoryInline(admin.TabularInline):
	model = Story

class TagInline(admin.TabularInline):
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
	list_display = ('story','text','style','position','active',)
	list_filter = ('style','position','active',)
	search_fields = ('story','text',)

class InfoBoxAdmin(admin.ModelAdmin):
	list_display = ('story','headline','style','position','active',)
	list_filter = ('style','position','active',)
	search_fields = ('story','text','headline',)

class StoryAdmin(admin.OSMGeoAdmin):
	field = (None,{'fields':('profile__name')})
	field = (None,{'fields':('headline')})
	field = (None,{'fields':('byline')})
	field = (None,{'geom': ('geom')})
	list_display = ('profile__name','headline','byline','geom',)
	list_filter = ('active',)
	default_lon = 37.214367
	default_lat = -93.29313
	order_by = ('profile__name', 'byline')
	search_fields = ('profile__name','headline','subheadline','text','byline', )
	inlines = [PullQuoteInline,InfoBoxInline,]

class PhotoAdmin(admin.OSMGeoAdmin):
	field = (None,{'fields':('profile__name')})
	field = (None,{'fields':('picture')})
	field = (None,{'fields':('cutline')})
	field = (None,{'fields':('credit')})
	field = (None,{'geom': ('geom')})
	list_display = ('profile__name','picture','credit','cutline','geom',)
	list_filter = ('active','credit',)
	default_lon = 37.214367
	default_lat = -93.29313
	order_by = ('profile__name', 'byline')
	search_fields = ('profile__name','picture','credit','cutline' )

class PhotoInline(admin.TabularInline):
	model = Photo

class ProfileAdmin(admin.OSMGeoAdmin):
	field = (None,{'fields':('name')})
	field = (None,{'fields':('headline')})
	field = (None,{'fields':('summary')})
	field = (None,{'geom': ('geom')})
	list_display = ('name','headline','summary','geom',)
	list_filter = ('active',)
	default_lon = 37.214367
	default_lat = -93.29313
	order_by = ('name', 'active')
	search_fields = ('name','summary', )

	inlines = [StoryInline,PhotoInline]


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