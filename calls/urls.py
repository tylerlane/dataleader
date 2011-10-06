from django.conf.urls.defaults import *

urlpatterns = patterns('calls.views',
	url(r'^crime/calls$','index', name='calls-index' ),
	url(r'^crime/calls/search$', 'search', name='calls-search' ),
	url(r'^crime/calls/list$', 'list',name='calls-list' ),
	url(r'^crime/calls/crimeline$','crimeline',name='calls-crimeline'),
	url(r'^infocenter/reversepub/calls/nightclubs$','nightclub_calls', name='nightclub_calls'),
	url(r'^infocenter/reversepub/calls/categories$','categories_summary',name='categories_summary'),
	url(r'^infocenter/reversepub/calls$','reversepub_calls', name='reversepub_calls')
	)