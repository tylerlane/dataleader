from BeautifulSoup import BeautifulStoneSoup,Tag,NavigableString
soup = BeautifulStoneSoup(open("/Users/tlane2/Desktop/metromix-export.xml").read(), markupMassage=False)
stuff = [ ]
items = soup.findAll('content_item')
for item in items:
    try:
        name = u"%s" % item.children["name"].contents
        #description = u"%s" % item.children["description"].children["value"].contents

        print name
        #print description
    except:
        print "error. skipping record"


