from django.contrib.gis import admin
from models import Genre,Age,Venue,Time,Photo,Event

# class GenreInline(admin.TabularInline):
# 	model = Genre
	
class AgeInline(admin.TabularInline):
 	model = Age

class TimeInline(admin.TabularInline):
 	model = Time

class PhotoInline(admin.TabularInline):
	model = Photo

class EventAdmin(admin.ModelAdmin):
	list_display = ("name","description","active","venue",)
	list_filter = ("active",)
	#date_hierarchy = "time_init"
	inlines = [PhotoInline,TimeInline ]#,AgeInline]

class GenreAdmin(admin.ModelAdmin):
	list_display = ("name","active","parent","app_layout",)
	list_filter = ( "active",)


class VenueAdmin(admin.ModelAdmin):
	list_display = ('name','address','active',)
	list_filer = ('active',)

class AgeAdmin(admin.ModelAdmin):
	list_display = ('name','age_min','age_max','active',)
	list_filter = ('active','age_min','age_max',)

class TimeAdmin(admin.ModelAdmin):
	list_display = ('start_time','end_time','active',)
	list_filter = ('active',)

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('picture','description','active',)
	list_filter = ('active',)

admin.site.register(Event,EventAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Venue,VenueAdmin)
admin.site.register(Age,AgeAdmin)
admin.site.register(Time,TimeAdmin)
admin.site.register(Photo,PhotoAdmin)
