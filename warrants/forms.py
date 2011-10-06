from django import forms
from django.db.models import Avg,Min,Max,Count,F,Q
from warrants.models import Warrant,Court

class SearchForm(forms.Form):
	name = forms.CharField( max_length=100,required=False )
	age = forms.CharField( max_length=5,required=False )
	violation_desc = forms.CharField( max_length=100,required=False,label="Crime" )
	bond = forms.CharField( max_length=100,required=False )
	release_cond = forms.CharField( max_length=100,required=False, label="Release Condition" )
	court = forms.ModelChoiceField( queryset= Court.objects.all(), empty_label = "ALL", label = "Court System", required = False )
	#tried doing them dymanically but that didn't work. so i'll just set the options manually
	types = [('','ALL'),('Appearance','Appearance'), ('Capias','Capias'), ('Felony','Felony'), ('General','General'), ('Information','Information'), ('Infraction','Infraction'), ('Juvenile','Juvenile'), ('Misdemeanor','Misdemeanor'), ('Municipal','Municipal'), ('Order to show cause','Order to show cause'), ('Probable Cause Warrant','Probable Cause Warrant'), ('Probation and Parole','Probation and Parole'), ('Showcause','Showcause'), ('Traffic','Traffic'), ('Writ of body Attachment','Writ of body Attachment')]
	warrant_type = forms.ChoiceField( choices=types, label="Warrant Type",required=False )
