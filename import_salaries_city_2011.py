import csv
#settings from django environment
import settings
setup_environ(settings)
from salaries.models import Organization,Person,Salary
from lib import bail

rows = csv.reader( open( "data/city_salary_2011.csv", "rU"), dialect="excel")

count = 0
for row in rows:
	if count != 0:
		print "%d %s" % (count, row)

		organization, org_created = Organization.objects.get_or_create(name="City of Springfield")
		if org_created is True:
			print "Created Organization for %s" % organization.name
			organization.save()

		print "%s" % row[0]
		name = row[0].split( "," )
		person,peep_created = Person.objects.get_or_create(name= name[1] + " " + name[0])
		if peep_created is True:
			#set the organization
			person.organization = organization
			person.title = row[2]
			if row[1] == "REGULAR FULLTIME":
				person.employment_type = "full_time"
			elif row[1] == "TEMP/SEASONAL":
				person.employment_type = "temp"
			elif row[1] == "CONTRACT":
				person.employment_type = "contract"
				

			

		