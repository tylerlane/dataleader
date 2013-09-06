from django.conf.urls.defaults import *

urlpatterns = patterns('things.views',
	url(r'things/genres$','listgenres',name='listgenres'),
	url(r'things/$','listgenres',name='listgenres2'),
	url(r'things/genre/(?P<genre>.*)$','events_by_genre',name='events_by_genre'),
	url(r'things/event/times/(?P<event_id>.*)$','event_times',name='event_times'),
	url(r'things/event/(?P<event_id>.*)$','event_detail',name='event_detail'),
	#url(r'things/test$','test',name='things-test'),
)