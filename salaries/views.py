# Create your views here.
import datetime
#from django.contrib.gis.geos import Point
#from django.contrib.gis.measure import D
from django.core.paginator import Paginator
#from django.db.models import Avg,Min,Max,Count,F,Q
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response
#from django.template.loader import render_to_string
from django.template import RequestContext
#from django.utils import simplejson
#from django.views.decorators.cache import never_cache
#from django.views.decorators.csrf import csrf_exempt
from models import Person,Salary



def index(request):
	persons = Person.objects.select_related().all()

	
	return render_to_response('salaries/index.html',
		{
			'persons': persons
		},context_instance=RequestContext(request),
	)

