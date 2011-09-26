# Create your views here.

from calls.models import Call,CallType,Jurisdiction
import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.db.models import Avg,Min,Max,Count,F,Q
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from models import Story,Keyword,Pageview
import simplejson
from warrants.models import Warrant,Court


@never_cache
def dataredirect( request ):
    #redirecting to the dataleader page.
    return HttpResponseRedirect("http://www.news-leader.com/section/DATA")

@never_cache
def faviconredirect( request ):
    #redirect to the favicon
    return HttpResponseRedirect("http://php.news-leader.com/favicon.ico")

@login_required
@user_passes_test( lambda u: u.is_staff )
@never_cache
def infocenter_landingpage( request ):
    return render_to_response( "infocenter_landingpage.html", context_instance = RequestContext( request ) )

@never_cache
def landing_page( request ):
    ################
    #stories section
    ################
    stories = Story.objects.filter( date_published__gte=datetime.datetime.today() - datetime.timedelta(days=10),active=True, keyword__keyword='crime' ).order_by( '-date_published')
    ##############
    #calls section
    ##############
    #start with our base object
    #this will pull in the last 24 hours worth of calls.
    #putting in geom__isnull cause we ONLY care about calls that have a a lat/lng
    calls = Call.objects.filter(call_time__gte=datetime.datetime.today() - datetime.timedelta(days=1), geom__isnull=False).order_by('-call_time')
    #going to try this. for some reason, there are a few calls that get geocoding WAY outside the city limits. so i'm going to do a search from downtown and limit the distance to 5 or 8 miles.
    # this will include the whole city but not give us our funky calls.
    P = Point( float( -93.292255 ), float(  37.208990 ) )
    calls = calls.filter( geom__distance_lt=( P, D( mi= float( 8 ) ) ) )
    calltypes = CallType.objects.filter(call__in=calls).values('category').annotate(count=Count('call')).distinct()
    categories = {}
    for calltype in calltypes:
        if calltype["category"] not in categories.keys():
            categories[ calltype["category"] ] = {}
            categories[ calltype["category"] ][ "name" ] = calltype["category"]
            categories[ calltype["category"] ][ "count" ] = 0
        categories[ calltype["category"] ]["count"] += calltype["count"]
    
    categories2 = []
    #make it readable for my template
    for category in categories:
        categories2.append( categories[category] )
    
    #################
    #Warrants section
    #################
    greene_county = Court.objects.get(description="Greene County")
    spf_municipal = Court.objects.get(description="Springfield Municipal")
    greene_warrant_counts = Warrant.objects.filter(court=greene_county,active=True).values("warrant_type").annotate(count=Count('warrant_type')).order_by('-count')
    spf_warrant_counts =  Warrant.objects.filter(court=spf_municipal,active=True).values("warrant_type").annotate(count=Count('warrant_type')).order_by('-count')
    
    warrants = {}
    for warrant in greene_warrant_counts:
        warrants[warrant["warrant_type"]] = {}
        warrants[warrant["warrant_type"]]["warrant_type"] = warrant["warrant_type"]
        warrants[warrant["warrant_type"]]["count"] = warrant["count"]
    #for warrant in spf_warrant_counts:
    #   warrants[warrant["warrant_type"]] = {}
    #   warrants[warrant["warrant_type"]]["warrant_type"] = warrant["warrant_type"]
    #   warrants[warrant["warrant_type"]]["count"] = warrant["count"]
    
    warrants2 = []
    for warrant in warrants:
        warrants2.append(warrants[warrant])
        
    return render_to_response( "landing_page.html", {"call_categories": simplejson.dumps(categories2),"warrants": simplejson.dumps(warrants2), "stories": stories },context_instance=RequestContext(request))

@never_cache
def story_pageview( request, story_id, headline=None ):
    #skipping the first 4 characters of the story_id cause its the year which we don't need
    story, created = Story.objects.get_or_create( id = story_id[4:],defaults={ 'date_published': datetime.datetime.today() } )
    if created:
        #checking to see if headline was passed to the story or not
        if headline is not None:
            story.headline = headline
        if "HTTP_REFERER" in request.META.keys():
            if len(request.META["HTTP_REFERER"]) < 200:
                story.long_url = request.META["HTTP_REFERER"]
        story.short_url = "http://www.news-leader.com/article/%s" % ( story_id )
        #print "Story %s created" % story_id
        story.save()
    else:
        if headline is not None:
            story.headline = headline
            if "HTTP_REFERER" in request.META.keys():
                story.long_url = request.META["HTTP_REFERER"]
            story.short_url = "http://www.news-leader.com/article/%s" % ( story_id )
                
            story.save()
    pageview = Pageview()
    pageview.story = story
    pageview.save()
    
    return HttpResponse( "" )
    
@login_required
@user_passes_test( lambda u: u.is_staff )
@never_cache
def list_pageviews( request, big = False ):
    #not sure if i like this view yet. mainly cause it has 2 returns and i generally don't like that. later i may move this into 2 seperate functions.
    if request.is_ajax():
        if "minutes" in request.GET.keys():
            pvs = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( seconds = ( int( request.GET["minutes"] ) * 60 ) ), datetime.datetime.today() ) )
        else:
            pvs = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( days=1 ), datetime.datetime.today() ) )
        pvs = pvs.values('story').annotate(pageviews=Count('id')).order_by('story')
        for pv in pvs:
            pv['story'] = Story.objects.get( id = pv['story'] )
        #print pvs.query
        return render_to_response( 'stories/pageviews_detail.html', { 'pvs': pvs } )
        
    else:
        pvs = Pageview.objects.filter( time_init__gte=datetime.datetime.today() - datetime.timedelta(hours=1))
        pvs = pvs.values('story').annotate(pageviews=Count('story')).order_by('story')
        for pv in pvs:
            pv['story'] = Story.objects.get( id = pv['story'] )
        if big is False:
            return render_to_response( "stories/pageviews.html",{"pvs":pvs }, context_instance = RequestContext( request ) )
        else:
            return render_to_response( "stories/pageviews_big.html",{"pvs":pvs }, context_instance = RequestContext( request ) )
            
