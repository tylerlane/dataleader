#setting my django environment
from django.core.management import setup_environ
import settings
setup_environ( settings )
from django.contrib.gis import geos
from django.contrib.gis.measure import D

from restaurants.models import Restaurant,Cuisine,Attribute
#import datetime
#import time
from lib import bail
from BeautifulSoup import BeautifulStoneSoup
from calls.textutils import clean_address
from geopy import geocoders
from geopy.distance import distance as geopy_distance
#seeing which path to use.
import socket
if socket.gethostname() == "2155529.pubip.peer1.net":
    g = geocoders.Google('ABQIAAAA2JAd-KesRNeDJwroL49_CxTC4wGmoCeUv8j3n4Pev0Dsu3hwqxS_gg6u4S_FFZd8gO-pLGIZ4Ui7VQ')
else:
    g = geocoders.Google('ABQIAAAA2JAd-KesRNeDJwroL49_CxRMPgAshc9HvuksOF-1hbNeUnHu2RR3TUaykJvxoc7edBwXZYs044EM3w')

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
        #print photo
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
    hours = None
    #since multiple name tags are in a content_item, we grab all of them
    #and check the parent of them, if the parent is content_item then we have our name
    names = item.findAll('name')

    #list of possible custom fields
    attr_fields = ["alcohol","parking","noise_level","payment_method","worth_noting","smoking","wheelchair_access","atmosphere","dress_code",
            "meals_seaved","carry_out","reservations","average_entree_price","specialities","bar_style","music_style","games","cross_streets",
            "delivery","romance_factor","outdoor_seating","critics_rating", "average_drink_price","cleanliness","internet_access","facilities",
            "live_music","features","shopping_genre","museum_type","public_transportation","admission_price","audience","seating_capacity",
            "recreation_facilities","gallery_type","store_type","atm","restaurant_style","seating","shopping_price","food","dance_style",
            "attractions", "community", "boutique_type", "theatre_genre", "private parties"]
    #dict to store them
    attributes = {}
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
                #and stick them into a variable for now
                cuisine += value.contents[0] + u","
                if cuisine not in cuisine2:
                    cuisine2.append(value.contents[0])

            if cuisine[-1] == ",":
                cuisine = cuisine[0:-1]
        if foo.contents[0] == "hours":
            value = foo.nextSibling.find("comment")
            if value is not None:
                hours = value.contents[0]
            else:
                hours = None

        #now to loop throug our attribute keys and figure out how to put them into the db properly
        if foo.contents[0] in attr_fields:
            values = foo.nextSibling.findAll("value")
            if values is not None:
                #make a list inside our attributes
                attributes[foo.contents[0]] = []
                for value in values:
                    attributes[foo.contents[0]].append(str( value.contents[0] ) )

            else:
                comment = foo.nextSibling.find("comment").contents[0]
                if comment is not None:
                    attributes[foo.contents[0]].append(comment)



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
    if hours is not None:
        stuff["hours"] = hours
    else:
        stuff["hours"] = None
    stuff["lat"] = lat
    stuff["lng"] = lng

    #print stuff
    stuff["attributes"] = attributes
    restaurants.append( stuff )

    #print stuff
    #print "===========================\r\n"

