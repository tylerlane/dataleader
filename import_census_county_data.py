import csv
#setting my django environment
from django.core.management import setup_environ
import settings
setup_environ( settings )

from census.models import CountyData,StateData,TractData
from lib import bail

rows = csv.reader( open( "data/DC/CountyDC.csv" ) )

count = 0
for row in rows:
	#if count == 0:
	#	#print row
	#	col_count = 0
	#	for column in row:
	#		#print col_count, column
	#		col_count +=1
	count += 1
	if count != 1:
		#print count, row
		
		cd,created = CountyData.objects.get_or_create(county_name = row[65], state= 'DC')
		#populating the data
		#cd.county_name = row[65]
		#cd.state = 'AL'
		try:
			cd.pop2000 = row[425]
			cd.pop2010 = row[68]
			cd.total_sqmiles = row[402]
			cd.water_sqmiles = row[401]
			cd.land_sqmiles = row[400]
			print "saving the pop and sqmiles"
			cd.save()
		except:
			print "error on saving the pop and sqmiles"
		
		#percentages now
		try:
			cd.pctwhite2000 = row[404]
			cd.popwhite2000 = row[429]
			cd.pctwhite2010 = row[403]
			cd.popwhite2010 = row[103]
			print "saving the white 2000/2010 stats"
			cd.save()
		except:
			print "error with white 2000/2010 stats"
		try:
			cd.pctblack2000 = row[406]
			cd.popblack2000 = row[432]  
			cd.pctblack2010 = row[405]
			cd.popblack2010 = row[104]  
			print "saving black 2000/2010 stats"
			cd.save()
		except:
			print "error with black stats"
		try:
			cd.pctamind2000 = row[408]
			cd.popamind2000 = row[435]  
			cd.pctamind2010 = row[407]
			cd.popamind2010 = row[105]  
			print "saving american indian stats"
			cd.save()
		except:
			print "error with american indian stats"
		try:
			cd.pctasian2000 = row[410]
			cd.popasian2000 = row[438]  
			cd.pctasian2010 = row[409]
			cd.popasian2010 = row[106]  
			print "saving asian stats"
			cd.save()
		except:
			print "error with asian stats"
		try:
			cd.pctnathaw2000 = row[412]
			cd.popnathaw2000 = row[441] 
			cd.pctnathaw2010 = row[411]
			cd.popnathaw2010 = row[107] 
			print "saving hawaiian stats"
			cd.save()
		except:
			print "error saving hawaiian stats"
		try:
			cd.pctother2000 = row[414]
			cd.popother2000 = row[444]  
			cd.pctother2010 = row[413]
			cd.popother2010 = row[108]  
			print "saving other stats"
			cd.save()
		except:
			print "error saving other stats"
		try:
			cd.pct2ormore2000 = row[416]
			cd.pop2ormore2000 = row[447] 
			cd.pct2ormore2010 = row[415]
			cd.pop2ormore2010 = row[109] 
			print "saving 2 or more stats"
			cd.save()
		except:
			print "error with 2 or more stats"
		try:
			cd.pcthisp2000 = row[418] 
			cd.pophisp2000 = row[450]
			cd.pcthisp2010 = row[417] 
			cd.pophisp2010 = row[173]
			print "saving hispanic stats"
			cd.save()
		except:
			print "error with hispanic stats"
		try:
			cd.pctnonhisp2000 = row[420] 
			cd.popnonhisp2000 = row[453]
			cd.pctnonhisp2010 = row[419]
			cd.popnonhisp2010 = row[175] 
			print "saving nonhispanic stats"
			cd.save()
		except:
			print "error nonhispanic stats"
		try:
			cd.pctwhitenonhisp2000 = row[422] 
			cd.popwhitenonhisp2000 = row[456]
			cd.pctwhitenonhisp2010 = row[421]
			cd.popwhitenonhisp2010 = row[176] 
			print "saving white nonhispanic stats"
			cd.save()
		except:
			print "error with white nonhispanic stats"
		try:
			cd.dividx2000 = row[424]
			cd.dividx2010 = row[423]
			print "saving diversity index"
			cd.save()
		except:
			print "error with diversity index"
			
		print "saving row ", count
	
	
	
