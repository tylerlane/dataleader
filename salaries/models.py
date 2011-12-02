from django.db import models

EMPLOYMENT_CHOICES = (
	('fulltime', 'Full-Time'),
	('parttime', 'Part-Time'),
	('contract', 'Contract'),
	('freelance', 'Freelance'),
	('temp', 'Temp/Seasonal'),
	('other', 'other'),
)

COMPENSATION_CHOICES = (
	('hourly', 'HOURLY'),
	('salary', 'SALARY'),
	('other', 'OTHER'),
)


class Organization(models.Model):
	name = models.CharField(max_length=100)
	active = models.BooleanField(default=True)

	objects = models.Manager()

	def __unicode__(self):
		return u"%s" % self.name


# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=200)
	#linking to an organization like Springfield City/County etc
	organization = models.ForeignKey('Organization')
	title = models.CharField(max_length=200)
	hire_date = models.DateTimeField("Hire Date", auto_now=False, 
		auto_now_add=False)
	#full/part time or contract etc
	employment_type = models.CharField(choices=EMPLOYMENT_CHOICES,
		max_length=25, null=True, blank=True)

	#whatever department the person is.
	department = models.CharField(max_length=200, null=True,
		blank=True)
	
	objects = models.Manager()

	def __unicode__(self):
		return u"%s" % self.name


class Salary(models.Model):
	person = models.ForeignKey('Person')
	year = models.IntegerField()
	#whatever financial compensation we get.
	compensation = models.IntegerField()
	#type to let us know if its hourly/salary/other
	compensation_type = models.CharField(choices=COMPENSATION_CHOICES,
		max_length=25)

	objects = models.Manager()

	def __unicode__(self):
		return u"%s - %d" % (self.person.name, self.year)