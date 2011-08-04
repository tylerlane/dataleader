#!/usr/bin/env python
#import csv
#setting my django environment
from django.core.management import setup_environ
import settings
setup_environ( settings )

from schools.models import School,District,AYPDetail,AYPSummary

schools = School.objects.all()
years = ['2006','2007', '2008', '2009', '2010', '2011']
detail_count = 0
summary_count = 0
for school in schools:
    for year in years:
        print "Creating Summary for %s - %s" % ( school, year)
        new_summary,created = AYPSummary.objects.get_or_create( school = school,  district=school.district, year = year )
        if created:
            new_summary.save()
            summary_count += 1

        print "Creating Detail for %s - %s" % ( school, year)
        new_detail,created = AYPDetail.objects.get_or_create( school = school, district = school.district , year = year )
        if created:
            new_detail.save()
            detail_count += 1

print "Created %d Detail Records" % detail_count
print "Created %d Summary Records" % summary_count

