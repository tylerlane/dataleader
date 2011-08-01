from django.conf.urls.defaults import *

urlpatterns = patterns('restaurants.views',
	url(r'^restaurants/$','index', name='restaurants-index' ),
    url(r'^restaurants/detail/(?P<restaurant_id>.*)$','detail',name='restaurant-detail' ),
   	url(r"restaurants/browse/(?P<letter>[A-Z])/(?P<page>\d+)/$","browse", name="restaurants-browse" ),
    url(r'^restaurants/search$','search',name='restaurants-search'),
   	url(r"^restaurants/search/(?P<page>\d+)/$","search", name="restaurants-search-page" ),
    url(r"^restaurants/confirm-merge","confirm_merge",name="restaurants-confirm-merge" ),
    url(r"^restaurants/final-merge","merge", name="restaurants-final-merge"),
    )

