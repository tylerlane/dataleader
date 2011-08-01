from django.conf.urls.defaults import *

urlpatterns = patterns('feedback.views',
	url(r'^feedback/$','index', name='feedback-index' ),
	url(r'^feedback/thanks$','thanks',name='feedback-thanks'),
    url(r'^feedback/error$','error',name='feedback-error'),
    )
