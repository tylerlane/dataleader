# Create your views here.
from census.models import CityData,CountyData,StateData,TractData
from django.db.models import Avg,Min,Max,Count,F,Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext


def index( request,embed=None ):
	states = StateData.objects.all()
	for state in states:
		state.popchange = state.pop2010 - state.pop2000
		state.popchangepercentage = ( float( state.popchange ) / float( state.pop2000 ) ) * 100.00
	if "sort_by" in request.GET.keys():
		sort_by = request.GET['sort_by']
	else:
		sort_by = 'state'
	if "order" in request.GET.keys():
		order = request.GET[ "order"]
	else:
		order ="ASC"
	if embed is None:
		return render_to_response( "census/index.html",{'states': states,'sort_by':sort_by, "order": order }, context_instance = RequestContext( request ) )
	else:
		return render_to_response( "census/embed/index.html", {"states": states,'sort_by':sort_by, "order": order }, context_instance = RequestContext( request ) )

def list_counties( request, state,embed=None ):
	counties = CountyData.objects.filter( state = state.upper() )
	state_data = StateData.objects.get( state = state.upper() )
	state_data.popchange = state_data.pop2010 - state_data.pop2000
	state_data.popchangepercentage = ( float( state_data.popchange ) / float( state_data.pop2000 ) ) * 100.00
	for county in counties:
		county.popchange = county.pop2010 - county.pop2000
		county.popchangepercentage = ( float( county.popchange ) / float( county.pop2000 ) ) * 100.00
	if "sort_by" in request.GET.keys():
		sort_by = request.GET['sort_by']
	else:
		sort_by = 'county'
	if "order" in request.GET.keys():
		order = request.GET[ "order"]
	else:
		order ="ASC"
	if embed is None:
		return render_to_response( "census/counties.html", {"counties": counties, 'state': state,"state_data":state_data,'sort_by':sort_by, "order": order }, context_instance =  RequestContext( request ) )
	else:
		return render_to_response( "census/embed/counties.html", {"counties": counties, "state": state, "state_data":state_data,'sort_by':sort_by, "order": order }, context_instance = RequestContext( request ) )

def list_cities( request, state,embed=None  ):
	cities = CityData.objects.filter( state = state.upper() )
	state_data = StateData.objects.get( state = state.upper() )
	state_data.popchange = state_data.pop2010 - state_data.pop2000
	state_data.popchangepercentage = ( float( state_data.popchange ) / float( state_data.pop2000 ) ) * 100.00
	for city in cities:
		city.popchange = city.pop2010 - city.pop2000
		city.popchangepercentage = ( float( city.popchange ) / float( city.pop2000 ) ) * 100.00
		#city.city_name_new = city.city_name.replace( "city","" )
		#city.city_name_new = city.city_name.replace( "town","" )
		#city.city_name_new = city.city_name.replace( "CDP","" )
	if "sort_by" in request.GET.keys():
		sort_by = request.GET['sort_by']
	else:
		sort_by = 'city'
	if "order" in request.GET.keys():
		order = request.GET[ "order"]
	else:
		order ="ASC"
	if embed is None:
		return render_to_response( "census/cities.html", {"cities": cities, "state": state, "state_data":state_data,'sort_by':sort_by, "order": order }, context_instance = RequestContext( request ) )
	else:
		return render_to_response( "census/embed/cities.html", {"cities": cities, "state": state, "state_data":state_data,'sort_by':sort_by, "order": order }, context_instance = RequestContext( request ) )
	

