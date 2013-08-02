# Create your views here
from BeautifulSoup import BeautifulSoup, NavigableString,Tag
import datetime
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.core.mail import send_mail,EmailMultiAlternatives
from django.core.paginator import Paginator
from django.db.models import Avg,Min,Max,Count,F,Q
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response, redirect,get_object_or_404,get_list_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from django.template.loader import render_to_string
from django.template import RequestContext,Context,Template
from django.utils import simplejson
from django.core.urlresolvers import reverse
# from django.utils.decorators import decorator_from_middleware
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from models import Layout,Tag,Profile,Story,PullQuote,InfoBox,Photo
import string
import random
from forms import ContactForm

#function for tag cloud
def getRanges(taglist):
	mincount = taglist[0][1]
	maxcount = taglist[len(taglist) - 1][1]
	distrib = (maxcount - mincount) / 3;
	index = mincount
	if (distrib == 0):
		distrib = 1
	ranges = []
	while (index <= maxcount):
		range = (index, index + distrib)
		index = index + distrib
		ranges.append(range)
	return ranges

def chunkIt(seq, num):
	avg = len(seq) / float(num)
	out = []
	last = 0.0
	while last < len(seq):
		out.append(seq[int(last):int(last + avg)])
		last += avg
	return out


#@login_required(redirect_field_name="next")
@never_cache
def index(request):
	profiles = Profile.objects.filter(active=True).order_by('-time_init')[:10]
	# for profile in profiles:
	# 	profile.story.infoboxes = InfoBox.objects.filter(story=profile.story).order_by('position')
	# 	profile.story.pullquotes = PullQuote.objects.filter(story=profile.story).order_by('position')
	# 	profile.photos = Photo.objects.filter(profile=profile).order_by('order')
	tags = Tag.objects.filter(active=True).order_by("?")
	taglist = []
	total_count = 0
	for tag in tags:
		tag.photos = Photo.objects.filter(tags=tag,profile__active=True)
		tag.profiles = Profile.objects.filter(tags=tag,active=True)
		tag.count = int( len(tag.profiles) +  len(tag.photos) )
		total_count += tag.count
		taglist.append((None,int( len(tag.profiles) +  len(tag.photos) )))

	
	rangeStyle = ["smallestTag", "smallTag", "mediumTag", "largeTag", "largestTag"]

	tag_min = map(min,zip(*taglist))
	tag_max = map(max,zip(*taglist))
	tag_range = dict(zip(rangeStyle,chunkIt(range(tag_min[1],(tag_max[1]+1)),5)))
	largestTag = tag_range["largestTag"]
	largeTag = tag_range["largeTag"]
	mediumTag = tag_range["mediumTag"]
	smallTag = tag_range["smallTag"]
	smallestTag = tag_range["smallestTag"]
	

	most_popular = Profile.objects.filter(most_popular=True,active=True)
	return render_to_response('trueozarks/landingPage.html',{'main_profile':profiles[0],'profiles':profiles[1:],"tags":tags,"most_popular":most_popular,"total_count":total_count,"min":tag_min,"max":tag_max,"range":tag_range,'largestTag':largestTag,'largeTag':largeTag,'mediumTag':mediumTag,'smallestTag':smallestTag,'smallTag':smallTag},context_instance=RequestContext(request))

#@login_required(redirect_field_name="next")
@never_cache
def browse_photos(request):
	photos = Photo.objects.filter(profile__active=True).order_by("profile")
	return render_to_response('trueozarks/photos.html',{'photos':photos},context_instance=RequestContext(request))

#@login_required(redirect_field_name="next")
@never_cache
def browse_tags(request):
	tags = Tag.objects.filter(active=True).order_by("?")
	taglist = []
	total_count = 0
	for tag in tags:
		tag.photos = Photo.objects.filter(tags=tag,profile__active=True)
		tag.profiles = Profile.objects.filter(tags=tag,active=True)
		tag.count = int( len(tag.profiles) +  len(tag.photos) )
		total_count += tag.count
		taglist.append((None,int( len(tag.profiles) +  len(tag.photos) )))

	rangeStyle = ["smallestTag", "smallTag", "mediumTag", "largeTag", "largestTag"]

	tag_min = map(min,zip(*taglist))
	tag_max = map(max,zip(*taglist))
	tag_range = dict(zip(rangeStyle,chunkIt(range(tag_min[1],(tag_max[1]+1)),5)))
	largestTag = tag_range["largestTag"]
	largeTag = tag_range["largeTag"]
	mediumTag = tag_range["mediumTag"]
	smallTag = tag_range["smallTag"]
	smallestTag = tag_range["smallestTag"]

	return render_to_response('trueozarks/tags.html',{'tags':tags,'taglist':taglist,"total_count":total_count,"min":tag_min,"max":tag_max,"range":tag_range,'largestTag':largestTag,'largeTag':largeTag,'mediumTag':mediumTag,'smallestTag':smallestTag,'smallTag':smallTag },context_instance=RequestContext(request))

