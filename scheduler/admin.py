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
	
	list_display = ('name','active',)


class ScheduleAdmin(admin.ModelAdmin):
	pass


admin.site.register(Position, PositionAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Schedule, ScheduleAdmin)

