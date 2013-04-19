from django.contrib import admin
from models import CarsFeed

class CarsFeedAdmin( admin.ModelAdmin ):
	pass
	

admin.site.register( CarsFeed, CarsFeedAdmin )