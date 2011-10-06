from django import forms
from django.contrib.localflavor.us.forms import USStateField,USZipCodeField,USPhoneNumberField
from django.contrib.localflavor.us.us_states import STATE_CHOICES
from django.db.models import Avg,Min,Max,Count,F,Q
#from django.contrib.localflavor import us
from models import FEEDBACK_TYPE_CHOICES,COPPA_CHOICES

class ContactForm(forms.Form):
  name = forms.CharField( max_length=100,required=True)
  address = forms.CharField( max_length=255,required=False)
  city = forms.CharField(max_length=100,required=False)
  state = USStateField(required = False,widget=forms.Select(choices = STATE_CHOICES))
  zip_code = USZipCodeField(required = False )
  phone_number = USPhoneNumberField(required = False)
  email = forms.EmailField(required=True)
  feedback_type = forms.ChoiceField(label="Type of Feedback",choices=FEEDBACK_TYPE_CHOICES, required=True)
  coppa = forms.ChoiceField(label="Age", choices=COPPA_CHOICES)
  message = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':60}))

  def clean_message( self ):
    message = self.cleaned_data['message']
    num_words = len(message.split())
    feedback_type = self.cleaned_data["feedback_type"]
    if feedback_type == "letter_to_editor" and num_words > 300:
        raise forms.ValidationError("Too many words, Letters to the editor can only be 300 words or less")
    elif feedback_type == "to_the_point" and num_words > 100:
        raise forms.ValidationError("Too many words, To the Point can only be 100 words or less")
    elif feedback_type == "rose_thorn" and  num_words > 100:
        raise forms.ValidationError("Too many words, Rose or Thorn submissions can only be 100 words or less")
    elif feedback_type == "voice_of_the_day" and num_words > 500:
        raise forms.ValidationError("Too many words, Voice of the Day submissions can only be 500 words or less")
    
    return message

  def clean_coppa( self ):
    if self.cleaned_data["coppa"] == "under13":
      raise forms.ValidationError("The Springfield News-Leader does not collect personal information from children under the age of 13.  Children under the age of 13 will not receive the service requested in this form, and the records submitted will be deleted. \n\nIf you have any questions, please refer to our terms of service, or contact the News-Leader Digital Editor at (417) 836-1255 or online@news-leader.com.")

    return self.cleaned_data["coppa"]

