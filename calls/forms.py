from django import forms
from zones.models import ReversePubZone
import datetime

class NightClubForm( forms.Form ):
	begin_date = forms.DateField(initial=datetime.date.today() - datetime.timedelta(days=3),required=False)
	end_date = forms.DateField(initial=datetime.date.today() + datetime.timedelta(days=1), required=False)

class ReversePubForm( forms.Form ):
	begin_date = forms.DateField(initial=datetime.date.today() - datetime.timedelta(days=8),required=False)
	end_date = forms.DateField(initial=datetime.date.today() - datetime.timedelta(days=1), required=False)
	zone = forms.ModelChoiceField(queryset=ReversePubZone.objects.filter(active=True),required=True,empty_label=None)
	
	
	