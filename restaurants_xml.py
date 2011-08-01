from BeautifulSoup import BeautifulStoneSoup,Tag,NavigableString
soup = BeautifulStoneSoup( open( "/Users/tlane2/Desktop/metromix-export.xml").read(), markupMassage = False )
stuff = [ ]
items = soup.findAll('content_item')
for item in items:
  print "%s" % item.children["name"].contents

  lat = item.find( 'latitude')
  if lat is not None:
    lat = lat.contents
  lng = item.find( 'longitude')
  if lng is not None:
    lng = lng.contents
  print "lat: %s" % lat
  print "lng: %s " % lng
  attributes = item.findAll( 'attribute' )
  for attribute in attributes:
    name = attribute.find('name').contents
    if name not in stuff:
      stuff.append(name)

for foo in stuff:
  print foo



