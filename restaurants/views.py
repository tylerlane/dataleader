# Create your views here
import datetime
#from django.contrib.gis.geos import Point
#from django.contrib.gis.measure import D
from django.core.paginator import Paginator
from django.db.models import Avg,Min,Max,Count,F,Q
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response,redirect
#from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils import simplejson
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from restaurants.models import Restaurant, Inspection, Cuisine, Attribute, Neighborhood, Featured, Gallery,Pageview
from restaurants.forms import SearchForm
#import re
#import simplejson
#from calls.textutils import *

#variable for items per page
ITEMS_PER_PAGE = 25


@never_cache
def index(request):
    main_featured = Featured.objects.all().order_by("-date")[0]
    main_featured.galleries = Gallery.objects.filter( restaurant = main_featured.restaurant )
    features = Featured.objects.all().order_by("?").exclude(restaurant=main_featured.restaurant)[0:1]
    for feature in features:
        feature.galleries = Gallery.objects.filter( restaurant=feature.restaurant )
    return render_to_response('restaurants/landingPage.html',
            {'features':features,"main_featured":main_featured},
            context_instance=RequestContext(request))


@never_cache
def detail(request, restaurant_id):
    restaurant = Restaurant.objects.select_related().get(id=restaurant_id)
    inspections = Inspection.objects.filter(restaurant=restaurant)
    #pull in our attributes
    restaurant.attributes = Attribute.objects.filter(restaurant=restaurant,active=True)
    restaurant.absolute_uri = request.build_absolute_uri()
    for attribute in restaurant.attributes:
        #replacing "_" with " "
        #attribute.name = " ".join(attribute.name.split("_"))
        #attribute.value = " ".join(attribute.value.split("_"))
        #if attribute.comma_delimited:
        if attribute.value[-1:] == ",":
            attribute.value = attribute.value[0:-2]
    if restaurant.rating is None:
        restaurant.rating = "0"
    pageview = Pageview(restaurant=restaurant)
    pageview.save()



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
    if letter != "%23":
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
            #now we delete the old restaurant<h2>Inside Details</h2>

            restaurant.delete()

    #get the letter of the main restaurant to redirect us to the first page of
    #listings
    letter = main_restaurant.name[0].upper()
    return HttpResponseRedirect('/restaurants/merge/' + letter + '/1')


@never_cache
def list_cuisines(request):
    cuisines = Cuisine.objects.all()
    title = "Cuisines"
    return render_to_response('restaurants/listcuisines.html',
            {'cuisines': cuisines, "title": title},
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

@never_cache
def record_rating_vote(request, restaurant, rating):
    #function to records the votes. should only be called via ajax.
    restaurant = Restaurant.objects.get(restaurant = restaurant)
    restaurant.rating_sum += rating
    restaurant.rating_total_votes += 1
    restaurant.save()

@never_cache
def list_attributes(request):
    attributes = Attribute.objects.values("name").distinct()
    
    return render_to_response('restaurants/listattributes.html',
            {'attributes':attributes,'title':'Browse By:'},
            context_instance=RequestContext(request))

@never_cache
def list_attribute_values(request, attribute):
    attributes = Attribute.objects.filter(name=attribute).values("name","value").distinct()
    title = "<b>%s</b>" % attribute
    for attribute in attributes:
        if attribute["name"] =="average entree price":
            if attribute["value"] == "very inexpensive":
                attribute["order"] = 1
            elif attribute["value"]  == "inexpensive":
                attribute["order"] = 2
            elif attribute["value"]  == "moderate":
                attribute["order"] = 3
            elif attribute["value"]  == "expensive":
                attribute["order"] = 4
            elif attribute["value"]  == "very expensive":
                attribute["order"] = 5
        else:
            attribute["order"] = 1

    return render_to_response('restaurants/listattributevalues.html',
            {'attributes':attributes, "title":title},
            context_instance=RequestContext(request))

@never_cache
def list_restaurants_attribute(request, attribute, value):
    attributes = Attribute.objects.filter(name=attribute, value=value)
    restaurants = []
    for attribute in attributes:
        tmp = Restaurant.objects.get(id=attribute.restaurant.id)
        restaurants.append(tmp)
    #restaurants = Restaurant.objects.filter(id__in=restaurants)
    title = "<b>%s</b> : <i>%s</i>" % (attribute, value)
    return render_to_response('restaurants/restaurantListing.html',
            {'restaurants': restaurants,'title':title},
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
                restaurant.rating_sum = restaurant.rating_sum + float(request.POST.get("rating"))
            if restaurant.rating_total_votes is None:
                restaurant.rating_total_votes = 1
            else:
                restaurant.rating_total_votes += 1
            restaurant.save()
            #print "saving vote"
            #print "Sum: %s" % restaurant.rating_sum
            #print "Total Votes: %s" % restaurant.rating_total_votes
            rating = (float(restaurant.rating_sum) / float(restaurant.rating_total_votes) )
            #rating_dict = {"rating":rating}
            return HttpResponse(rating)
    else:
        return HttpResponse(status="400")

@never_cache
def display_top_rated(request):
    restaurants = Restaurant.objects.filter(active=True,rating__isnull=False).order_by('rating')
    restaurants = restaurants[0:20]
    title = "Top Rated Restaurants"
    
    return render_to_response('restaurants/restaurantListing.html',
            {'restaurants': restaurants,'title': title},
            context_instance=RequestContext(request))

@never_cache
def display_most_viewed(request):
    #get pageviews
    pvs = Pageview.objects.filter(time_init__range =
            (datetime.datetime.today() - datetime.timedelta(seconds=2592000),
            datetime.datetime.today()))
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
    title = "Most Viewed Restaurants"
    return  render_to_response('restaurants/restaurantListing.html',
            {'restaurants': restaurants,'title': title },
            context_instance=RequestContext(request))

@never_cache
def new_restaurants(request, page=None):
    restaurants = Restaurant.objects.filter(status="NEW")
    pages = Paginator(restaurants, ITEMS_PER_PAGE)
    if page is None:
        #set it to 1
        page = 1
    
    #get the page from the paginator
    try:
        p = pages.page(page)
    except:
        raise Http404

    return render_to_response('restaurants/admin_new_restaurants.html',
            {'restaurants': p.object_list,
            'title': 'New Restaurants',
            'to': 'new_restaurants_admin',
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
def restaurants_not_updated(request, page=None):
    restaurants = Restaurant.objects.filter(last_updated__gte=(datetime.datetime.today() - datetime.timedelta(days=356)))

    pages = Paginator(restaurants, ITEMS_PER_PAGE)
    if page is None:
        #set it to 1
        page = 1
    
    #get the page from the paginator
    try:
        p = pages.page(page)
    except:
        raise Http404

    return render_to_response('restaurants/admin_new_restaurants.html',
            {'restaurants': p.object_list,
            'title': 'Restaurants Not Updated in 12 Months',
            'to': 'restaurants_not_updated',
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
def mark_restaurant_updated(request, restaurant,to, page=None):
    restaurant = Restaurant.objects.get(id=restaurant)
    restaurant.status = "UPDATED"
    restaurant.last_updated = datetime.datetime.today()
    restaurant.save()
    if page is None: 
        page = 1

    return redirect(to, page=page)