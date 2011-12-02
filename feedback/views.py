# Create your views here
import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from feedback.models import Feedback
from forms import ContactForm,WorkerForm,ChristmasForm
import logging
from models import FEEDBACK_TYPE_CHOICES

@never_cache
def index( request ):
  #checking to see if the form has been submitted
  if request.method == 'POST':
    try:
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
        message += u'COPPA: ' + cd['coppa'] +'\r\n'
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
        message = u'Thank you for submitting your feedback. It has been sent to editors for evaluation.\r\n'
        message += u'Below is a copy for your records:\r\n'
        message += u'Name: ' + cd['name'] + '\r\n'
        message += u'Address: ' + cd['address'] +'\r\n'
        message += u'City: ' + cd['city'] +'\r\n'
        message += u'State: ' + cd['state'] +'\r\n'
        message += u'Zip Code: ' + cd['zip_code'] +'\r\n'
        message += u'Email: ' + cd['email'] +'\r\n'
        message += u'Phone Number: ' + cd['phone_number'] +'\r\n'
        message += u'Message: '
        #converting unicode to ascii, hopefully
        message += cd['message']

        send_mail(
            'News-Leader ' + feedback_type_text + ' Submission: ' + str(cd['name']),
            message,
            'online@news-leader.com',
            [cd['email'],],
            )


        return HttpResponseRedirect('/feedback/thanks')
    except:
      #there was an error.. send to the error page.
      return HttpResponseRedirect('/feedback/error')
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

def error( request ):
  #a function to show an error page
  return render_to_response('feedback/error.html',context_instance=RequestContext(request))


def worker_form( request ):
  if request.method == "POST":
    form = WorkerForm(request.POST,request.FILES)
    if form.is_valid():
      cd = form.cleaned_data
      #Load the image you want to send at bytes
      #utf8_file = codecs.EncodedFile(request.FILES['file_field'],"utf-8")
      img_data = request.FILES["image"].open()
      # Create a "related" message container that will hold the HTML 
      # message and the image
      #msg = MIMEMultipart(_subtype='related')
      # Create the body with HTML. Note that the image, since it is inline, is 
      # referenced with the URL cid:myimage... you should take care to make
      # "myimage" unique
      message_text = u'<b>Name:</b> ' + cd['name'] + '<br />'
      message_text += u'<b>Company:</b> ' + cd['company'] +'<br />'
      message_text += u'<b>Nominated By:</b> ' + cd['nominated_by'] +'<br />'
      message_text += u'<b>Business Name:</b> ' + cd['business_name'] +'<br />'
      message_text += u'<b>Phone:</b> ' + cd['phone_number'] +'<br />'
      message_text += u'<b>Email:</b> ' + cd['email'] +'<br />'
      message_text += u'<b>What does your nominee do?:</b> ' + cd['nominee_do'] +'<br />'
      message_text += u'<b>What makes your nominee special?:</b> ' + cd['nominee_special'] +'<br />'
      message_text += u'<b>How long has this worker been with your company?:</b> ' + cd['nominee_worked'] +'<br />'
      message_text += u'<b>Additional Comments: </b>' + cd['nominee_addl_comments'] +'<br />'
      message_text += u'<b>Image</b>: attached '
      #body = MIMEText( message_text , _subtype='html')
      #msg.attach(body)

      # Now create the MIME container for the image
      #img = MIMEImage(img_data, 'jpeg')
      #img.add_header('Content-Id', '<myimage>')  # angle brackets are important
      #msg.attach(img)
      msg = EmailMultiAlternatives('Worker of the Week Submission: ' + cd['name'],'some text here','online@news-leader.com', ['csain@gannett.com','tlane2@gannett.com','mpeterson4@gannett.com'],)
      msg.attach_alternative( message_text, 'text/html')
      msg.attach(request.FILES["image"].name,request.FILES["image"].read())
      msg.send()
      
      #send_mail("Worker of the week Submission", msg.as_string(),"online@news-leader.com",['csain@gannett.com','tlane2@gannett.com','mpeterson4@gannett.com'],)

      return HttpResponseRedirect('/feedback/worker/thanks')

      #except:
      #  #there was an error.. send to the error page.
      #  return HttpResponseRedirect('/feedback/worker/error')
  else:
    form = WorkerForm()

  return render_to_response( 'feedback/worker/form.html', {'form':form}, context_instance = RequestContext(request))

def worker_thanks( request ):
  return render_to_response('feedback/worker/thanks.html', context_instance=RequestContext(request))

def worker_error( request ):
  return render_to_response('feedback/worker/error.html', context_instance=RequestContext(request))

def christmas_form( request ):
  if request.method == "POST":
    form = ChristmasForm(request.POST,request.FILES)
    if form.is_valid():
      cd = form.cleaned_data
      #Load the image you want to send at bytes
      #utf8_file = codecs.EncodedFile(request.FILES['file_field'],"utf-8")
      img_data = request.FILES["image"].open()
      # Create a "related" message container that will hold the HTML 
      # message and the image
      #msg = MIMEMultipart(_subtype='related')
      # Create the body with HTML. Note that the image, since it is inline, is 
      # referenced with the URL cid:myimage... you should take care to make
      # "myimage" unique
      message_text = u'<b>Name:</b> ' + cd['name'] + '<br />'
      message_text += u'<b>Address:</b>' + cd['address'] +'<br />'
      message_text += u'<b>City:</b>' + cd['city'] +'<br />'
      message_text += u'<b>State:</b>' + cd['state'] +'<br />'
      message_text += u'<b>Address:</b>' + cd['address'] +'<br />'
      message_text += u'<b>Phone:</b> ' + cd['phone_number'] +'<br />'
      message_text += u'<b>Email:</b> ' + cd['email'] +'<br />'
      message_text += u'<b>Story:</b> ' + cd['story'] +'<br />'
      message_text += u'<b>Image</b>: attached '
      #body = MIMEText( message_text , _subtype='html')
      #msg.attach(body)

      # Now create the MIME container for the image
      #img = MIMEImage(img_data, 'jpeg')
      #img.add_header('Content-Id', '<myimage>')  # angle brackets are important
      #msg.attach(img)
      msg = EmailMultiAlternatives('Christmas Lights Submission: ' + cd['name'],'some text here','online@news-leader.com', ['aolding@gannett.com','tlane2@gannett.com','mpeterson4@gannett.com','ggarrison@News-Leader.com'],)
      msg.attach_alternative( message_text, 'text/html')
      msg.attach(request.FILES["image"].name,request.FILES["image"].read())
      msg.send()
      
      #send_mail("Worker of the week Submission", msg.as_string(),"online@news-leader.com",['csain@gannett.com','tlane2@gannett.com','mpeterson4@gannett.com'],)

      return HttpResponseRedirect('/feedback/christmas/thanks')

      #except:
      #  #there was an error.. send to the error page.
      #  return HttpResponseRedirect('/feedback/worker/error')
  else:
    form = ChristmasForm(initial={'state':'MO'})

  return render_to_response( 'feedback/christmas/form.html', {'form':form}, context_instance = RequestContext(request))

def christmas_thanks( request ):
  return render_to_response('feedback/christmas/thanks.html', context_instance=RequestContext(request))

def christmas_error( request ):
  return render_to_response('feedback/christmas/error.html', context_instance=RequestContext(request))