@never_cache
def list_pageviews_json( request ):
    if "minutes" in request.GET.keys():
        pvs = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( seconds = ( int( request.GET["minutes"] ) * 60 ) ), datetime.datetime.today() ) )
    else:
        pvs = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( days=1 ), datetime.datetime.today() ) )
    pvs = pvs.values('story').annotate(pageviews=Count('id')).order_by('story')
    for pv in pvs:
        pv['story'] = Story.objects.get( id = pv['story'] )
    json = {
        'pvs' : pvs,
    }
    return render_to_string( simplejson.dumps( json ) )

@never_cache
def pageviews_widget( request ):
    #need 4 different query sets.
    today = datetime.datetime.today()
    today_stories = Pageview.objects.filter( time_init__year = today.strftime( "%Y"), time_init__month=today.strftime( "%m"), time_init__day=today.strftime( "%d") )
    today_stories = today_stories.values( 'story' ).annotate( pageviews=Count('id')).order_by('story')
    for story in today_stories:
        story['story'] = Story.objects.get( id= story['story'] )
    
    yesterday = datetime.datetime.today() - datetime.timedelta( days=1 )
    yesterday_stories = Pageview.objects.filter( time_init__year = yesterday.strftime( "%Y"), time_init__month=yesterday.strftime( "%m"), time_init__day=yesterday.strftime( "%d") )    
    #yesterday_stories = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( days = 2 ), datetime.datetime.today() - datetime.timedelta( days = 1 ) ) )
    yesterday_stories = yesterday_stories.values( 'story' ).annotate( pageviews=Count('id')).order_by('story')
    for story in yesterday_stories:
        story['story'] = Story.objects.get( id= story['story'] )
    
    
    week_stories = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( days = 7 ),datetime.datetime.today() ) )
    week_stories = week_stories.values( 'story' ).annotate( pageviews=Count('id')).order_by('story')
    for story in week_stories:
        story['story'] = Story.objects.get( id= story['story'] )

    
    month_stories = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( days = 30 ), datetime.datetime.today() ) )
    month_stories = month_stories.values( 'story' ).annotate( pageviews=Count('id')).order_by('story')
    for story in month_stories:
        story['story'] = Story.objects.get( id= story['story'] )

    
    return render_to_response( 'stories/pageviews_widget.html',{'today_stories': today_stories, 'yesterday_stories': yesterday_stories, 'week_stories': week_stories, 'month_stories': month_stories }, context_instance = RequestContext( request ) )

@login_required
@user_passes_test( lambda u: u.is_staff )
@never_cache
def list_featured_stories( request ):
    message = None
    #if its a POST request.
    if request.method == "POST":
        checked_stories = request.POST.getlist( "stories" )
        #marking our stories as featured
        
        if len( checked_stories ) > 0:
            #unchecking all of the old featured stories
            old_stories = Story.objects.filter( featured = True )
            for story in old_stories:
                story.featured = False
                story.save()
            
            for story_id in checked_stories:
                story = Story.objects.get( id = story_id )
                story.featured = True
                story.save()
            message = "Featured Stories updated!"
            
        
    #get the current featured stories first
    current_features = Story.objects.filter( featured=True )
    #then get the latest stories
    today = datetime.datetime.today()
    today_stories = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( seconds = 2700 ), datetime.datetime.today() ) ).exclude( story__featured = True )
    today_stories = today_stories.values( 'story' ).annotate( pageviews = Count( 'id' ) ).order_by( 'story' )
    for foo in today_stories:
        foo[ 'story' ] = Story.objects.get( id = foo[ 'story' ] )
        
    #today_stories = Story.objects.filter( date_published__year = today.strftime( "%Y"), date_published__month=today.strftime( "%m" ), date_published__day = today.strftime( "%d" ) ).order_by( "-date_published" )
    #if there are no stories for today. then we'll just get the last 20 stories
    if len( today_stories ) == 0:
        today_stories = Story.objects.all().order_by("-date_published")[:20]

    return render_to_response( 'stories/list_featured_stories.html', { 'current_features': current_features, 'today_stories': today_stories, 'message': message }, context_instance = RequestContext( request ) )

@never_cache
def front_page_stories_widget( request ):
    #get the featured stories first
    featured = Story.objects.filter( featured = True )
    now = datetime.datetime.today()
    pvs = Pageview.objects.filter( time_init__range = ( datetime.datetime.today() - datetime.timedelta( seconds = 2700 ), datetime.datetime.today() ) ).exclude( story__featured = True )
    pvs = pvs.values( 'story' ).annotate( pageviews = Count( 'id' ) ).order_by( 'story' )
    
    stories = Story.objects.filter( featured = False ).order_by( '-date_published' )[:15]
    for pv in pvs:
        pv[ 'story' ] = Story.objects.get( id = pv[ 'story' ] )
        
        
    return render_to_response( 'stories/front_page_stories_widget.html',{'featured': featured, 'pvs': pvs, 'stories': stories }, context_instance = RequestContext( request ) )
    
    
