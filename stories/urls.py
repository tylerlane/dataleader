from django.conf.urls.defaults import *

urlpatterns = patterns('stories.views',
	url(r'^$','dataredirect'),
	url(r'favicon.ico$','faviconredirect'),
	url(r'crime$','landing_page',name='landing_page'),
	url(r'crime/$','landing_page',name='landing_page2'),
	url(r'infocenter$','infocenter_landingpage'),
	url(r'pageview/story/(?P<story_id>\d+)/(?P<headline>.*)$', 'story_pageview',name='story_pageview'),
	url(r'infocenter/pageviews$', 'list_pageviews',name='list_pageviews'),
	url(r'infocenter/pageviews/json$','list_pageviews_json', name='list_pageviews_json' ),
	url(r'infocenter/pageviews-(?P<big>\w+)$','list_pageviews',name='list_pageviews'),
	url(r'pageview/pageviews_widget$', 'pageviews_widget', name='pageviews_widget'),
	url(r'infocenter/stories/featured$','list_featured_stories',name='list_featured_stories'),
	url(r'stories/front_page_widget$','front_page_stories_widget', name='front_page_stories_widget'),
)
