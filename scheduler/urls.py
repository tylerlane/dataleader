from django.conf.urls.defaults import *

urlpatterns = patterns("scheduler.views",
	url(r"scheduler/preview/(?P<banner>.*)$","display_banner_preview", name="display_banner_preview" ),
	url(r"scheduler/(?P<position>.*)$","display_banner", name="display_banner" ),
	)