from django.conf.urls.defaults import *

urlpatterns = patterns('zones.views',
	url(r'^zones/$','index', name='zones-index' ),
	url(r'^zones/kml-output','kml_output',name='kml-output'),
	)