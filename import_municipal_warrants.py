#/usr/bin/env python
from BeautifulSoup import BeautifulSoup
import urllib
import sys,os
import datetime
import time
import socket
#my library functions. put in a seperate file for ease
from lib import bail, email_message, log_me, get_sql_var
if socket.gethostname() == "2155529.pubip.peer1.net":
	sys.path.append('/opt/django/data.news-leader.com/')
else:
	sys.path.append('/Users/tlane2/Code/data/trunk')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from warrants.models import Warrant,Court


#dictionary of column names
columns = { 0: "name", 1: "age", 2: "warrant_type", 3:"violation_desc", 4:"bond", 5:"warrant_number", 6:"release_cond" }

letters = [ "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","W","Y","Z"]
#letters = [ "B" ]
#pull down the url
warrants = []
row_count = 0
for letter in letters:
	doc = urllib.urlopen( 'http://www.springfieldmo.gov/spd/Wanted/MunicipalWarrants/Default.aspx?linit=' + str( letter.upper() ) )
	print "pulling letter %s from website" % letter
	#parse the file to get an tree to mess with
	soup = BeautifulSoup( doc )
	#find all the tables
	tables = soup.findAll( 'table' )
	
	letter_row_count = 0
	for table in tables:
		#find the rows in the table
		trs = table.findAll( 'tr' )
		#loop through the rows
		for tr in trs:
			#find the colums in the row
			tds = tr.findAll( 'td' )
			#loop through the columns
			count = 0
			#dict to store our key/values
			warrant = {}
			#skipping the first row cause its the column headers
			if letter_row_count > 0:
				for td in tds:
					#HATE HATE HATE HATE that i have to do this but
					#they have some REALLY stupid column headers stuck in the table i need to ignore
					if td.find( text=True ) in [ "DFNAME", "AGE","WTYPTX","VILLD1","TKINFO","RELCON", "WRTBND" ]:
						pass
					else:	
						string = str( columns[ count ] ) + ": " + td.find( text=True )
						#print string
						warrant[ columns[ count ] ] = str( td.find( text=True )).replace("&AMP;", " & ")
						warrant[ columns[ count ] ] = str( td.find( text=True )).replace("&amp;", " & ")
						count += 1
				if warrant is not None:		
					warrants.append( warrant )
				#print warrant
			row_count += 1
			letter_row_count += 1
		
#okay now that we have everything built. now we can loop through everything and insert/update/delete
insert_count = 0
update_count = 0
court = Court.objects.get(id=2)
archive_count = 0
#going to pull down all of the existing warrants that are active.
existing_ids = []
existing_warrants = Warrant.objects.filter(active=True,court=court).values_list('id',flat=True)
for warrant in existing_warrants:
	existing_ids.append( warrant )
#print existing_warrants.keys()
print len( warrants ), "Warrants Parsed from the website"
for warrant in warrants:
	#stupid but apparently there's a row in there that has no nothing
	#print warrant
	if "warrant_number" not in warrant.keys():
		pass
	else:
		try:
			new_warrant = Warrant.objects.get( warrant_number__exact = str( warrant[ "warrant_number" ]), court=court,age=int(warrant["age"]),warrant_type=str(warrant["warrant_type"]),violation_desc=str(warrant["violation_desc"]),bond=str(warrant["bond"]),release_cond=str(warrant["release_cond"]),active=True )
			#print new_warrant
			print "FOUND! Warrant %s already exists" % warrant[ "warrant_number" ]
			update_count += 1
			new_warrant.name = str(warrant[ "name" ])
			new_warrant.age  =  int( warrant[ "age" ] )
			new_warrant.warrant_type = str( warrant[ "warrant_type" ] )
			new_warrant.violation_desc = str( warrant[ "violation_desc" ] )
			new_warrant.warrant_number = str( warrant[ "warrant_number" ] )
			new_warrant.bond = str( warrant[ "bond" ] )
			new_warrant.release_cond = str( warrant["release_cond" ] )
			new_warrant.active = True
			new_warrant.court = court
			new_warrant.time_init = datetime.datetime.now()
			new_warrant.save()


			#remove the warrant from our existing warrants list if its in the db
			try:
				existing_ids.remove( new_warrant.id )
			except:
				print "ERROR! removing id %s" % new_warrant.id

		except Warrant.DoesNotExist:
			#print "No record found for %s" % warrant[ "warrant_number" ]
			new_warrant = Warrant()
			new_warrant.name = str(warrant[ "name" ])
			new_warrant.age  =  int( warrant[ "age" ] )
			new_warrant.warrant_type = str( warrant[ "warrant_type" ] )
			new_warrant.violation_desc = str( warrant[ "violation_desc" ] )
			new_warrant.warrant_number = str( warrant[ "warrant_number" ] )
			new_warrant.bond = str( warrant[ "bond" ] )
			new_warrant.release_cond = str( warrant["release_cond" ] )
			new_warrant.active = True
			new_warrant.court = court
			new_warrant.time_init = datetime.datetime.now()
			new_warrant.save()
			print "INSERTED! %s " % warrant["warrant_number"]
			insert_count += 1
			
#archiving
for existing_id in existing_ids:
	warrant = Warrant.objects.get( id=existing_id)
	warrant.active = False
	warrant.time_finished = datetime.datetime.now()
	warrant.save()
	archive_count += 1
	print "Archiving %s " % warrant.warrant_number
		
print row_count, "Total Rows parsed from website"
print insert_count, "Inserted Records"
print update_count, "Updated Records"
print archive_count, "Archived Records"