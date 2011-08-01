# Create your views here
import datetime
from django.core.mail import send_mail
#from django.template.loader import render_to_string
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import ContactForm
from models import FEEDBACK_TYPE_CHOICES
from feedback.models import Feedback
from django.views.decorators.cache import never_cache
import logging

@never_cache
def index( request ):
  #checking to see if the form has been submitted
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      #message
      message = u'Name: ' + cd['name'] + '\r\n'
      message += u'Address: ' + cd['address'] +'\r\n'
      message += u'City: ' + cd['city'] +'\r\n'
      message += u'State: ' + cd['state'] +'\r\n'
      message += u'Zip Code: ' + cd['zip_code'] +'\r\n'
      message += u'Email: ' + cd['email'] +'\r\n'
      message += u'Phone Number: ' + cd['phone_number'] +'\r\n'
      message += u'Feedback Type: ' + cd['feedback_type'] + '\r\n'
      message += u'Message: '
      #converting unicode characters to ascii. hopefully.
      message += cd['message']
      message += u'\r\n\r\n\r\nDebug Information\r\rUser Agent: ' + request.META['HTTP_USER_AGENT'] +'\r\n' 
      message += u'IP Address: ' + request.META['REMOTE_ADDR'] +'\r\n' 
      message += u'Referer: ' + request.META['HTTP_REFERER'] +'\r\n'
      message += u'Number of Words: ' + str( len(cd['message'].split()) ) +'\r\n'
      #saving feedback in the database
      feedback = Feedback()
      feedback.feedback_type = cd['feedback_type']
      feedback.name = cd['name']
      feedback.address = cd['address']
      feedback.city = cd['city']
      feedback.state = cd['state']
      feedback.zip_code = cd['zip_code']
      feedback.phone_number = cd['phone_number']
      feedback.email = cd['email']
      feedback.message = message
      #saving the feedback
      feedback.save()

      #setting where the email goes
      #by default everything goes to letters UNLESS specified
      to = "letters@news-leader.com"
      feedback_type = cd["feedback_type"]
      if feedback_type == "feedback" or feedback_type == "other":
        to = "online@news-leader.com"
      elif feedback_type == "story_idea" or feedback_type == "press_release" or feedback_type == "you_asked":
        to = "webeditor@news-leader.com"

      if feedback_type == 'letter_to_editor':
        feedback_type_text = 'Letter To The Editor'
      elif feedback_type == 'voice_of_day':
        feedback_type_text = 'Voice of the Day'
      elif feedback_type == 'to_the_point':
        feedback_type_text = 'To The Point'
      elif feedback_type == 'rose_thorn':
        feedback_type_text = 'Roses and Thorn'
      elif feedback_type == 'feedback':
        feedback_type_text = 'Story Feedback'
      elif feedback_type == 'story_idea':
        feedback_type_text = 'Story Idea'
      elif feedback_type == 'press_release':
        feedback_type_text = 'Press Release'
      elif feedback_type == 'you_asked':
        feedback_type_text = 'You Asked'
      elif feedback_type == 'other':
        feedback_type_text = 'Other'

      #sending the email
      send_mail(
          'News-Leader.com ' + feedback_type_text + ' Submission: ' + str(cd['name']),
          message,
          'online@news-leader.com',
          #['letters@news-leader.com','snl-letters@gannett.com','tlane@news-leader.com','tlane2@gannett.com'],
          [to,'tlane2@gannett.com','mpeterson4@gannett.com',],
          )

      #secondary message to the user without the debug
      message = 'Name: ' + str(cd['name']) + '\r\n'
      message += 'Address: ' + str(cd['address']) +'\r\n'
      message += 'City: ' + str(cd['city']) +'\r\n'
      message += 'State: ' + str(cd['state']) +'\r\n'
      message += 'Zip Code: ' + str(cd['zip_code']) +'\r\n'
      message += 'Email: ' + str(cd['email']) +'\r\n'
      message += 'Phone Number: ' + str(cd['phone_number']) +'\r\n'
      message += "Message: "
      #converting unicode to ascii, hopefully
      message += str(cd['message'].encode('ascii','xmlcharrefreplace'))
      
      send_mail(
          'News-Leader ' + feedback_type_text + ' Submission: ' + str(cd['name']),
          message,
          'online@news-leader.com',
          [cd['email'],],
          )


      return HttpResponseRedirect('/feedback/thanks')
  else:
    #first submission of the form
    feedback_type= "letter_to_editor"
    if 'feedback_type' in request.GET.keys():
      feedback_type = request.GET['feedback_type']
    form = ContactForm(initial={'state':'MO','feedback_type': feedback_type})
  return render_to_response('feedback/feedback.html', {'form': form},context_instance = RequestContext(request))

def thanks( request ):
  #just an empty function to display our thanks page.
  return render_to_response('feedback/thanks.html', context_instance=RequestContext(request))
