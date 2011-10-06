from django.db import models

# Create your models here.
class District( models.Model ):
	name = models.CharField( max_length = 255 )
	active = models.BooleanField( default = True, blank = False )
	
	objects = models.Manager()
	
	def __unicode__(self ):
		return u'%s' % self.name


class School( models.Model ):
	SCHOOL_TYPE_CHOICES = ( 
			( 'elementary','Elementary School' ),
			( 'middle','Middle School' ),
			( 'high','High School' ),
			( 'other','Other' ),
		)
	
	name = models.CharField( max_length  = 255 )
	active = models.BooleanField( default = True, blank = False )
	district = models.ForeignKey( 'District' )
	school_type = models.CharField( max_length = 100, choices = SCHOOL_TYPE_CHOICES, blank = True, null = True )
	
	objects = models.Manager()
	
	def __unicode__( self ):
		return u'%s' % self.name
		
class AYPSummary( models.Model ):
	school = models.ForeignKey( 'School', blank = True, null = True )
	district = models.ForeignKey( 'District' )
	year = models.IntegerField( max_length = 4, help_text='Please enter the year in YYYY format' )
	comm_arts_status = models.NullBooleanField( 'Communication Arts Status' )
	math_status = models.NullBooleanField( 'Mathematics Status' )
	attendance_status = models.NullBooleanField( 'Attendance Status' )
	graduation_status = models.NullBooleanField( 'Graduation Status' )
	
	objects = models.Manager()
	
	def __unicode__( self ): 
		return u'%s - %s AYP Summary' % ( self.school.name, self.year )
	class Meta:
		verbose_name = "Adequate Yearly Progress - Summary"
		verbose_name_plural = "Adequate Yearly Progress - Summaries"


class AYPDetail( models.Model ):
	school = models.ForeignKey( 'School', blank = True, null = True )
	district = models.ForeignKey( 'District' )
	year = models.IntegerField( max_length = 4, help_text='Please enter the year in YYYY format' )
	#communication arts
	comm_school_total = models.FloatField( 'School Total', max_length = 5,blank = True, null = True )
	comm_asian_prof = models.FloatField( 'Asian/Pacific Islander Proficiency', max_length = 5, blank = True, null = True  )
	comm_black_prof = models.FloatField( 'Black Proficiency', max_length = 5, blank = True, null = True )
	comm_hispanic_prof = models.FloatField( 'Hispanic Proficiency', max_length = 5, blank = True, null = True )
	comm_indian_prof = models.FloatField( 'American Indian Proficiency', max_length = 5, blank = True, null = True )
	comm_white_prof = models.FloatField( 'White Proficiency', max_length = 5, blank = True, null = True )
	comm_other_prof = models.FloatField( 'Other/ Non-Response', max_length = 5, blank = True, null = True )
	comm_low_income_prof = models.FloatField( 'Low Income Proficiency', max_length = 5, blank = True, null = True )
	comm_special_ed_prof = models.FloatField( 'Special Education Proficiency', max_length = 5, blank = True, null = True )
	comm_low_english_prof = models.FloatField( 'Low English Proficiency', max_length = 5, blank = True, null = True )
	#mathematics
	math_school_total = models.FloatField( 'School Total', max_length = 5, blank = True, null = True )
	math_asian_prof = models.FloatField( 'Asian/Pacific Islander Proficiency', max_length = 5, blank = True, null = True  )
	math_black_prof = models.FloatField( 'Black Proficiency', max_length = 5, blank = True, null = True )
	math_hispanic_prof = models.FloatField( 'Hispanic Proficiency', max_length = 5, blank = True, null = True )
	math_indian_prof = models.FloatField( 'American Indian Proficiency', max_length = 5, blank = True, null = True )
	math_white_prof = models.FloatField( 'White Proficiency', max_length = 5, blank = True, null = True )
	math_other_prof = models.FloatField( 'Other/ Non-Response', max_length = 5, blank = True, null = True )
	math_low_income_prof = models.FloatField( 'Low Income Proficiency', max_length = 5, blank = True, null = True )
	math_special_ed_prof = models.FloatField( 'Special Education Proficiency', max_length = 5, blank = True, null = True )
	math_low_english_prof = models.FloatField( 'Low English Proficiency', max_length = 5, blank = True, null = True )
	#additional indicators
	attendance_pct = models.FloatField( 'Attendance Percentage', max_length = 5, blank = True, null = True )
	graduation_pct = models.FloatField( 'Graduation Percentage', max_length = 5, blank = True, null = True )
	
	objects = models.Manager()
	
	def __unicode__( self ):
		return u'%s - %s AYP Detail' % ( self.school.name, self.year )
		
	
	class Meta:
		verbose_name = "Adequate Yearly Progress - Detail"
		verbose_name_plural = "Adequate Yearly Progress - Details"