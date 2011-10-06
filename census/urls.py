from django.conf.urls.defaults import *

urlpatterns = patterns('census.views',
	#regular urls
	url(r'^census/$','index', name='census-index' ),
	url(r'^census/(?P<state>\w+)$', 'list_counties', name='list_counties' ),
	url(r'^census/(?P<state>\w+)/county/(?P<county>.*[County|city|Parish]$)$', 'county_detail',name='county_detail' ),
	url(r'^census/(?P<state>\w+)/cities$','list_cities',name='list_cities'),
	url(r'^census/(?P<state>\w+)/cities/(?P<city>.*[city|town|CDP|village|city \(balance\)|borough]$)$','city_detail',name='city_detail'),
	url(r'^census/(?P<state>\w+)/detail$','state_detail',name='state_detail'),
	#embedded urls
	url(r'^census-(?P<embed>embed)/$','index', name='embed-census-index' ),
	url(r'^census-(?P<embed>embed)/(?P<state>\w+)$', 'list_counties', name='embed_list_counties' ),
	url(r'^census-(?P<embed>embed)/(?P<state>\w+)/county/(?P<county>.*[County|city|Parish]$)$', 'county_detail',name='embed_county_detail' ),
	url(r'^census-(?P<embed>embed)/(?P<state>\w+)/cities/$','list_cities',name='embed_list_cities'),
	url(r'^census-(?P<embed>embed)/(?P<state>\w+)/cities/(?P<city>.*[city|town|CDP|village|city \(balance\)|borough]$)$','city_detail',name='embed_city_detail'),
	url(r'^census-(?P<embed>embed)/(?P<state>\w+)/detail/$','state_detail', name='embed_state_detail'),
	)