found = 0
not_found = 0
count = 0
new_count = 0
for restaurant in restaurants:
    print str(restaurant["name"])
    count += 1
    #now lets try to update our restaurants
    try:
        temp_restaurants = Restaurant.objects.filter(name__iexact=str(restaurant["name"]))
        for temp_restaurant in temp_restaurants:
            if temp_restaurant.address is not None and restaurant["address"] is not None:
                print "Address-xml: %s | address-db: %s" % (restaurant["address"], temp_restaurant.address)
                if clean_address(temp_restaurant.address) == clean_address(restaurant["address"]):
                    temp_restaurant.zip_code = str(restaurant["zip_code"])[:10]
                    temp_restaurant.phone = str(restaurant["main_phone_number"])
                    temp_restaurant.long_description = str(restaurant["description"])
                    temp_restaurant.photo_url = str(restaurant["photo"])
                    if restaurant["hours"] is not None:
                        temp_restaurant.hours = str(restaurant["hours"])
                    temp_restaurant.save()
                    print "saving Restaurant: %s" % temp_restaurant.name
                    #now to do cuisines
                    #print "Cuisine: %s" % restaurant["cuisine2"]
                    if restaurant["cuisine2"] is not None:
                        for tmp_cuisine in restaurant["cuisine2"]:
                            try:
                                new_cuisine,created = Cuisine.objects.get_or_create(name=str(tmp_cuisine))
                                print "adding cuisine: %s to %s" % ( tmp_cuisine, temp_restaurant.name)
                                new_cuisine.label = str(tmp_cuisine)
                                new_cuisine.save()

                                #now we associate a cuisine with a restaurant
                                temp_restaurant.cuisine.add(new_cuisine)
                            except:
                                print bail()
                    #now lets save
                    print "saving Restaurant: %s" % temp_restaurant.name
                    temp_restaurant.save()

                    #now we work on adding our attributes
                    if restaurant["attributes"] is not None:
                        print "looping through attributes"
                        for key in restaurant["attributes"].keys():
                            if len(restaurant["attributes"][key]) > 1:
                                tmp_attr = ""
                                for var in restaurant["attributes"][key]:
                                    tmp_attr += var + ", "

                                comma_delimited = True
                                new_attribute,created = Attribute.objects.get_or_create( restaurant=temp_restaurant,name=str(key), value=str(tmp_attr), comma_delimited = True)
                                if created:
                                    new_attribute.save()
                                    print "Saving attribute: %s" % key
                            else:
                                if restaurant["attributes"][key] is not None:
                                    try:
                                        new_attribute,created = Attribute.objects.get_or_create( restaurant=temp_restaurant,name=str(key),value=str(restaurant["attributes"][key][0]), comma_delimited = False)
                                        if created:
                                            new_attribute.save()
                                            print "Saving attribute: %s" % key
                                    except IndexError:
                                        print "Empty attribute: %s" % key

                    found += 1
                else:
                    #if it doesn't have a geometery stored in the db.
                    #we pull one
                    if temp_restaurant.geom is None:
                        try:
                            place, ( lat, lng ) = g.geocode( temp_restaurant.address + " " + temp_restaurant.city + "," + temp_restaurant.state, exactly_one=True )
                            new_point =  geos.fromstr( 'POINT(' + str(lng)+ " " + str(lat) +')', srid = 4326)
                            temp_restaurant.geom = new_point
                            print "geocoding restaurant since it isn't tagged"
                            temp_restaurant.save()
                        except:
                            print "error geocoding or multiple places found"
                    #geocode the restaurant if the addresses don't match.
                    try:
                        place, ( lat, lng ) = g.geocode( restaurant["address"] + " " + restaurant["city"] + "," + restaurant["state"], exactly_one=True )
                        new_point = ( lat, lng )
                        temp_rest_point = (temp_restaurant.geom.y, temp_restaurant.geom.x)
                        d = geopy_distance( temp_rest_point, new_point )
                        new_point =  geos.fromstr( 'POINT(' + str(lng)+ " " + str(lat) +')', srid = 4326 )
                        #temp_restaurant.geom.transform(32610)
                        #new_point.transform(32610)

                        #distance = new_point.distance(temp_restaurant.geom)
                        #distance = D( distance).ft

                        print "Distance between addresses: %s miles" % str(d.miles)
                        if d.miles <= 0.1:
                            #if its less than 0.1 miles i'm going assume it is the same restaurant with the same name
                            temp_restaurant.name = str(restaurant["name"])
                            temp_restaurant.description = str(restaurant["description"])
                            temp_restaurant.address = str(restaurant["address"])
                            temp_restaurant.city = str(restaurant["city"])
                            temp_restaurant.state = str(restaurant["state"])
                            temp_restaurant.zip_code = str(restaurant["zip_code"])
                            temp_restaurant.photo_url = str(restaurant["photo"])

                            if restaurant["hours"] is not None:
                                temp_restaurant.hours = restaurant["hours"]

                            print "saving restaurant: %s" % temp_restaurant.name
                            temp_restaurant.save()
                            print "Cuisine: %s" % restaurant["cuisine2"]
                            if restaurant["cuisine2"] is not None:
                                for tmp_cuisine in restaurant["cuisine2"]:
                                    try:
                                        new_cuisine,created = Cuisine.objects.get_or_create(name=str(tmp_cuisine))
                                        print "adding cuisine: %s to %s" % ( tmp_cuisine, temp_restaurant.name)
                                        new_cuisine.label = str(tmp_cuisine)
                                        new_cuisine.save()

                                        #now we associate a cuisine with a restaurant
                                        temp_restaurant.cuisine.add(new_cuisine)
                                    except:
                                        print bail()
                            #now lets save
                            temp_restaurant.geom = new_point
                            print "saving Restaurant: %s" % temp_restaurant.name
                            temp_restaurant.save()
                            
                            #now we work on adding our attributes
                            if restaurant["attributes"] is not None:
                                print "looping through attributes"
                                for key in restaurant["attributes"].keys():
                                    if len(restaurant["attributes"][key]) > 1:
                                        tmp_attr = ""
                                        for var in restaurant["attributes"][key]:
                                            tmp_attr += var + ", "
                                        comma_delimited = True
                                        new_attribute,created = Attribute.objects.get_or_create( restaurant=temp_restaurant,name=str(key), value=str(tmp_attr), comma_delimited = True)
                                        if created:
                                            new_attribute.save()
                                            print "Saving attribute: %s" % key
                                    else:
                                        if restaurant["attributes"][key] is not None:
                                            try:
                                                new_attribute,created = Attribute.objects.get_or_create( restaurant=temp_restaurant,name=str(key),value=str(restaurant["attributes"][key][0]), comma_delimited = False)
                                                if created:
                                                    new_attribute.save()
                                                    print "Saving attribute: %s" % key
                                            except IndexError:
                                                print "Empty Attribute: %s" % key



                            found += 1
                            print "Name matches & address matches via geocode ", found
                    except:
                        print "error geocoding or multiple places found"
            else:
                print "No address!"
                #skip for now....
                not_found += 1

        if temp_restaurants is None or len( temp_restaurants ) < 1:
            print "Restaurant not found using Name", not_found
            #if restaurant not found then we create it
            #call our new function
            new_restaurant = Restaurant()
            new_restaurant.name = str(restaurant["name"])
            new_restaurant.address = str(restaurant["address"])
            new_restaurant.city = str(restaurant["city"])
            #new_restaurant.state = str(temp_restaurant["state"])
            #defaulting to MO
            new_restaurant.state = "MO"
            new_restaurant.phone = str(restaurant["main_phone_number"])
            new_restaurant.zip_code = str(restaurant["zip_code"])[:10]
            new_restaurant.description = str(restaurant["description"])
            new_restaurant.photo_url = str( restaurant["photo"])
            new_restaurant.hours = str(restaurant["hours"])
            print "saving Restaurant: %s" % new_restaurant.name
            new_restaurant.save()
            if restaurant["cuisine2"] is not None:
                for tmp_cuisine in restaurant["cuisine2"]:
                    try:
                        new_cuisine,created = Cuisine.objects.get_or_create(name=str(tmp_cuisine))
                        new_cuisine.label = str(tmp_cuisine)
                        new_cuisine.save()
                        #now we associate a cuisine with a restaurant
                        new_restaurant.cuisine.add(new_cuisine)
                    except:
                        print bail()
            #now lets save
            print "saving Restaurant: %s" % new_restaurant.name
            new_restaurant.save()
            #now we work on adding our attributes
            if restaurant["attributes"] is not None:
                print "looping through attributes"
                for key in restaurant["attributes"].keys():
                    if len(restaurant["attributes"][key]) > 1:
                        tmp_attr = ""
                        for var in restaurant["attributes"][key]:
                            tmp_attr += var + ", "
                        comma_delimited = True
                        new_attribute,created = Attribute.objects.get_or_create( restaurant=temp_restaurant,name=str(key), value=str(tmp_attr), comma_delimited = True)
                        if created:
                            new_attribute.save()
                            print "Saving attribute: %s" % key
                    else:
                        if restaurant["attributes"][key] is not None:
                            try:
                                new_attribute,created = Attribute.objects.get_or_create( restaurant=temp_restaurant,name=str(key),value=str(restaurant["attributes"][key][0]), comma_delimited = False)
                                if created:
                                    new_attribute.save()
                                    print "Saving attribute: %s" % key
                            except IndexError:
                                print "Empty Attribute: %s" % key


            #bump up our counter
            new_count +=1



    except:
        print bail()
        exit()
        print "some undefined error happened. help!!!!"


print "Restaurants:"
print "Found: %d" % found
print "Not Found: %d" % not_found
print "New Restaurants: %d" % new_count
print "Total Restaurants: %d" % count
