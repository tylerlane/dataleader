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
from django.template import RequestContext
from django.utils import simplejson
# from django.utils.decorators import decorator_from_middleware
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from models import Layout,Tag,Profile,Story,PullQuote,InfoBox,Photo


@never_cache
def index(request):
	profiles = Profile.objects.filter(active=True).order_by('-id')

	return render_to_reponse('trueozarks/test.html',{'profiles':profiles},context_instance=RequestContext(request))