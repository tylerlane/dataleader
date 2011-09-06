# Create your views here
import datetime
#from django.contrib.gis.geos import Point
#from django.contrib.gis.measure import D
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
#from django.template.loader import render_to_string
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from restaurants.models import Restaurant, Inspection,Cuisine,Attribute,Neighborhood,Featured
from restaurants.forms import SearchForm
#import re
#import simplejson
#from calls.textutils import *

#variable for items per page
ITEMS_PER_PAGE = 25


@never_cache
def index(request):
    featured = Featured.objects.all()
    return render_to_response('restaurants/landingPage.html',
            {'featured':featured},
            context_instance=RequestContext(request))


@never_cache
def detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    inspections = Inspection.objects.filter(restaurant=restaurant)

    return render_to_response('restaurants/insideRestaurant.html',
        {'restaurant': restaurant, 'inspections': inspections},
        context_instance=RequestContext(request))


@never_cache
def browse(request, letter=None, page=None):
    #my alphabet to loop through on the template
    alphabet = ("%23", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    #if no letter is set.
    if letter is None:
        #set it to A
        letter = "A"
    #if no page is set
    if page is None:
        #set it to 1
        page = 1
    if letter != "#":
        #get the restaurants startign with letter
        restaurants = Restaurant.objects.select_related().filter(name__istartswith=letter)
    else:
        restaurants = Restaurant.objects.select_related().all()
        for letter in alphabet[1:]:
            restaurants = restaurants.exclude(name__istartswith=letter)
    restaurants = restaurants.order_by('name')
    #pass to paginator
    pages = Paginator(restaurants, ITEMS_PER_PAGE)
    #get the page from the paginator
    try:
        p = pages.page(page)
    except:
        raise Http404

    return render_to_response('restaurants/restaurantListing.html',
            {'restaurants': p.object_list,
            'letter': letter,
            'alphabet': alphabet,
            'page_range': pages.page_range,
            'num_pages': pages.num_pages, 'page': p,
            'has_pages': pages.num_pages > 1,
            'has_previous': p.has_previous(),
            'has_next': p.has_next(),
            'previous_page': p.previous_page_number(),
            'next_page': p.next_page_number(),
            'is_first': p == 1,
            'is_last': p == pages.num_pages},
            context_instance=RequestContext(request))


@never_cache
def search(request, page=None):
    #post means we want to do something with the form
    if page is None:
        page = 1
        #flush the session
        request.session.clear()
    #first time they submit the form it is a POST
    if request.method == "POST" or request.session.get("searched", False):
        #we set our post form
        if request.method == "POST":
            form = SearchForm(request.POST)
            request.session["post"] = {}
            request.session["post"]["name"] = form.data["name"]
            request.session["post"]["address"] = form.data["address"]
            request.session["post"]["city"] = form.data["city"]
            request.session["searched"] = True
        else:
            form = SearchForm(request.session["post"])
            request.session["searched"] = True
            request.session.modified = True
        if form.is_valid():
            #shortening the form.cleaned_data to cd
            #to make the code fit within 79 chars
            cd = form.cleaned_data
            #NAME
            if cd["name"] is not None and cd["name"] != "":
                name_q = Q(name__icontains=cd["name"])
            else:
                name_q = None
            #address
            if cd["address"] is not None and cd["address"] != "":
                address_q = Q(address__icontains=cd["address"])
            else:
                address_q = None
            #CITY
            if cd["city"] is not None and cd["city"] != "":
                city_q = Q(city__icontains=cd["city"])
            else:
                city_q = None

            restaurants = Restaurant.objects.all()
            #then we check our search results and filter them if they are there
            if name_q is not None:
                restaurants = restaurants.filter(name_q)
            if address_q is not None:
                restaurants = restaurants.filter(address_q)
            if city_q is not None:
                restaurants = restaurants.filter(city_q)

            pages = Paginator(restaurants, ITEMS_PER_PAGE)
            try:
                # going to see if i can figure out how to do pagination
                p = pages.page(page)
            except:
                #raising a 404 error for pages that have nothing.
                #so crawlers will stop crawling them.
                raise Http404
            content = {'restaurants': p.object_list,
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
                    'form': form, }
        else:
            #setting form and content to send back tot he page
            form = SearchForm()
            content = {'form': form }
    else:
        #setting my form
        form = SearchForm(auto_id=False)
        content = {'form': form, }

    return render_to_response('restaurants/search.html', content,
            context_instance=RequestContext(request))


@never_cache
def confirm_merge(request):
    restaurants_list = request.POST.getlist('restaurants')
    restaurants = Restaurant.objects.filter(id__in=restaurants_list)

    return render_to_response('restaurants/confirm_merge.html',
            {'restaurants': restaurants},
            context_instance=RequestContext(request))

@never_cache
def merge(request,letter=None, page=None):
    #my alphabet to loop through on the template
    alphabet = ("%23", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    #if no letter is set.
    if letter is None:
        #set it to A
        letter = "A"
    #if no page is set
    if page is None:
        #set it to 1
        page = 1
    if letter != "#":
        #get the restaurants startign with letter
        restaurants = Restaurant.objects.select_related().filter(name__istartswith=letter)
    else:
        restaurants = Restaurant.objects.select_related().all()
        for letter in alphabet[1:]:
            restaurants = restaurants.exclude(name__istartswith=letter)
    restaurants = restaurants.order_by('name')
    #pass to paginator
    pages = Paginator(restaurants, ITEMS_PER_PAGE)
    #get the page from the paginator
    try:
        p = pages.page(page)
    except:
        raise Http404

    return render_to_response('restaurants/merge.html',
            {'restaurants': p.object_list,
            'letter': letter,
            'alphabet': alphabet,
            'page_range': pages.page_range,
            'num_pages': pages.num_pages, 'page': p,
            'has_pages': pages.num_pages > 1,
            'has_previous': p.has_previous(),
            'has_next': p.has_next(),
            'previous_page': p.previous_page_number(),
            'next_page': p.next_page_number(),
            'is_first': p == 1,
            'is_last': p == pages.num_pages},
            context_instance=RequestContext(request))


@never_cache
def final_merge(request):
    restaurants_list = request.POST.getlist('restaurants')
    main_restaurant_id = request.POST.get('main_restaurant')
    main_restaurant = Restaurant.objects.get(id=main_restaurant_id)

    for restaurant_id in restaurants_list:
        if restaurant_id != main_restaurant_id:
            #find the restaurant
            restaurant = Restaurant.objects.get(id=restaurant_id)
            #now find all of the inspections
            inspections = Inspection.objects.filter(restaurant=restaurant)
            #loop through them
            for inspection in inspections:
                #set the restaurant to the new restaurant
                inspection.restaurant = main_restaurant
                #save the inspection
                inspection.save()
            #now we delete the old restaurant
            restaurant.delete()

    #get the letter of the main restaurant to redirect us to the first page of
    #listings
    letter = main_restaurant.name[0].upper()
    return HttpResponseRedirect('/restaurants/browse/' + letter + '/1')


@never_cache
def list_cuisines(request):
    cuisines = Cuisine.objects.all()

    return render_to_response('restaurants/listcuisines.html',
            {'cuisines': cuisines},
            context_instance=RequestContext(request))

@never_cache
def list_restaurants_cuisine(request,cuisine):
    cuisine = Cuisine.objects.get(name=cuisine)
    restaurants = Restaurant.objects.filter(cuisine = cuisine )


    return render_to_response('restaurants/restaurantListing.html',
            {'restaurants': restaurants},
            context_instance=RequestContext(request))

@never_cache
def list_recent_inspections(request):
    #days_since = request.GET.get('days', 30)

    #going to show the last 30 days worth of inspections on the index page
    #restaurants = Restaurant.objects.all()
    #days_since_delta = datetime.timedelta(days=int(days_since))
    #inspections = Inspection.objects.select_related().filter(
    #    date__gt=datetime.datetime.today() - days_since_delta)

    #violations = inspections.order_by('-critical')[:10]

    inspections = Inspection.objects.select_related().all().order_by('-date')[:50]

    return render_to_response('restaurants/inspectionListing.html',
            {'inspections': inspections},
            context_instance=RequestContext(request))

@never_cache
def list_neighborhoods(request):
    neighborhoods = Neighborhood.objects.filter(active=True)

    return render_to_response('restaurants/listneighborhoods.html',
            {'neighborhoods' : neighborhoods },
            context_instance=RequestContext(request))

@never_cache
def list_restaurants_neighborhood(request, neighborhood):
    neighborhood = Neighborhood.objects.get(name=neighborhood)
    restaurants = Restaurant.objects.filter(geom__within=neighborhood.geom)

    return render_to_response('restaurants/restaurantListing.html',
            {'restaurants': restaurants},
            context_instance=RequestContext(request))
