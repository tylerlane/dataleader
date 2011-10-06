# Create your views here.
from django.shortcuts import render_to_response
#from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.http import Http404
from django.template import RequestContext
from django.db.models import Avg,Min,Max,Count,F,Q
import datetime
from warrants.models import Warrant,Court
from warrants.forms import SearchForm
#Variable for items per page
ITEMS_PER_PAGE = 50

def browse( request, letter=None, page=None ):
	#my alphabet to loop through on the template
	alphabet = ( "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z" )
	#if no letter is set.
	if letter is None:
		#set it to A
		letter = "A"
	#if no page is set
	if page is None:
		#set it to 1
		page = 1
	#get the warrants startign with letter
	warrants = Warrant.objects.filter( name__istartswith = letter, active = True ).order_by('name')
	#pass it to the paginator 
	pages = Paginator( warrants, ITEMS_PER_PAGE )
	#get the page from the paginator
	try:
		# going to see if i can figure out how to do pagination
		p = pages.page( page )
	except:
		#raising a 404 error for pages that have nothing. so crawlers will stop crawling them.
		raise Http404
	#return the data to our template
	return render_to_response( 'warrants/browse.html', { 'warrants': p.object_list,
														'letter': letter, 
														'alphabet': alphabet,
														'page_range': pages.page_range,
														'num_pages': pages.num_pages,
														'page': p,
														'has_pages': pages.num_pages > 1,
														'has_previous': p.has_previous(),
														'has_next': p.has_next(),
														'previous_page': p.previous_page_number(),
														'next_page': p.next_page_number(),
														'is_first': p == 1,
														'is_last': p == pages.num_pages,
														'omniture_pagename': 'Data - Warrants' }
														,context_instance = RequestContext(request))
	
def search( request, page=None ):
	#post means we want to do something with the form
	if page is None:
		page = 1
		#flush the session
		request.session.clear()
	#first time they submit the form it is a POST
	if request.method == "POST" or request.session.get( "searched", False ):
		#we set our post form
		if request.method == "POST":
			form = SearchForm( request.POST )
			request.session["post"] = {}
			request.session[ "post" ][ "name" ] = form.data[ "name" ]
			request.session[ "post" ][ "age" ] = form.data[ "age" ]
			request.session[ "post" ][ "bond" ] = form.data[ "bond" ]
			request.session[ "post" ][ "violation_desc" ] = form.data[ "violation_desc" ]
			request.session[ "post" ][ "release_cond" ] = form.data[ "release_cond" ]
			request.session[ "post" ][ "court" ] = form.data[ "court" ]
			request.session[ "post" ][ "warrant_type" ] = form.data[ "warrant_type" ]
			request.session["searched"] = True
		else:
			form = SearchForm(request.session["post"])
			request.session[ "searched" ] = True
			request.session.modified = True
		if form.is_valid():
			#NAME
			if form.cleaned_data[ "name" ] is not None and form.cleaned_data[ "name" ] != "":
				name_q = Q( name__icontains = form.cleaned_data[ "name" ] )
			else:
				name_q = None
			#AGE
			if form.cleaned_data[ "age" ] is not None and form.cleaned_data[ "age" ] != "":
				age_q = Q( age__icontains = form.cleaned_data["age"] )
			else:
				age_q = None
			#BOND
			if form.cleaned_data[ "bond" ] is not None and form.cleaned_data[ "bond" ] != "":
				bond_q = Q( bond__icontains = form.cleaned_data[ "bond" ] )
			else:
				bond_q = None
			#VIOLATION_DESC
			if form.cleaned_data[ "violation_desc" ] is not None and form.cleaned_data[ "violation_desc"] != "":
				violation_desc_q = Q( violation_desc__icontains = form.cleaned_data[ "violation_desc" ] )
			else:
				violation_desc_q = None
			#RELEASE_COND
			if form.cleaned_data[ "release_cond" ] is not None and form.cleaned_data[ "release_cond"] != "":
				release_cond_q = Q( release_cond__icontains = form.cleaned_data[ "release_cond" ] )
			else:
				release_cond_q = None
			#COURT
			if form.cleaned_data[ "court" ] is not None and form.cleaned_data[ "court" ] != "":
				court = Court.objects.get( description = form.cleaned_data[ "court" ] )
				court_q = Q( court=form.cleaned_data["court"])
			else:
				court_q = None
			#WARRANT_TYPE
			if form.cleaned_data[ "warrant_type" ] is not None and form.cleaned_data[ "warrant_type" ] != "":
				warrant_type_q = Q( warrant_type = form.cleaned_data[ "warrant_type" ] )
			else:
				warrant_type_q = None
			#we only want to let them search active warrants. the inactive ones are for us only
			warrants = Warrant.objects.filter( active = True )
			#then we check our search results and filter them if they are there.
			if name_q is not None:
				warrants = warrants.filter( name_q )
			if age_q is not None:
				warrants = warrants.filter( age_q )
			if bond_q is not None:
				warrants = warrants.filter( bond_q )
			if violation_desc_q is not None:
				warrants = warrants.filter( violation_desc_q )
			if court_q is not None:
				warrants = warrants.filter( court_q )
			if release_cond_q is not None:
				warrants = warrants.filter( release_cond_q )
			if warrant_type_q is not None:
				warrants = warrants.filter( warrant_type_q )
		else:
			warrants = Warrant.objects.filter( active=True )
			
		pages = Paginator( warrants, ITEMS_PER_PAGE )
		try:
			# going to see if i can figure out how to do pagination
			p = pages.page( page )
		except:
			#raising a 404 error for pages that have nothing. so crawlers will stop crawling them.
			raise Http404
		
		content = { 'warrants': p.object_list,
					'page_range': pages.page_range,
					'num_pages': pages.num_pages,
					'page': p,
					'has_pages': pages.num_pages > 1,
					'has_previous': p.has_previous(),
					'has_next': p.has_next(),
					'previous_page': p.previous_page_number(),
					'next_page': p.next_page_number(),
					'is_first': p == 1,
					'is_last': p == pages.num_pages,
					'form': form,
					'omniture_pagename': 'Data - Warrants'
					 }
	else:
		#setting my form
		form = SearchForm(auto_id=False)
		content = {
				"form" : form,
				'omniture_pagename': 'Data - Warrants'
				}
		
	return render_to_response('warrants/search.html', content, context_instance = RequestContext( request ))
	
def stats( request ):
	greene_county = Court.objects.get(description="Greene County")
	spf_municipal = Court.objects.get(description="Springfield Municipal")
	greene_warrant_counts = Warrant.objects.filter(court=greene_county,active=True).values("warrant_type").annotate(dcount=Count('warrant_type')).order_by('-dcount')
	spf_warrant_counts =  Warrant.objects.filter(court=spf_municipal,active=True).values("warrant_type").annotate(dcount=Count('warrant_type')).order_by('-dcount')
	
	return render_to_response('warrants/stats.html', {"greene_warrant_counts": greene_warrant_counts, "spf_warrant_counts": spf_warrant_counts,'omniture_pagename': 'Data - Warrants'}, context_instance = RequestContext(request))

