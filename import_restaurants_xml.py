#setting my django environment
from django.core.management import setup_environ
import settings
setup_environ( settings )

from restaurants.models import Restaurant,Cuisine,Attribute
import datetime
import time
from lib import bail
from BeautifulSoup import BeautifulStoneSoup
from calls.textutils import *
soup = BeautifulStoneSoup(open("metromix-export.xml").read(), markupMassage = False, convertEntities="html")
items = soup.findAll('content_item')
restaurants = []
for item in items:
    #temp list to hold my vars
    stuff = {}
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
    cuisine2 = []
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
                if cuisine not in cuisine2:
                    cuisine2.append(value.contents[0])

            if cuisine[-1] == ",":
                cuisine = cuisine[0:-1]

    stuff["name"] = name
    stuff["address"] = address
    stuff["city"] = city
    stuff["state"] = state
    stuff["zip_code"] = zip_code
    stuff["main_phone_number"] = main_phone_number
    stuff["photo"] = photo
    stuff["description"] = description
    stuff["cuisine"] = cuisine
    stuff["cuisine2"] = cuisine2
    stuff["lat"] = lat
    stuff["lng"] = lng
    #print stuff
    restaurants.append( stuff )


found = 0
not_found = 0
for restaurant in restaurants:
    print restaurant["name"]
    #now lets try to update our restaurants
    try:
        temp_restaurants = Restaurant.objects.filter(name=str(restaurant["name"]))
        for temp_restaurant in temp_restaurants:
            if clean_address(temp_restaurant.address) == clean_address(restaurant["address"]):
                temp_restaurant.zip_code = str(restaurant["zip_code"])
                temp_restaurant.main_phone_number = str(restaurant["main_phone_number"])
                temp_restaurant.description = str(restaurant["description"])

                #now to do cuisines
                if restaurant["cuisine2"] is not None:
                    for tmp_cuisine in restaurant["cuisine2"]:
                        try:
                            new_cuisine,created = Cuisine.objects.get_or_create(name=str(tmp_cuisine))
                            new_cuisine.label = str(tmp_cuisine)
                            new_cuisine.save()

                            #now we associate a cuisine with a restaurant
                            temp_restaurant.cuisine.add(new_cuisine)
                        except:
                            print bail()
                #now lets save
                print "saving Restaurant: %s" % temp_restaurant.name
                temp_restaurant.save()
                found += 1
            else:
                not_found += 1
                print "Name matches but address doesn't ", not_found
                print "Address-xml | address-db = %s | %s" % (restaurant["address"], temp_restaurant.address)
    except Restaurant.DoesNotExist:
        not_found +=1
        print "Restaurant not found using Name", not_found
        #print bail()

print "Restaurants:"
print "Found: %d" % found
print "Not Found: %d" % not_found
