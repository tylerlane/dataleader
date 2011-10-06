from django.conf.urls.defaults import *

urlpatterns = patterns('',
						(r'^accounts/login/$', 
						'django.contrib.auth.views.login', 
						{'template_name': 'accounts/login.html'}),

						(r'^accounts/logout/$', 
						'django.contrib.auth.views.logout', 
						{'template_name': 'accounts/logged_out.html'}),

						(r'^accounts/password_change/$', 
						'django.contrib.auth.views.password_change', 
						{'template_name': 'accounts/password_change_form.html'}),

						(r'^accounts/password_change/done/$', 
						'django.contrib.auth.views.password_change_done', 
						{'template_name': 'accounts/password_change_done.html'}),

						(r'^accounts/password_reset/$', 
						'django.contrib.auth.views.password_reset', 
						{'template_name': 'accounts/password_reset_form.html',
						 'email_template_name': 'accounts/password_reset_email.html'}),

						(r'^accounts/password_reset/done/$', 
						'django.contrib.auth.views.password_reset_done', 
						{'template_name': 'accounts/password_reset_done.html'}),

						(r'^accounts/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
						'django.contrib.auth.views.password_reset_confirm', 
						{'template_name': 'accounts/password_reset_confirm.html'}),

						(r'^accounts/reset/done/$', 
						'django.contrib.auth.views.password_reset_complete', 
						{'template_name': 'accounts/password_reset_complete.html'}),
					)