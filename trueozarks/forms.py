from django import forms
from django.contrib.localflavor.us.forms import USStateField,USZipCodeField,USPhoneNumberField
from django.contrib.localflavor.us.us_states import STATE_CHOICES
from django.db.models import Avg,Min,Max,Count,F,Q
#from django.contrib.localflavor import us
from feedback.models import FEEDBACK_TYPE_CHOICES,COPPA_CHOICES
from trueozarks.models import Profile

class ContactForm( forms.Form ):
  name = forms.CharField( max_length=150, required=True )
  phone_number = USPhoneNumberField( required = True )
  email = forms.EmailField( required = True )
  #profile = forms.ModelChoiceField(queryset=Profile.objects.filter(active=True),required=False)
  comments = forms.CharField( label='Comments',widget=forms.Textarea(attrs={'rows':5,'cols':60}), required=False)
  image = forms.ImageField( label="Picture",required=False )