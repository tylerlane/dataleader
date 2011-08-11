from BeautifulSoup import BeautifulStoneSoup,Tag,NavigableString
soup = BeautifulStoneSoup( open( "metromix-export.xml").read(), markupMassage = False,convertEntities="html" )
stuff = [ ]
items = soup.findAll('content_item')
for item in items:
    if item.location is not None:
        if item.location.nextSibling.name == "name":
            print   u"Name = " + item.location.nextSibling.contents[0]
    elif item.description is not None:
        print u"Name = " + item.description.previousSibling.contents[0]
    elif item.main_phone_number is not None:
        print u"Name = " + item.main_phone_number.previousSibling.contents[0]
    elif item.address is not None:
        if item.address.previousSibling.name == "name":
            print u"Name = " + item.address.previousSibling.contents[0]
    else:
        stuff.append(item)
    lat = item.find( 'latitude')
    if lat is not None:
        lat = lat.contents
    lng = item.find( 'longitude')
    if lng is not None:
        lng = lng.contents
    print "lat: %s" % lat
    print "lng: %s " % lng
    #attributes = item.findAll( 'attribute' )
    #for attribute in attributes:
    #    name = attribute.find('name').contents
    #    if name not in stuff:
    #        stuff.append(name)

for foo in stuff:
    print foo



