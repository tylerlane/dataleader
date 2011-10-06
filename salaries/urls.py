from django.conf.urls.defaults import *

urlpatterns = patterns('salaries.views',
	url(r'^salaries/$', 'index',name='salaries-index'),
)