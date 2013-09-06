from django.conf.urls.defaults import patterns,handler500,handler404,include
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from trueozarks import views

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'', include('calls.urls')),
    (r'', include('warrants.urls')),
    (r'', include('stories.urls')),
    (r'', include('zones.urls')),
    #(r'', include( 'beaches.urls')),
    (r'', include('accounts.urls')),
    (r'', include('schools.urls')),
    #(r'', include( 'scheduler.urls')),
    (r'', include('census.urls')),
    (r'', include('feedback.urls')),
    (r'', include('restaurants.urls')),
    (r'', include('trueozarks.urls')),
    (r'', include('things.urls')),
    #dirty dirty hack but i have to do this to make the schools stuff serve properly
    #(r'schools/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #(r'(?P<path>crossdomain.xml)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'schools/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/opt/django/data.news-leader.com/dataleader/static'}),
    (r'(?P<path>crossdomain.xml)$', 'django.views.static.serve',{'document_root': '/opt/django/data.news-leader.com/dataleader/static'}),
)

handler500 = 'trueozarks.views.handler500'

if settings.DEBUG:
    #SET
    media_url = settings.MEDIA_URL[1:]
    #extend
    urlpatterns += patterns('',
    (r'^%s(?P<path>.*)$' % media_url, 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT } ),
    )
