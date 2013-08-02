from django.contrib.gis import admin
from models import Genre,Age,Venue,Time,Photo,Event

# class GenreInline(admin.TabularInline):
# 	model = Genre
	
# class AgeInline(admin.TabularInline):
# 	model = Age

# class TimeInline(admin.TabularInline):
# 	model = Time

class PhotoInline(admin.TabularInline):
	model = Photo

class VenueInline(admin.TabularInline):
	model = Venue

class EventAdmin(admin.ModelAdmin):
	list_display = ("name","description","active","venue",)
	list_filter = ("active",)
	#date_hierarchy = "time_init"
	#inlines = [PhotoInline,VenueInline,]


admin.site.register(Event,EventAdmin)
