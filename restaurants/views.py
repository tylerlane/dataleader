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
from restaurants.models import Restaurant, Inspection, Cuisine, Attribute, Neighborhood, Featured, Gallery, Pageview, Contest
from restaurants.forms import SearchForm,FeedbackForm,RestaurantForm,ContestForm
from lib import bail

#import re
#import simplejson
#from calls.textutils import *
#variable for items per page
ITEMS_PER_PAGE = 20


#@@decorator_from_middleware(mobileesp.mobile.MobileDetectionMiddleware)

@never_cache
def index(request):
    main_featured = Featured.objects.select_related().filter(restaurant__active=True).order_by("?")[0]
    
    features = Featured.objects.filter(restaurant__active=True,restaurant__cuisine__isnull=False).order_by("-id").exclude(restaurant=main_featured.restaurant).distinct("id")[0:10]
    if request.is_phone or request.is_tablet:
        return render_to_response('restaurants/mobile/main.html', {'features':features,'main_featured':main_featured}, context_instance=RequestContext(request))
    else:
        return render_to_response('restaurants/landingPage.html',{'features':features,"main_featured":main_featured}, context_instance=RequestContext(request))


@never_cache
def detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant,id=restaurant_id)
    inspections = Inspection.objects.filter(restaurant=restaurant)
    #galleries = Gallery.objects.filter(restaurant=restaurant)
    featureds = Featured.objects.filter(restaurant=restaurant)
    if restaurant.geom:
        neighborhoods = Neighborhood.objects.filter(geom__contains=restaurant.geom,active=True)
    else:
        neighborhoods = []
    
    #pull in our attributes
    restaurant.attributes = Attribute.objects.filter(restaurant=restaurant,active=True)
    restaurant.absolute_uri = request.build_absolute_uri()
    
    message = ""
    if restaurant.name is not None:
        message += "Name: " + restaurant.name + "\r\n"
    if restaurant.address is not None:
        message += "Address: " + restaurant.address  + "\r\n"
    if restaurant.city is not None:
        message += "City: " + restaurant.city + "\r\n"
    if restaurant.state is not None:
        message += "State: " + restaurant.state + "\r\n"
    if restaurant.zip_code is not None:
        message += "Zip: " + restaurant.zip_code + "\r\n"
    if restaurant.website is not None:
        message += "Website: " + restaurant.website + "\r\n"
    if restaurant.phone is not None:
        message += "Phone: " + restaurant.phone + "\r\n"
    if restaurant.description is not None:
        message += "Description: " + restaurant.description + "\r\n"
    message += "-----------------\r\n"
    for attribute in restaurant.attributes:
        #replacing "_" with " "
        #attribute.name = " ".join(attribute.name.split("_"))
        #attribute.value = " ".join(attribute.value.split("_"))
        #if attribute.comma_delimited:
        if attribute.value[-1:] == ",":
            attribute.value = attribute.value[0:-2]
        message += attribute.name + ": " + attribute.value + "\r\n"
    if restaurant.rating is None:
        restaurant.rating = "0"
    #form = FeedbackForm(initial=[{'restaurant':restaurant.id,'message':message}])
    #record a pageview for the restaurant
    pageview = Pageview(restaurant=restaurant)
    pageview.save()

    #rest_form = RestaurantForm( instance=restaurant )

    if request.is_phone or request.is_tablet:
        return render_to_response('restaurants/mobile/profile.html',
            {
             'restaurant': restaurant, 
             'inspections': inspections,
             'featureds': featureds,
             'neighborhoods': neighborhoods
            },context_instance=RequestContext(request))
    else:
        return render_to_response('restaurants/insideRestaurant.html',
            {
             'restaurant': restaurant, 
             'inspections': inspections,
             'featureds': featureds,
             'neighborhoods': neighborhoods
            },
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
        #this lets us have The Rebecca Grille show up under T and R
        letter_q = Q(name__istartswith=letter)
        theletter_q = Q(name__istartswith="The " + letter)
        if letter == "T":
            restaurants = Restaurant.objects.filter(letter_q|theletter_q,cuisine__isnull=False,active=True).exclude(name__istartswith="the ").distinct('id')
        else:
            restaurants = Restaurant.objects.filter(letter_q|theletter_q,cuisine__isnull=False,active=True).distinct('id')
    else:
        restaurants = Restaurant.objects.filter(cuisine__isnull=False,active=True)
        for letter in alphabet[1:]:
            restaurants = restaurants.exclude(name__istartswith=letter)
    
    temp_restaurants = []

    restaurants = restaurants.order_by('name')
    #pass to paginator
    pages = Paginator(restaurants, ITEMS_PER_PAGE)
    #get the page from the paginator
    try:
        p = pages.page(page)
    except:
        raise Http404
    if request.is_phone or request.is_tablet:
        return render_to_response('restaurants/mobile/name.html',
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
    else: 
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
            # request.session["post"]["address"] = form.data["address"]
            # request.session["post"]["city"] = form.data["city"]
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
            name_q = Q(name__icontains=cd["name"])
            #address
            address_q = Q(address__icontains=cd["name"])
            #CITY
            city_q = Q(city__icontains=cd["name"])

            cuisine_q = Q(cuisine__name__icontains=cd["name"])

            #attr_names_q = Q(attribute__name__icontains=cd["name"])

            #attr_values_q = Q(attribute__value__icontains=cd["name"])

            restaurants = Restaurant.objects.all()
            #then we check our search results and filter them if they are there
            restaurants = restaurants.filter(name_q|address_q|city_q|cuisine_q)
            
            restaurants = restaurants.filter(active=True,cuisine__isnull=False).distinct("id")

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


@login_required
@user_passes_test( lambda u: u.is_staff )
@never_cache
def confirm_merge(request):
    restaurants_list = request.POST.getlist('restaurants')
    restaurants = Restaurant.objects.filter(id__in=restaurants_list)

    return render_to_response('restaurants/confirm_merge.html',
            {'restaurants': restaurants},
            context_instance=RequestContext(request))

@login_required
@user_passes_test( lambda u: u.is_staff )
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
    if letter != "%23":
        #get the restaurants startign with letter
        restaurants = Restaurant.objects.filter(name__istartswith=letter,active=True).distinct("id")
    else:
        restaurants = Restaurant.objects.all()
        for letter in alphabet[1:]:
            restaurants = restaurants.exclude(name__istartswith=letter)

    restaurants = restaurants.filter(active=True)
    restaurants = restaurants.order_by('name')
    #pass to paginator
    pages = Paginator(restaurants, 50)
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


@login_required
@user_passes_test( lambda u: u.is_staff )
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
    return HttpResponseRedirect('/restaurants/merge/' + letter + '/1')


@never_cache
def list_cuisines(request):
    cuisines = Cuisine.objects.all()
    temp_cuisines = []
    for cuisine in cuisines: 
        restaurants = Restaurant.objects.filter(cuisine=cuisine,active=True)
        if len( restaurants ) > 0:
            temp_cuisines.append(cuisine)
    title = "Cuisines"

    if request.is_phone or request.is_tablet:
       return render_to_response('restaurants/mobile/cuisine.html', {'cuisines': temp_cuisines, "title": title}, context_instance=RequestContext(request))
    else:
        return render_to_response('restaurants/listcuisines.html', {'cuisines': temp_cuisines, "title": title}, context_instance=RequestContext(request))


@never_cache
def list_restaurants_cuisine(request,cuisine,page=None):
    #if no page is set
    if page is None:
        #set it to 1
        page = 1
    #setting the title
    title = "Cuisine: %s" % cuisine

    cuisine = Cuisine.objects.get(name=cuisine)
    browse_cuisine = cuisine.name
    restaurants = Restaurant.objects.filter(cuisine = cuisine )
    restaurants = restaurants.filter(active=True)
    #pass to paginator
    pages = Paginator(restaurants, ITEMS_PER_PAGE)
    #get the page from the paginator
    try:
        p = pages.page(page)
    except:
        raise Http404
    
    path = 'list_restaurants_cuisine'
    if request.is_phone or request.is_tablet:
        cuisines = Cuisine.objects.all()
        temp_cuisines = []
        for cuisine in cuisines: 
            restaurants = Restaurant.objects.filter(cuisine=cuisine,active=True)
            if len( restaurants ) > 0:
                temp_cuisines.append(cuisine)
        cuisines = temp_cuisines
        return render_to_response('restaurants/mobile/cuisine.html',
            {'restaurants': p.object_list,
            'page_range': pages.page_range,
            'num_pages': pages.num_pages, 'page': p,
            'has_pages': pages.num_pages > 1,
            'has_previous': p.has_previous(),
            'has_next': p.has_next(),
            'previous_page': p.previous_page_number(),
            'next_page': p.next_page_number(),
            'is_first': p == 1,
            'is_last': p == pages.num_pages,
            'search_cuisine': browse_cuisine,
            'cuisines': cuisines,
            'path': path,
            'title': title
            },
            context_instance=RequestContext(request))
    else:
        return render_to_response('restaurants/restaurantListing.html',
            {'restaurants': p.object_list,
            'page_range': pages.page_range,
            'num_pages': pages.num_pages, 'page': p,
            'has_pages': pages.num_pages > 1,
            'has_previous': p.has_previous(),
            'has_next': p.has_next(),
            'previous_page': p.previous_page_number(),
            'next_page': p.next_page_number(),
            'is_first': p == 1,
            'is_last': p == pages.num_pages,
            'search_cuisine': cuisine,
            'path': path,
            'title': title
            },
            context_instance=RequestContext(request))


@never_cache
def list_recent_inspections(request,page=None):
    #if page isn't set, set it to 1
    if page is None:
        page = 1

    inspections = Inspection.objects.filter(date__lte=datetime.datetime.today()).order_by('-date')[:500]

    #only show top violators if page is #1
    if page == "1":
        latest_inspection = inspections[0]
        #now to get the highest violations over the last 30 days
        top_violators = Inspection.objects.filter( date__range = ( latest_inspection.date - datetime.timedelta( days = 30 ) , latest_inspection.date )).order_by('-critical')[:10]
    else:
        top_violators = []
    #pass to paginator
    pages = Paginator(inspections, ITEMS_PER_PAGE)
    #get the page from the paginator
    try:
        p = pages.page(page)
    except:
        raise Http404
    path = 'list_recent_inspections'
    if request.is_phone or request.is_tablet:
        return render_to_response('restaurants/mobile/inspections.html',
            {'inspections': p.object_list,
            'page_range': pages.page_range,
            'num_pages': pages.num_pages, 'page': p,
            'has_pages': pages.num_pages > 1,
            'has_previous': p.has_previous(),
            'has_next': p.has_next(),
            'previous_page': p.previous_page_number(),
            'next_page': p.next_page_number(),
            'is_first': p == 1,
            'is_last': p == pages.num_pages,
            'top_violators': top_violators,
            'path': list_recent_inspections
            },
            context_instance=RequestContext(request))
    else:
        return render_to_response('restaurants/inspectionListing.html',
            {'inspections': p.object_list,
            'page_range': pages.page_range,
            'num_pages': pages.num_pages, 'page': p,
            'has_pages': pages.num_pages > 1,
            'has_previous': p.has_previous(),
            'has_next': p.has_next(),
            'previous_page': p.previous_page_number(),
            'next_page': p.next_page_number(),
            'is_first': p == 1,
            'is_last': p == pages.num_pages,
            'top_violators': top_violators,
            'path': list_recent_inspections
            },
            context_instance=RequestContext(request))

    return render_to_response('restaurants/inspectionListing.html',
            {
                'inspections': inspections,
                'top_violators': top_violators
            },
            context_instance=RequestContext(request))

@never_cache
def list_neighborhoods(request):
    neighborhoods = Neighborhood.objects.filter(active=True)
    for neighborhood in neighborhoods:
        restaurants = Restaurant.objects.filter(geom__within=neighborhood.geom,cuisine__isnull=False,active=True).distinct("id")
        neighborhood.count = len(restaurants)
    if request.is_phone or request.is_tablet:
        return render_to_response('restaurants/mobile/neighborhood.html',{'neighborhoods' : neighborhoods },context_instance=RequestContext(request))
    else:
        return render_to_response('restaurants/listneighborhoods.html',{'neighborhoods' : neighborhoods },context_instance=RequestContext(request))

@never_cache
def list_restaurants_neighborhood(request, neighborhood,page=None):
    #if no page is set
    if page is None:
        #set it to 1
        page = 1

    neighborhood = Neighborhood.objects.get(name=neighborhood)
    restaurants = Restaurant.objects.filter(geom__within=neighborhood.geom,active=True,cuisine__isnull=False).distinct("id")
    title = "Restaurants in %s" % (neighborhood.name)
    #pass to paginator
    pages = Paginator(restaurants, ITEMS_PER_PAGE)
    #get the page from the paginator
    try:
        p = pages.page(page)
    except:
        raise Http404
    path = 'list_restaurants_neighborhood'
    if request.is_phone or request.is_tablet:
        neighborhoods = Neighborhood.objects.filter(active=True)
        return render_to_response('restaurants/mobile/neighborhood.html',
                {'restaurants':p.object_list,
                'page_range':pages.page_range,
                'num_pages': pages.num_pages,
                'page':p,
                'has_pages': pages.num_pages > 1,
                'has_previous':p.has_previous(),
                'has_next': p.has_next(),
                'previous_page': p.previous_page_number(),
                'next_page': p.next_page_number(),
                'is_first': p == 1,
                'is_last': p == pages.num_pages,
                'neighborhood': neighborhood.name,
                'neighborhoods': neighborhoods,
                'title': 'Restaurants in %s' % (neighborhood.name),
                'path': 'list_restaurants_neighborhood'

                },context_instance=RequestContext(request))
    else:
        return render_to_response('restaurants/restaurantListing.html',
                {'restaurants': p.object_list,
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
                'neighborhood': neighborhood.name,
                'path': 'list_restaurants_neighborhood',
                'title': "Restaurants in %s" % (neighborhood.name)
                },
                context_instance=RequestContext(request))


@never_cache
def record_rating_vote(request, restaurant, rating):
    #function to records the votes. should only be called via ajax.
    restaurant = Restaurant.objects.get(restaurant = restaurant)
    restaurant.rating_sum += rating
    restaurant.rating_total_votes += 1
    restaurant.save()

@never_cache
def list_attributes(request):
    attributes = Attribute.objects.filter(active=True).values("name").distinct("name")
    json_data=open('/opt/django/data.news-leader.com/dataleader/static/restaurants/restaurant_attribute_values.json')

    data = simplejson.load(json_data)
    json_data.close();
    if request.is_phone or request.is_tablet:
        return render_to_response('restaurants/mobile/features.html', {'attributes':attributes,'title':'Browse By:',"new_attrs":data}, context_instance=RequestContext(request))
    else:
        return render_to_response('restaurants/listattributes.html', {'attributes':attributes,'title':'Browse By:'}, context_instance=RequestContext(request))

@never_cache
def list_attribute_values(request, attribute,page=None):
    #if no page is set
    if page is None:
        #set it to 1
        page = 1
    #adding the restaurant__active to show only attributes for active restaurants :)
    attributes = Attribute.objects.filter(name__iexact=attribute,active=True,restaurant__active=True,restaurant__cuisine__isnull=False).values("name","value").distinct("value")
    
    attributes_list = []

    title = "%s" % attribute
    
    for attribute in attributes:
        #getting a list of values
        attrs_split = attribute["value"].split(",")
        for attr in attrs_split:
            attributes_list.append(str(attr).strip().lower())
    #now that we have the attributes. we remove dups
    last = attributes_list[-1]
    #code to remove duplicates
    seen = set()
    seen_add = seen.add
    attributes_list =  [ x for x in attributes_list if x not in seen and not seen_add(x)]
    if request.is_phone or request.is_tablet:
        attributes = Attribute.objects.filter(active=True).values("name").distinct("name")
        return render_to_response('restaurants/mobile/features.html',
            {'attributes':attributes,'attributes_list':attributes_list,"orig_attribute": attribute,"attributes":attributes, "title":title},
            context_instance=RequestContext(request))
    else:
        return render_to_response('restaurants/listattributevalues.html',
            {'attributes':attributes,'attributes_list':attributes_list,"orig_attribute": attribute, "title":title},
            context_instance=RequestContext(request))

@never_cache
def list_restaurants_attribute(request, attribute, value, page=None):
    #if no page is set
    if page is None:
        #set it to 1
        page = 1
    #if attribute is average entree price then do an exact lookup, else do an icontains/ilike
    #this may not be needed after i fixed the avg entree prices
    if attribute == "average entree price":
        attributes = get_list_or_404(Attribute,name__iexact=attribute, value__iexact=value, active=True)
    else:
        attributes = get_list_or_404(Attribute,name__iexact=attribute, value__icontains=value, active=True)
    restaurants = []
    for attribute in attributes:
        try: 
            tmp = Restaurant.objects.get(id=attribute.restaurant.id,active=True)
            restaurants.append(tmp)
        except:
            pass

    #setting title
    title = "%s : %s" % (attribute, value)
    #have to sort the restaurant objects that are in my list. found this on stackoverflow. very useful to sort a 
    #list of objects by a value in the objects
    restaurants = sorted(restaurants, key=lambda x: x.name, reverse=False)  
    #restaurants = restaurants.filter(active=True)
    #pass to paginator
    pages = Paginator(restaurants, ITEMS_PER_PAGE)
    #get the page from the paginator
    try:
        p = pages.page(page)
    except:
        raise Http404
    
    path = "list_restaurants_attribute"
    if request.is_phone or request.is_tablet:
        #if it's mobile we need to get the attributes and values also since we're displaying them all on one page.
        #long term this will be cleaned up and made better
        # attributes = Attribute.objects.filter(name__iexact=attribute,active=True,restaurant__active=True,restaurant__cuisine__isnull=False).values("name","value").distinct("value")
        # attributes_list = []
               
        # for attribute in attributes:
        #     #getting a list of values
        #     attrs_split = attribute["value"].split(",")
        #     for attr in attrs_split:
        #         attributes_list.append(str(attr).strip().lower())
        # #now that we have the attributes. we remove dups
        # last = attributes_list[-1]
        # #code to remove duplicates
        # seen = set()
        # seen_add = seen.add
        #attributes_list =  [ x for x in attributes_list if x not in seen and not seen_add(x)]

        attributes = Attribute.objects.filter(active=True).values("name").distinct("name")
        return render_to_response('restaurants/mobile/features.html',
            {'restaurants': p.object_list,
            'page_range': pages.page_range,
            'num_pages': pages.num_pages, 'page': p,
            'has_pages': pages.num_pages > 1,
            'has_previous': p.has_previous(),
            'has_next': p.has_next(),
            'previous_page': p.previous_page_number(),
            'next_page': p.next_page_number(),
            'is_first': p == 1,
            'is_last': p == pages.num_pages,
            'title': title,
            'path': path,
            'attribute': attribute,
            'value': value,
            #'attributes_list':attributes_list,
            'attributes': attributes

            },
            context_instance=RequestContext(request))
    else:
        return render_to_response('restaurants/restaurantListing.html',
            {'restaurants': p.object_list,
            'page_range': pages.page_range,
            'num_pages': pages.num_pages, 'page': p,
            'has_pages': pages.num_pages > 1,
            'has_previous': p.has_previous(),
            'has_next': p.has_next(),
            'previous_page': p.previous_page_number(),
            'next_page': p.next_page_number(),
            'is_first': p == 1,
            'is_last': p == pages.num_pages,
            'title': title,
            'path': path,
            'attribute': attribute,
            'value': value
            },
            context_instance=RequestContext(request))


@csrf_exempt
@never_cache
def record_rating(request):
    if request.is_ajax():
        if request.method == 'POST':
            print "restaurant: %s" % request.POST.get("restaurant")
            print "rating: %s" %request.POST.get("rating")
            restaurant = Restaurant.objects.get(id=request.POST.get("restaurant"))
            print "restaurant: %s" % restaurant
            if restaurant.rating_sum is None:
                restaurant.rating_sum = float(request.POST.get("rating"))
            else:
                restaurant.rating_sum = float(restaurant.rating_sum) + float(request.POST.get("rating"))
            if restaurant.rating_total_votes is None:
                restaurant.rating_total_votes = 1
            else:
                restaurant.rating_total_votes += 1
            restaurant.save()
            #print "saving vote"
            #print "Sum: %s" % restaurant.rating_sum
            #print "Total Votes: %s" % restaurant.rating_total_votes
            rating = str((float(restaurant.rating_sum) / float(restaurant.rating_total_votes) ))
            #rating_dict = {"rating":rating}
            return HttpResponse(rating)
    else:
        return HttpResponse(status="400")

@never_cache
def display_top_rated(request,page=None):
    if page is None:
        page=1

    restaurants = Restaurant.objects.filter(active=True,rating__isnull=False,rating_total_votes__gte=10,rating__gte=3.0).order_by('rating')
    #restaurants = restaurants[0:20]
    title = "Top Rated Restaurants"
    toprated = True
    #pass to paginator
    pages = Paginator(restaurants, ITEMS_PER_PAGE)
    #get the page from the paginator
    try:
        p = pages.page(page)
    except:
        raise Http404

    return render_to_response('restaurants/restaurantListing.html',
            {'restaurants': p.object_list,
            'page_range': pages.page_range,
            'num_pages': pages.num_pages, 'page': p,
            'has_pages': pages.num_pages > 1,
            'has_previous': p.has_previous(),
            'has_next': p.has_next(),
            'previous_page': p.previous_page_number(),
            'next_page': p.next_page_number(),
            'is_first': p == 1,
            'is_last': p == pages.num_pages,
            'title': title,
            'toprated': toprated
            },
            context_instance=RequestContext(request))
    
    #return render_to_response('restaurants/restaurantListing.html',
    #        {'restaurants': restaurants,'title': title},
    #        context_instance=RequestContext(request))

@never_cache
def display_most_viewed(request):
    #get pageviews
    pvs = Pageview.objects.filter(time_init__range =
            (datetime.datetime.today() - datetime.timedelta(seconds=7776000),
            datetime.datetime.today()),restaurant__cuisine__isnull=False)
    #then group and count them by restaurant and we are limiting it to the top 30
    pvs = pvs.values('restaurant').annotate(pageviews=Count('id')).order_by('restaurant')[0:30]
    #empty list to story our restaurants
    restaurants = []
    for pv in pvs:
        #loop through pageviews and pull the restaurant for each pageview
        #and stick it into our list
        tmp = Restaurant.objects.get(id=pv['restaurant'])
        tmp.pageviews = pv["pageviews"]
        restaurants.append( tmp )


    mostviewed = True
    title = "Most Viewed Restaurants (Last 90 Days)"
    return  render_to_response('restaurants/restaurantListing.html',
            {'restaurants': restaurants,'title': title, 'mostviewed': mostviewed },
            context_instance=RequestContext(request))

# @never_cache
# def new_restaurants(request, page=None):
#     restaurants = Restaurant.objects.filter(status="NEW")
#     restaurants = restaurants.filter(active=True)
#     pages = Paginator(restaurants, ITEMS_PER_PAGE)
#     if page is None:
#         #set it to 1
#         page = 1
    
#     #get the page from the paginator
#     try:
#         p = pages.page(page)
#     except:
#         raise Http404

#     return render_to_response('restaurants/admin_new_restaurants.html',
#             {'restaurants': p.object_list,
#             'title': 'New Restaurants',
#             'to': 'new_restaurants_admin',
#             'page_range': pages.page_range,
#             'num_pages': pages.num_pages, 'page': p,
#             'has_pages': pages.num_pages > 1,
#             'has_previous': p.has_previous(),
#             'has_next': p.has_next(),
#             'previous_page': p.previous_page_number(),
#             'next_page': p.next_page_number(),
#             'is_first': p == 1,
#             'is_last': p == pages.num_pages},
#             context_instance=RequestContext(request))

# @never_cache
# def restaurants_not_updated(request, page=None):
#     restaurants = Restaurant.objects.filter(last_updated__gte=(datetime.datetime.today() - datetime.timedelta(days=356)))
#     restaurants = restaurants.filter(active=True)
#     pages = Paginator(restaurants, ITEMS_PER_PAGE)
#     if page is None:
#         #set it to 1
#         page = 1
    
#     #get the page from the paginator
#     try:
#         p = pages.page(page)
#     except:
#         raise Http404

#     return render_to_response('restaurants/admin_new_restaurants.html',
#             {'restaurants': p.object_list,
#             'title': 'Restaurants Not Updated in 12 Months',
#             'to': 'restaurants_not_updated',
#             'page_range': pages.page_range,
#             'num_pages': pages.num_pages, 'page': p,
#             'has_pages': pages.num_pages > 1,
#             'has_previous': p.has_previous(),
#             'has_next': p.has_next(),
#             'previous_page': p.previous_page_number(),
#             'next_page': p.next_page_number(),
#             'is_first': p == 1,
#             'is_last': p == pages.num_pages},
#             context_instance=RequestContext(request))

# @never_cache
# def mark_restaurant_updated(request, restaurant, to, page=None):
#     restaurant = Restaurant.objects.get(id=restaurant)
#     restaurant.status = "UPDATED"
#     restaurant.last_updated = datetime.datetime.today()
#     restaurant.save()
#     if page is None: 
#         page = 1

#     return redirect(to, page=page)

@never_cache
def neighborhood_kml(request,neighborhood):
    neighborhood = Neighborhood.objects.get(name=neighborhood)
    soup = BeautifulSoup(neighborhood.geom.kml)
    tag = Tag(soup, "extrude")
    soup.polygon.insert(0, tag )
    text = "1"
    tag.insert(0, text)
    xml = str(soup )
    return render_to_response("restaurants/kml_template.html",{'neighborhood': neighborhood,"xml": xml}, context_instance=RequestContext(request))
    
@never_cache
def update_restaurant_form(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    if request.method != "POST":
        form = RestaurantForm(instance=restaurant)
    else:
        form = RestaurantForm( request.POST )
        if form.is_valid():
            cd = form_cleaned_data
            message = u'Name: ' + cd['name'] + '(' + restaurant.id +')\r\n'
            message += u'Address: ' + cd['address'] +'\r\n'
            message += u'City: ' + cd['city'] +'\r\n'
            message += u'State: ' + cd['state'] +'\r\n'
            message += u'Zip Code: ' + cd['zip_code'] +'\r\n'
            message += u'Website: ' + cd['website'] +'\r\n'
            message += u'Phone: ' + cd['phone'] +'\r\n'
            message += u'Hours: ' + cd['hours'] + '\r\n'
            message += u'Description: ' + cd['description'] + '\r\n'
            message += u'\r\n\r\n\r\nDebug Information\r\rUser Agent: ' + request.META['HTTP_USER_AGENT'] +'\r\n' 
            message += u'IP Address: ' + request.META['REMOTE_ADDR'] +'\r\n' 
            message += u'Referer: ' + request.META['HTTP_REFERER'] +'\r\n'
            
            send_mail(
                'News-Leader.com Restaurant:' +  restaurant.name + ' Submission: ' + str(cd['name']),
                message,
                'online@news-leader.com',
                [to,'tlane2@gannett.com','mpeterson4@gannett.com',],
                )

    return render_to_response('restaurants/update_restaurant_form.html',
        {
            'restaurant': restaurant,
            'form': form,
            #'submit': submit 
        }, context_instance=RequestContext(request))

@never_cache
def contest_entry(request):
    max_entries = 5
    message = ""
    if request.method != "POST":
        form = ContestForm()
    else:
        form = ContestForm( request.POST )
        if form.is_valid():
            cd = form.cleaned_data
            # contests_check = Contest.objects.filter(email=cd['email'])
            # if len(contests_check) > max_entries:
            #     #return HttpResponseRedirect("/restaurants/contest/error")
            #     message = "Sorry! You have already entered this contest " + str(max_entries) + " times with this email address."
            #     form = ContestForm(request.POST)
            # else:
        
            contest = Contest()
            contest.name = cd['name']
            contest.address = cd['address']
            contest.city = cd['city']
            contest.state = cd['state']
            contest.zip_code = cd['zip_code']
            contest.phone_number = cd['phone_number']
            contest.email = cd['email']
            contest.dob = cd['dob']
            contest.save()
            # message = u'Name: ' + cd['name'] + '\r\n'
            # message += u'Address: ' + cd['address'] +'\r\n'
            # message += u'City: ' + cd['city'] +'\r\n'
            # message += u'State: ' + cd['state'] +'\r\n'
            # message += u'Zip Code: ' + cd['zip_code'] +'\r\n'
            # message += u'Phone: ' + cd['phone_number'] +'\r\n'
            # message += u'Email: ' + cd['email'] + '\r\n'
            # message += u'Date of Birth: ' + cd['dob'] + '\r\n'
            # message += u'\r\n\r\n\r\nDebug Information\r\rUser Agent: ' + request.META['HTTP_USER_AGENT'] +'\r\n' 
            # message += u'IP Address: ' + request.META['REMOTE_ADDR'] +'\r\n' 
            # message += u'Referer: ' + request.META['HTTP_REFERER'] +'\r\n'
            
            # send_mail(
            #     'News-Leader.com Restaurant Contest Submission: ' + str(cd['name']),
            #     message,
            #     'online@news-leader.com',
            #     [to,'tlane2@gannett.com',],#'mpeterson4@gannett.com',],
            #     )

            return HttpResponseRedirect("/restaurants/contest/success")

    return render_to_response('restaurants/contest_entry.html',
        {
            'form': form,
            'message':message,
        }, context_instance=RequestContext(request))
@never_cache
def contest_error(request):
    #empty function to display a page.
    return render_to_response('restaurants/contest_error.html', context_instance=RequestContext(request))

@never_cache
def contest_success(request):
    #empty function to display page
    form = ContestForm()
    return render_to_response('restaurants/contest_success.html', {'form':form}, context_instance=RequestContext(request))
@never_cache
def nearme( request ):
    if request.is_ajax:

        lat = request.GET.get("lat")
        lng = request.GET.get("lng")
        #defaulting to city center if nothing is provided
        if lat is None and lng is None:
            P = Point( float( -93.292255 ), float(  37.208990 ) )
        else:
            P = Point( float( lng),float(lat) )
        #get all of the restaurants that have a cuisine and distance less than .5 miles from the point given. 
           
        restaurants = Restaurant.objects.filter( active=True,cuisine__isnull=False,geom__distance_lt=( P, D( mi= float( 0.5 ) ) ) ).distinct("id")
        counts = {}
        for restaurant in restaurants:
            print restaurant.name + " = " + restaurant.address 
            for cuisine in restaurant.cuisine.all():
                cuisine
                if counts.has_key(cuisine.name):
                    counts[cuisine.name] += 1
                else:
                    counts[cuisine.name] = 0
    
        return render_to_string('restaurants/mobile/nearme_detail.html',{'restaurants': counts,'num_restaurants':len(restaurants)}, context_instance=RequestContext(request))
    else:
        return render_to_response('restaurants/mobile/nearme.html', context_instance=RequestContext(request))
