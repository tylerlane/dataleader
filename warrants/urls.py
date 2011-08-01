from django.conf.urls.defaults import *

urlpatterns = patterns("warrants.views",
	url(r"crime/warrants/$","browse", name="warrants-index" ),
	#this will give me the url of /warrants/browse/A/1
	url(r"crime/warrants/browse/(?P<letter>[A-Z])/(?P<page>\d+)/$","browse", name="warrants-browse" ),
	url(r"crime/warrants/search/$","search", name="warrants-search" ),
	url(r"crime/warrants/search/(?P<page>\d+)/$","search", name="warrants-search-page" ),
	url(r"crime/warrants/stats/$","stats", name="warrants-stats"),
	)