from django.conf.urls.defaults import *

urlpatterns = patterns("schools.views",
	url(r"schools/ayp$","display_ayp", name="display_ayp" ),
	url(r"schools/ayp/xml$", "ayp_xml", name="ayp_xml" ),
	url(r"schools/ayp/detail$", "get_schools", name="get_schools" ),
	url(r"schools/ayp/detail/(?P<district>.*)/(?P<school>.*)$", "get_school_ayp_xml", name="get_school_ayp_xml"),
	url(r"schools/ayp/detail/(?P<district>.*)$", "get_school_ayp_xml", name="get_school_ayp_xml2"),
)
