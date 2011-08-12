#setting my django environment
from django.core.management import setup_environ
import settings
setup_environ( settings )

from restaurants.models import Restaurant,Cuisine,Attribute
import datetime
import time
from BeautifulSoup import BeautifulStoneSoup
soup = BeautifulStoneSoup(open("metromix-export.xml").read(), markupMassage = False, convertEntities="html")
stuff = [ ]
items = soup.findAll('content_item')
for item in items:
    #since multiple name tags are in a content_item, we grab all of them
    #and check the parent of them, if the parent is content_item then we have our name
    names = item.findAll('name')
    cuisine2 = u""
    for foo in names:
        if foo.parent.name == "content_item":
            name = foo.contents[0]
        #cuisine section
        #check to see if its cuisine
        if foo.contents[0] == "cuisine":
            #then get all of the values for it
            values = foo.nextSibling.findAll("value")
            #loop through the values
            for value in values:
                created = None
                #and stick them into a variable for now
                cuisine2 += value.contents[0] + u","
                #and we'll stick them into our database.
                cuisine = Cuisine.objects.get(name=value.contents[0])
                if cuisine is None:
                    new_cuisine = Cuisine(name=value.contents[0])
                    new_cuisine.label = value.contents[0]
                    new_cuisine.save()
                    print "Created a new cuisine in DB: %s" % new_cuisine.name

            #if cuisine[-1] == ",":
            #    cuisine = cuisine[0:-1]
    #get the lat/lng
    lat = item.find('latitude')
    if lat is not None:
        lat = lat.contents[0]
    lng = item.find('longitude')
    if lng is not None:
        lng = lng.contents[0]
    #description section
    if item.description is not None:
        description = item.description.value.contents[0]
    else:
        description = None
    #cuisine section
    print u"name: %s" % name
    print u"description: %s" % description
    print u"cuisine: %s" %cuisine2
    print u"lat:  %s" % lat
    print u"lng:  %s" % lng

