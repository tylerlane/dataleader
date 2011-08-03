import csv
#setting my django environment
from django.core.management import setup_environ
import settings
setup_environ( settings )

from schools.models import School,District,AYPDetail,AYPSummary
from lib import bail

rows = csv.reader( open( "AYP_School_2011.csv","rU" ), dialect="excel" )

count = 0
for row in rows:
	if count != 0:
		#print "%d %s" % ( count, row )
		
		
		district,dist_created = District.objects.get_or_create( name = row[2] )
		if dist_created is True:
			print "Created District for %s " % row[2]
			district.save()
		#else:
		#	print "District Already made for %s" % row[2]
			
		school,school_created = School.objects.get_or_create( name = row[4],district = district )
		if school_created is True:
			print "Created School for %s in %s" % (row[4], row[2])
			school.save()
		#else:
		#	#print "School  already made for %s in %s" % ( row[4], row[2] )
		
		try:
			ayp_detail,detail_created = AYPDetail.objects.get_or_create( school = school, district = district, year = row[8] )
			ayp_summary,summary_created = AYPSummary.objects.get_or_create( school = school, district = district, year = row[8] )  
			if row[5] == "Communication Arts":
				if row[6] == "GT1YR_Race/Ethnicity":
					if row[7] == "White(not Hispanic)":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.comm_white_prof = row[19]
							print "Setting comm_white_prof = %s" % row[19]
					elif row[7] == "Black(not Hispanic)":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.comm_black_prof = row[19]
							print "Setting comm_black_prof = %s" % row[19]
					elif row[7] == "Amer. Indian or Alaska Native":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.comm_indian_prof = row[19]
							print "Setting comm_indian_prof = %s" % row[19]
					elif row[7] == "Asian/Pacific Islander":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.comm_asian_prof = row[19]
							print "Setting comm_asian_prof = %s" % row[19]
					elif row[7] == "Hispanic":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.comm_hispanic_prof = row[19]
							print "Setting comm_hispanic_prof = %s" % row[19]
				elif row[6] == "GT1YR_Special Programs":
					if row[7] == "IEP_student":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.comm_special_ed_prof = row[19]
							print "Setting comm_special_ed_prof = %s" % row[19]
					elif row[7] == "Map Free and Reduced Lunch":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.comm_low_income_prof = row[19]
							print "Setting comm_low_income_prof = %s" % row[19]
					elif row[7] == "LEP Students":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.comm_low_english_prof = row[19]
							print "Setting comm_low_english_prof = %s" % row[19]
				elif row[6] == "GT1YR_Total":
					if row[7] == "Total":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.comm_school_total = row[19]
							print "Setting comm_school_total = %s" % row[19]
							if row[23] == "Y":
								ayp_summary.comm_arts_status = True
							else:
								ayp_summary.comm_arts_status = False
							print "Setting summary.comm_arts_status to %s" % ayp_summary.comm_arts_status
						if row[29] != "" or row[29] != " " or row[29] is not None:
							ayp_detail.attendance_pct =  row[29]
							print "Setting attendance_pct = %s" % row[29]
						if row[32] != "" or row[32] != " " or row[32] is not None:
							ayp_detail.graduation_pct = row[32]
							print "Setting graduation_pct = %s" % row[32]
						
			elif row[5] == "Mathematics":
				if row[6] == "GT1YR_Race/Ethnicity":
					if row[7] == "White(not Hispanic)":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.math_white_prof = row[19]
							print "Setting math_white_prof = %s" % row[19]
					elif row[7] == "Black(not Hispanic)":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.math_black_prof = row[19]
							print "Setting math_black_prof = %s" % row[19]
					elif row[7] == "Amer. Indian or Alaska Native":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.math_indian_prof = row[19]
							print "Setting math_indian_prof = %s" % row[19]
					elif row[7] == "Asian/Pacific Islander":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.math_asian_prof = row[19]
							print "Setting math_asian_prof = %s" % row[19]
					elif row[7] == "Hispanic":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.math_hispanic_prof = row[19]
							print "Setting math_hispanic_prof = %s" % row[19]
				elif row[6] == "GT1YR_Special Programs":
					if row[7] == "IEP_student":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.math_special_ed_prof = row[19]
							print "Setting math_special_ed_prof = %s" % row[19]
					elif row[7] == "Map Free and Reduced Lunch":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.math_low_income_prof = row[19]
							print "Setting math_low_income_prof = %s" % row[19]
					elif row[7] == "LEP Students":
						if row[19] != "" or row[19] != " " or row[19] is not None:
							ayp_detail.math_low_english_prof = row[19]
							print "Setting math_low_english_prof = %s" % row[19]
				elif row[6] == "GT1YR_Total":
					if row[7] == "Total":
						if row[19] != " " or row[19] is not None:
							ayp_detail.math_school_total = row[19]
							print "Setting math_school_total = %s" % row[19]
							if row[23] == "Y":
								ayp_summary.math_status = True
							else:
								ayp_summary.math_status = False
							print "Setting summary.math_status to %s" % ayp_summary.math_status  
							if row[29] != "" or row[29] != " " or row[29] is not None:
								ayp_detail.attendance_pct =  row[29]
								print "Setting attendance_pct = %s" % row[29]
							if row[32] != "" or row[32] != " " or row[32] is not None:
								ayp_detail.graduation_pct = row[32]
								print "Setting graduation_pct = %s" % row[32]
			print "Updating AYP Detail for %s in %s for %s" % ( school, district, row[8] )
			print "Updating AYP SUmmary for %s in %s for %s" % ( school, district, row[8] )
			ayp_detail.save()
			ayp_summary.save()
		except:
			print 'There was an error on row %d' % count
			print bail()
			
			
		


		print "processing row %d" % count
	count += 1
