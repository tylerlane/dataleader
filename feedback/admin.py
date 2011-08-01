from django.contrib import admin
from models import Feedback


class FeedbackAdmin( admin.ModelAdmin ):
  list_display = ('name','feedback_type','time_init')
	

admin.site.register( Feedback, FeedbackAdmin )