def county_detail( request, state, county, embed=None ):
	county = CountyData.objects.get( state = state.upper(), county_name = county )
	county.popchange = county.pop2010 - county.pop2000
	county.popchangepercentage = ( float( county.popchange ) / float( county.pop2000 ) ) * 100.00

	county.whitechange =  county.popwhite2010 - county.popwhite2000
	try:
		county.whitechangepercentage = ( float( county.whitechange ) / float ( county.popwhite2000 ) ) * 100.00
	except:
		county.whitechangepercentage = 0
		
	county.blackchange =  county.popblack2010 - county.popblack2000
	try:
		county.blackchangepercentage = ( float( county.blackchange ) / float ( county.popblack2000 ) ) * 100.00
	except:
		county.blackchangepercentage = 0

	county.amindchange = county.popamind2010 - county.popamind2000
	try:
		county.amindchangepercentage = ( float( county.amindchange ) / float ( county.popamind2000 ) ) * 100.00
	except:
		county.amindchangepercentage = 0

	county.asianchange = county.popasian2010 - county.popasian2000
	try:
		county.asianchangepercentage = ( float( county.asianchange ) / float( county.popasian2000 ) ) * 100.00
	except:
		county.asianchangepercentage = 0

	county.nathawchange = county.popnathaw2010 - county.popnathaw2000
	try:
		county.nathawchangepercentage = ( float( county.nathawchange ) / float( county.popnathaw2000 ) ) * 100.00
	except:
		county.nathawchangepercentage = 0

	county.otherchange = county.popother2010 - county.popother2000
	try:
		county.otherchangepercentage = ( float( county.otherchange ) / float( county.popother2000 ) ) * 100.00
	except:
		county.otherchangepercentage = 0

	county.twoormorechange = county.pop2ormore2010 - county.pop2ormore2000
	try:
		county.twoormorechangepercentage = ( float( county.twoormorechange ) / float( county.pop2ormore2000 ) ) * 100.00
	except:
		county.twoormorechangepercentage = 0
	county.hispchange = county.pophisp2010 - county.pophisp2000
	try:
		county.hispchangepercentage = ( float( county.hispchange ) / float( county.pophisp2000 ) ) * 100.00
	except:
		county.hispchangepercentage = 0

	county.nonhispchange = county.popnonhisp2010 - county.popnonhisp2000
	try:
		county.nonhispchangepercentage = ( float( county.nonhispchange ) / float( county.popnonhisp2000 ) ) * 100.00
	except:
		county.nonhispchangepercentage = 0

	county.whitenonhispchange = county.popwhitenonhisp2010 - county.popwhitenonhisp2000
	try:
		county.whitenonhispchangepercentage = ( float( county.whitenonhispchange ) / float( county.popwhitenonhisp2000 ) ) * 100.00
	except:
		county.whitenonhispchangepercentage = 0
	if "sort_by" in request.GET.keys():
		sort_by = request.GET['sort_by']
	else:
		sort_by = 'county'
	if "order" in request.GET.keys():
		order = request.GET[ "order"]
	else:
		order ="ASC"
	if embed is None:
		return render_to_response( "census/county_detail.html", {"county": county, "state": state,'sort_by':sort_by, "order": order }, context_instance = RequestContext( request ) )
	else:
		return render_to_response( "census/embed/county_detail.html", {"county": county, "state": state,'sort_by':sort_by, "order": order }, context_instance = RequestContext( request ) )

def city_detail( request, state, city, embed=None ):
	city = CityData.objects.get( state = state.upper(), city_name = city )
	city.popchange = city.pop2010 - city.pop2000
	city.popchangepercentage = ( float( city.popchange ) / float( city.pop2000 ) ) * 100.00

	city.whitechange =  city.popwhite2010 - city.popwhite2000
	try:
		city.whitechangepercentage = ( float( city.whitechange ) / float ( city.popwhite2000 ) ) * 100.00
	except:
		city.whitechangepercentage = 0

	city.blackchange =  city.popblack2010 - city.popblack2000
	try:
		city.blackchangepercentage = ( float( city.blackchange ) / float ( city.popblack2000 ) ) * 100.00
	except:
		city.blackchangepercentage = 0

	city.amindchange = city.popamind2010 - city.popamind2000
	try:
		city.amindchangepercentage = ( float( city.amindchange ) / float ( city.popamind2000 ) ) * 100.00
	except:
		city.amindchangepercentage = 0
		
	city.asianchange = city.popasian2010 - city.popasian2000
	try:
		city.asianchangepercentage = ( float( city.asianchange ) / float( city.popasian2000 ) ) * 100.00
	except:
		city.asianchangepercentage = 0
	
	city.nathawchange = city.popnathaw2010 - city.popnathaw2000
	try:
		city.nathawchangepercentage = ( float( city.nathawchange ) / float( city.popnathaw2000 ) ) * 100.00
	except:
		city.nathawchangepercentage = 0	
	
	city.otherchange = city.popother2010 - city.popother2000
	try:
		city.otherchangepercentage = ( float( city.otherchange ) / float( city.popother2000 ) ) * 100.00
	except:
		city.otherchangepercentage = 0
		
	city.twoormorechange = city.pop2ormore2010 - city.pop2ormore2000
	try:
		city.twoormorechangepercentage = ( float( city.twoormorechange ) / float( city.pop2ormore2000 ) ) * 100.00
	except:
		city.twoormorechangepercentage = 0
		
	city.hispchange = city.pophisp2010 - city.pophisp2000
	try:
		city.hispchangepercentage = ( float( city.hispchange ) / float( city.pophisp2000 ) ) * 100.00
	except:
		city.hispchangepercentage = 0

	city.nonhispchange = city.popnonhisp2010 - city.popnonhisp2000
	try:
		city.nonhispchangepercentage = ( float( city.nonhispchange ) / float( city.popnonhisp2000 ) ) * 100.00
	except:
		city.nonhispchangepercentage = 0

	city.whitenonhispchange = city.popwhitenonhisp2010 - city.popwhitenonhisp2000
	try:
		city.whitenonhispchangepercentage = ( float( city.whitenonhispchange ) / float( city.popwhitenonhisp2000 ) ) * 100.00
	except:
		city.whitenonhispchangepercentage = 0
	if "sort_by" in request.GET.keys():
		sort_by = request.GET['sort_by']
	else:
		sort_by = 'city'
	if "order" in request.GET.keys():
		order = request.GET[ "order"]
	else:
		order ="ASC"
	if embed is None: 
		return render_to_response( "census/city_detail.html", {"city": city, "state": state,'sort_by':sort_by, "order": order }, context_instance = RequestContext( request ) )
	else:
		return render_to_response( "census/embed/city_detail.html", {"city": city, "state": state,'sort_by':sort_by, "order": order }, context_instance = RequestContext( request ) )
	
	
