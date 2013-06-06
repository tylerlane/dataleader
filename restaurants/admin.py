from django.contrib.gis import admin
from models import Restaurant, Inspection, Cuisine, Attribute, Neighborhood, Featured, Gallery, Pageview, Contest



class InspectionInline(admin.TabularInline):
    model = Inspection


class AttributeInline(admin.TabularInline):
    model = Attribute


class RestaurantAdmin(admin.OSMGeoAdmin):
    field = (None, {'fields': ('name')})
    field = (None, {'fields': ('address')})
    field = (None, {'fields': ('active')})
    field = (None, {'geom': ('geom')})
    list_display = ('name', 'address', 'city','active',)
    list_filter = ('active','cuisine','city',)
    default_lon = 37.214367
    default_lat = -93.29313
    order_by = ('name', 'address')
    search_fields = ('name', )
    #
    #inline for inspections
    #inlines = [ AttributeInline, InspectionInline, ]
    inlines = [ AttributeInline, ]
    def make_inactive(self, request, queryset):
        rows_updated = queryset.update(active=False)
        if rows_updated == 1:
            message_bit = "1 restaurant was"
        else:
            message_bit = "%s restaurants were" % rows_updated
        self.message_user(request, "%s successfully marked as inactive." % message_bit)
    make_inactive.short_description = "Mark selected restaurant(s) as inactive"
    actions = [make_inactive]
    

class InspectionAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'date', 'reinspection', )
    list_filter = ('critical', 'noncritical', 'reinspection', )


class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name', 'label', )


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value','restaurant', 'comma_delimited', )
    list_filter = ('name',)


class NeighborhoodAdmin(admin.OSMGeoAdmin):
    field = (None, {'fields': ('name')})
    field = (None, {'fields': ('active')})
    field = (None, {'geom': ('geom')})
    default_lon = 37.214367
    default_lat = -93.29313

class ContestAdmin(admin.ModelAdmin):
    list_display = ('name','email','time_init',)

class FeaturedAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'title', )


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'gallery_url', )


class PageviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'time_init', )




admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Featured, FeaturedAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Pageview, PageviewAdmin)
admin.site.register(Contest,ContestAdmin)