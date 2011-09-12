from django.contrib.gis import admin
from models import Restaurant, Inspection, Cuisine, Attribute, Neighborhood, Featured,Gallery


class InspectionInline(admin.TabularInline):
    model = Inspection


class RestaurantAdmin(admin.OSMGeoAdmin):
    field = (None, {'fields': ('name')})
    field = (None, {'fields': ('address')})
    field = (None, {'geom': ('geom')})
    list_display = ('name', 'address', 'city')
    list_filter = ('city', 'cuisine', )
    default_lon = 37.214367
    default_lat = -93.29313
    order_by = ('name', 'address')
    search_fields = ('name', )
    #inline for inspections
    inlines = [ InspectionInline, ]


class InspectionAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'date', 'reinspection', )
    list_filter = ('critical', 'noncritical', 'reinspection', )


class CuisineAdmin(admin.ModelAdmin):
    list_dipaly = ('name', 'label', )


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value','restaurant', 'comma_delimited', )
    list_filter = ('name',)


class NeighborhoodAdmin(admin.OSMGeoAdmin):
    field = (None, {'fields': ('name')})
    field = (None, {'fields': ('active')})
    field = (None, {'geom': ('geom')})
    default_lon = 37.214367
    default_lat = -93.29313


class FeaturedAdmin(admin.ModelAdmin):
    list_display = ('restaurant','title', )


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('restaurant','gallery_url', )


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Featured, FeaturedAdmin)
admin.site.register(Gallery,GalleryAdmin)
