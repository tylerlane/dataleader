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
    #address section
    #street
    if item.address.street_address is not None:
        address = item.address.street_address.contents[0]
    else:
        address = None
    #city
    if item.address.city is not None:
        city = item.address.city.contents[0]
    else:
        city = None
    #state
    if item.address.state is not None:
        state = item.address.state.contents[0]
    else:
        state = None
    #zipcode
    if item.address.zipcode is not None:
        zip_code = item.address.zipcode.contents[0]
    else:
        zip_code = None
    #photo url
    if item.multimedia is not None:
        photo = item.multimedia.image.url.contents[0]
    else:
        photo = None
    #phone number
    if item.main_phone_number is not None:
        main_phone_number = item.main_phone_number.contents[0]
    else:
        main_phone_number = None
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
    #var to hold cuisine
    cuisine = u""

    #since multiple name tags are in a content_item, we grab all of them
    #and check the parent of them, if the parent is content_item then we have our name
    names = item.findAll('name')

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
                cuisine += value.contents[0] + u","
                #new_cuisine = Cuisine(name=value.contents[0])
                #new_cuisine.label = value.contents[0]
                #new_cuisine.save()
                #print "Creating DB record for cuisine: %s" % value.contents[0]
                #and we'll stick them into our database.

            if cuisine[-1] == ",":
                cuisine = cuisine[0:-1]

    #cuisine section
    print u"name: %s" % name
    print u"address: %s" % address
    print u"city: %s" % city
    print u"state: %s" % state
    print u"zip_code: %s" % zip_code
    print u"main_phone_number: %s" % main_phone_number
    print u"photo: %s" % photo
    print u"description: %s" % description
    print u"cuisine: %s" %cuisine
    print u"lat:  %s" % lat
    print u"lng:  %s" % lng
    print "==========================\r\n\r\n"
