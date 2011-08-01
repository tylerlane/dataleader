#!/usr/bin/env python
import os
import sys
import socket

if socket.gethostname() == "2155529.pubip.peer1.net":
	sys.path.append('/opt/django/data.news-leader.com/')
else:
	sys.path.append('/Users/tlane2/Code/data/trunk')
	
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.contrib.gis.geos import fromstr
from django.conf import settings
from stories.models import Story,Keyword
import feedparser
import datetime


#okay got everything imported i need, so lets try pull our stories in from RSS
d = feedparser.parse( "http://www.news-leader.com/feeds/RSS16.xml")


print "%d Stories scraped from Crime RSS" % len( d[ "entries" ] )

#loop through our stories
for entry in d[ "entries" ]:
	try: 
		#seeing if the story is in the db already or not.
		story = Story.objects.get( id= entry.link.split("/")[-3] )
		print "Story %s already in the db" % entry.link.split("/")[-3]
	except:
		story = Story()
		print "Story %s not found. inserting into db" % entry.link.split("/")[-3]
		#now we need to get our story id from the url
		#we take the link from the entry. split it by / and then grab the 3rd item from the end
		story.id = entry.link.split("/")[-3]
		
	story.short_url = "http://www.news-leader.com/article/2010%s" % story.id
	story.long_url = entry.link
	story.active = True
	story.category = entry.link.split("/")[-4]
	story.headline = entry.title
	story.summary = entry.summary
	story.date_published = datetime.datetime( entry.updated_parsed[0], entry.updated_parsed[1], entry.updated_parsed[2], entry.updated_parsed[3], entry.updated_parsed[4], entry.updated_parsed[5] )

	print "saving story"
	story.save()
	
	#keyword section
	try:
		keyword = Keyword.objects.get(story_id=story, keyword="crime")
		print "keyword already exists"
	except:
		keyword = Keyword()
		print "inserting keyword"
		keyword.story = story
		keyword.keyword = "crime"
		keyword.save()
		