def state_detail( request, state, embed = None ):
	state = StateData.objects.get( state = state.upper() )
	state.popchange = state.pop2010 - state.pop2000
	state.popchangepercentage = ( float( state.popchange ) / float( state.pop2000 ) ) * 100.00

	state.whitechange =  state.popwhite2010 - state.popwhite2000
	try:
		state.whitechangepercentage = ( float( state.whitechange ) / float ( state.popwhite2000 ) ) * 100.00
	except:
		state.whitechangepercentage = 0

	state.blackchange =  state.popblack2010 - state.popblack2000
	try:
		state.blackchangepercentage = ( float( state.blackchange ) / float ( state.popblack2000 ) ) * 100.00
	except:
		state.blackchangepercentage = 0

	state.amindchange = state.popamind2010 - state.popamind2000
	try:
		state.amindchangepercentage = ( float( state.amindchange ) / float ( state.popamind2000 ) ) * 100.00
	except:
		state.amindchangepercentage = 0

	state.asianchange = state.popasian2010 - state.popasian2000
	try:
		state.asianchangepercentage = ( float( state.asianchange ) / float( state.popasian2000 ) ) * 100.00
	except:
		state.asianchangepercentage = 0

	state.nathawchange = state.popnathaw2010 - state.popnathaw2000
	try:
		state.nathawchangepercentage = ( float( state.nathawchange ) / float( state.popnathaw2000 ) ) * 100.00
	except:
		state.nathawchangepercentage = 0	

	state.otherchange = state.popother2010 - state.popother2000
	try:
		state.otherchangepercentage = ( float( state.otherchange ) / float( state.popother2000 ) ) * 100.00
	except:
		state.otherchangepercentage = 0

	state.twoormorechange = state.pop2ormore2010 - state.pop2ormore2000
	try:
		state.twoormorechangepercentage = ( float( state.twoormorechange ) / float( state.pop2ormore2000 ) ) * 100.00
	except:
		state.twoormorechangepercentage = 0

	state.hispchange = state.pophisp2010 - state.pophisp2000
	try:
		state.hispchangepercentage = ( float( state.hispchange ) / float( state.pophisp2000 ) ) * 100.00
	except:
		state.hispchangepercentage = 0

	state.nonhispchange = state.popnonhisp2010 - state.popnonhisp2000
	try:
		state.nonhispchangepercentage = ( float( state.nonhispchange ) / float( state.popnonhisp2000 ) ) * 100.00
	except:
		state.nonhispchangepercentage = 0

	state.whitenonhispchange = state.popwhitenonhisp2010 - state.popwhitenonhisp2000
	try:
		state.whitenonhispchangepercentage = ( float( state.whitenonhispchange ) / float( state.popwhitenonhisp2000 ) ) * 100.00
	except:
		state.whitenonhispchangepercentage = 0
	if "sort_by" in request.GET.keys():
		sort_by = request.GET['sort_by']
	else:
		sort_by = 'state'
	if "order" in request.GET.keys():
		order = request.GET[ "order"]
	else:
		order ="ASC"
	if embed is None:
		return render_to_response( "census/state_detail.html", { "state": state,'sort_by':sort_by, "order": order }, context_instance = RequestContext( request ) )
	else:
		return render_to_response( "census/embed/state_detail.html", { "state": state,'sort_by':sort_by, "order": order }, context_instance = RequestContext( request ) )
