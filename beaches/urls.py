from django.conf.urls.defaults import *

urlpatterns = patterns('beaches.views',
	url(r'^beaches$','index', name='beaches-index' ),
	)	