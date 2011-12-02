from django.contrib import admin
from django.core.urlresolvers import reverse
from models import Position,Banner,Schedule


class PositionAdmin(admin.ModelAdmin):
	pass


class ScheduleInlineAdmin(admin.TabularInline):
	model = Schedule


class BannerAdmin(admin.ModelAdmin):
	inlines = [
		ScheduleInlineAdmin,
	]
	list_filter = ( 'position', 'active',)
	list_display = ('name','active',)


class ScheduleAdmin(admin.ModelAdmin):
	#list_filter = ( 'banner__position', )
	list_display = ('banner', 'start_time','end_time',)


admin.site.register(Position, PositionAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Schedule, ScheduleAdmin)