#@login_required(redirect_field_name="next")
@never_cache
def tag_detail(request,tag):
	tag = get_object_or_404(Tag,name=tag)
	profiles = Profile.objects.filter(tags=tag.id,active=True).order_by('name')
	photos = Photo.objects.filter(tags=tag.id,profile__active=True).order_by('profile','order')
	return render_to_response('trueozarks/tag_detail.html',{'tag':tag,'profiles':profiles,'photos':photos},context_instance=RequestContext(request))

#@login_required(redirect_field_name="next")
@never_cache
def browse_maps(request):
	profiles = Profile.objects.filter(active=True)
	return render_to_response('trueozarks/maps.html',{'profiles':profiles},context_instance=RequestContext(request))

##@login_required(redirect_field_name="next")
@never_cache
def view_profile(request,profile_id,profile_name=None):
	profile = get_object_or_404(Profile,id=profile_id)
	pullquotes = PullQuote.objects.filter(profile=profile,active=True).order_by("position")
	photos = Photo.objects.filter(profile=profile,in_gallery=True)
	photos_in_story = Photo.objects.filter(in_story=True,profile=profile).order_by("position")

	infoboxes = InfoBox.objects.filter(profile=profile,active=True).order_by("position")
	paragraphs = profile.story.text.split("\r\n")
	#looping through the paragraphs to kill off empty ones.
	paragraph_count = 0
	total_paragraphs = len(paragraphs)
	while paragraph_count != total_paragraphs:
		try:
			if paragraphs[paragraph_count] == "":
				del paragraphs[paragraph_count]
		except:
			pass
		paragraph_count += 1

	if profile.layout.name != "default":
		return render_to_response(profile.layout.template.path,{'profile':profile,'pullquotes':pullquotes,'photos':photos,'infoboxes':infoboxes,'paragraphs':paragraphs,"photos_in_story":photos_in_story},context_instance=RequestContext(request))
	else:
		return render_to_response('trueozarks/profile.html',{'profile':profile,'pullquotes':pullquotes,'photos':photos,'infoboxes':infoboxes,'paragraphs':paragraphs,"photos_in_story":photos_in_story},context_instance=RequestContext(request))

#@login_required(redirect_field_name="next")
@never_cache
def login_page(request):
	return render_to_response("trueozarks/login_page.html",context_instance=RequestContext(request))

def handler500(request):
	"""
	500 error handler which includes ``request`` in the context.

	Templates: `500.html`
	Context: None
	"""
	from django.template import Context, loader
	from django.http import HttpResponseServerError

	if "trueozarks" in request.path:
		t = loader.get_template('trueozarks/500.html') # You need to create a 500.html template.
	else:
		t = loader.get_template('500.html') #load the default 500 error page.
	return HttpResponseServerError(t.render(RequestContext(request)))

def handler404(request):
	pass

def contactform(request):

	if request.method == "POST":
		#try:
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			if request.FILES.has_key("image"):
				img_data = request.FILES["image"].open()
			# Create a "related" message container that will hold the HTML 
			# message and the image
			#msg = MIMEMultipart(_subtype='related')
			# Create the body with HTML. Note that the image, since it is inline, is 
			# referenced with the URL cid:myimage... you should take care to make
			# "myimage" unique
			message_text = u'<b>Name:</b> ' + cd['name'] + '<br />'
			message_text += u'<b>Phone:</b> ' + cd['phone_number'] +'<br />'
			message_text += u'<b>Email:</b> ' + cd['email'] +'<br />'
			message_text += u'<b>Comments: </b>' + cd['comments'] +'<br />'
			if request.FILES.has_key("image"):
				message_text += u'<b>Image</b>: attached '
			#body = MIMEText( message_text , _subtype='html')
			#msg.attach(body)

			# Now create the MIME container for the image
			#img = MIMEImage(img_data, 'jpeg')
			#img.add_header('Content-Id', '<myimage>')  # angle brackets are important
			#msg.attach(img)
			msg = EmailMultiAlternatives('Springfield Revealed Submission: ' + cd['name'],'some text here','online@news-leader.com', ['shocklan@gannett.com','tlane2@gannett.com','mpeterson4@gannett.com'],)
			msg.attach_alternative( message_text, 'text/html')
			if request.FILES.has_key("image"):
				msg.attach(request.FILES["image"].name,request.FILES["image"].read())
			msg.send()

			return HttpResponseRedirect('/trueozarks/contact/success')
		#except:
		#	return HttpResponseRedirect('/trueozarks/contact/error')
	else:
		form = ContactForm()
	return render_to_response("trueozarks/contactform.html",{'form':form}, context_instance=RequestContext(request))

def contact_success(request):
	return render_to_response("trueozarks/contact_success.html",context_instance=RequestContext(request))

def contact_error(request):
	return render_to_response("trueozarks/contact_error.html",context_instance=RequestContext(request))