from django.conf.urls.defaults import *

urlpatterns = patterns('restaurants.views',
    url(r'^restaurants/$', 'index', name='restaurants-index' ),
    url(r'^restaurants/detail/(?P<restaurant_id>.*)$', 'detail', name='restaurant-detail' ),
    url(r'^restaurants/browse/(?P<letter>\#|.*)/(?P<page>\d+)/$', 'browse', name='restaurants-browse' ),
    #cuisines
    url(r'^restaurants/cuisines$', 'list_cuisines', name='list_cuisines'),
    url(r'^restaurants/cuisine/(?P<cuisine>.*)/(?P<page>\d+)$', 'list_restaurants_cuisine', name='list_restaurants_cuisine'),
    url(r'^restaurants/neighborhoods$', 'list_neighborhoods', name='list_neighborhoods'),
    url(r'^restaurants/neighborhood/(?P<neighborhood>.*)/(?P<page>\d+)/$', 'list_restaurants_neighborhood', name='list_restaurants_neighborhood'),
    url(r'^restaurants/search$', 'search', name='restaurants-search'),
    url(r'^restaurants/search/(?P<page>\d+)/$', 'search', name='restaurants-search-page' ),
    url(r'^restaurants/merge/(?P<letter>\#|.*)/(?P<page>\d+)/$', 'merge', name='restaurants-merge-page' ),
    url(r'^restaurants/confirm-merge', 'confirm_merge', name='restaurants-confirm-merge' ),
    url(r'^restaurants/final-merge', 'final_merge', name='restaurants-final-merge'),
    #inspections
    url(r'^restaurants/inspections', 'list_recent_inspections', name='list_recent_inspections'),
    #list attribute values
    url(r'^restaurants/attributes$', 'list_attributes', name='list_attributes'),
    url(r'^restaurants/attribute/(?P<attribute>.*)/(?P<value>.*)/(?P<page>\d+)/$','list_restaurants_attribute', name='list_restaurants_attribute'),
    url(r'^restaurants/attribute/(?P<attribute>.*)$', 'list_attribute_values', name='list_attribute_values'),
    #url to record votes
    url(r'^restaurants/record_rating','record_rating', name='record_rating'),
    #top rated
    url(r'^restaurants/toprated','display_top_rated', name='display_top_rated'),
    #mostviewed
    url(r'^restaurants/mostviewed','display_most_viewed', name='display_most_viewed'),
    #admin pages
    url(r'^restaurants/admin/new_restaurants/$','new_restaurants', name='new_restaurants'),
    url(r'^restaurants/admin/new_restaurants/(?P<page>\d+)/$','new_restaurants', name='new_restaurants_admin'),
    url(r'^restaurants/admin/updated_restaurants/$','restaurants_not_updated',name='restaurants_not_updated'),
    url(r'^restaurants/admin/updated_restaurants/(?P<page>\d+)$','restaurants_not_updated',name='restaurants_not_updated'),
    url(r'^restaurants/admin/mark_updated/(?P<restaurant>\d+)/(?P<to>\w+)/(?P<page>\d+)$','mark_restaurant_updated',name='mark_restaurant_updated'),
    )
