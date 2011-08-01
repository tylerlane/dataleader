from django.contrib import admin
from django.core.urlresolvers import reverse
from models import Position,Banner,Schedule

class PositionAdmin( admin.ModelAdmin ):
	pass

class ScheduleInlineAdmin( admin.TabularInline ):
	model = Schedule

class BannerAdmin( admin.ModelAdmin ):
	inlines = [
		ScheduleInlineAdmin,
	]
	
	def link( self,object ):
		return "<a href=\"%s\" target=\"_blank\">%s - Preview Link</a>" % ( reverse('display_banner_preview', args = ( object.name, ) ), object.name )
	
	link.allow_tags = True
	link.short_description = "Preview"
	
	list_display = ('name','active','link',)

class ScheduleAdmin( admin.ModelAdmin ):
	pass
	

admin.site.register( Position,PositionAdmin )
admin.site.register( Banner, BannerAdmin )
admin.site.register( Schedule, ScheduleAdmin )

