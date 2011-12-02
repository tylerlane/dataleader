from django.conf.urls.defaults import *

urlpatterns = patterns('feedback.views',
	url(r'^feedback/$','index', name='feedback-index' ),
	url(r'^feedback/thanks$','thanks',name='feedback-thanks'),
    url(r'^feedback/error$','error',name='feedback-error'),
    url(r'^feedback/worker$','worker_form',name='worker-form'),
    url(r'^feedback/worker/thanks$','worker_thanks',name='worker-thanks'),
    url(r'^feedback/worker/error$','worker_error', name='worker-error' ),
    url(r'^feedback/christmas$','christmas_form',name='christmas-form'),
    url(r'^feedback/christmas/thanks$','christmas_thanks',name='christmas-thanks'),
    url(r'^feedback/christmas/error$','christmas_error', name='christmas-error' ),
    
    )
