import csv
#setting my django environment
from django.core.management import setup_environ
import settings
setup_environ( settings )

from census.models import CountyData,StateData,TractData
from lib import bail

rows = csv.reader( open( "/Users/tlane2/Code/dataleader/data/AR/TractAR.csv" ) )

count = 0
for row in rows:
	#if count == 0:
		#print row
	
		#col_count = 0
		#for column in row:
		#	print col_count, column
		#	col_count +=1
	count += 1
	if count != 1:
		print count, row
		col_count = 0
		columns = [65,425,68,402,401,400,404,403,406,408,407,410,409,412,411,414,413,416,415,418,417,420,419,422,421,420,423,429,103,432,104,435,105,438,106,441,107,444,108,447,109,450,173,453,175,456,176]
		for column in row:
			if col_count in columns:
				row[ col_count ] = 0
			col_count = 0
		cd = TractData()
		#populating the data
		cd.tract_name = row[65]
		cd.state = 'AR'
		cd.pop2000 = row[425]
		cd.pop2010 = row[68]
		cd.total_sqmiles = row[402]
		cd.water_sqmiles = row[401]
		cd.land_sqmiles = row[400]
	
		#percentages now
		cd.pctwhite2000 = row[404]
		cd.popwhite2000 = row[429]
		cd.pctwhite2010 = row[403]
		cd.popwhite2010 = row[103]
		cd.pctblack2000 = row[406]
		cd.popblack2000 = row[432]  
		cd.pctblack2010 = row[405]
		cd.popblack2010 = row[104]  
		cd.pctamind2000 = row[408]
		cd.popamind2000 = row[435]  
		cd.pctamind2010 = row[407]
		cd.popamind2010 = row[105]  
		cd.pctasian2000 = row[410]
		cd.popasian2000 = row[438]  
		cd.pctasian2010 = row[409]
		cd.popasian2010 = row[106]  
		cd.pctnathaw2000 = row[412]
		cd.popnathaw2000 = row[441] 
		cd.pctnathaw2010 = row[411]
		cd.popnathaw2010 = row[107] 
		cd.pctother2000 = row[414]
		cd.popother2000 = row[444]  
		cd.pctother2010 = row[413]
		cd.popother2010 = row[108]  
		cd.pct2ormore2000 = row[416]
		cd.pop2ormore2000 = row[447] 
		cd.pct2ormore2010 = row[415]
		cd.pop2ormore2010 = row[109] 
		cd.pcthisp2000 = row[418] 
		cd.pophisp2000 = row[450]
		cd.pcthisp2010 = row[417] 
		cd.pophisp2010 = row[173]
		cd.pctnonhisp2000 = row[420] 
		cd.popnonhisp2000 = row[453]
		cd.pctnonhisp2010 = row[419]
		cd.popnonhisp2010 = row[175] 
		cd.pctwhitenonhisp2000 = row[422] 
		cd.popwhitenonhisp2000 = row[456]
		cd.pctwhitenonhisp2010 = row[421]
		cd.popwhitenonhisp2010 = row[176] 
		cd.dividx2000 = row[424]
		cd.dividx2010 = row[423]
	
		cd.save()
		print "saving row ", count
	
	
	