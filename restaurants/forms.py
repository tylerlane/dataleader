from django import forms
#from django.db.models import Avg,Min,Max,Count,F,Q
#from restaurants.models import Restaurant,Inspection


class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    address = forms.CharField(max_length=150, required=False)
    city = forms.CharField(max_length=100, required=False, label="City")
