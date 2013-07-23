from django.conf.urls.defaults import patterns,handler500,handler404,include,url

urlpatterns = patterns('trueozarks.views',
	url(r'trueozarks/$','index',name='trueozarks-index'),
	url(r'trueozarks/photos$','browse_photos',name='trueozarks-browse-photos'),
	url(r'trueozarks/tags$','browse_tags',name='trueozarks-browse-tags'),
	url(r'trueozarks/maps$','browse_maps',name='trueozarks-browse-maps'),
	url(r'trueozarks/profile/(?P<profile_id>\d+)/(?P<profile_name>.*)$','view_profile',name='trueozarks_profile'),
	url(r'trueozarks/tag/(?P<tag>.*)$','tag_detail',name='tag_detail'),
	url(r'trueozarks/login$','login_page',name='login_page'),
	url(r'trueozarks/contact$','contactform',name='contactform'),
	url(r'trueozarks/contact/success','contact_success',name="trueozarks_contact_success"),
	url(r'trueozarks/contact/error','contact_error',name="trueozarks_contact_error"),
	)

