# Create your views here.
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson
from models import School,District,AYPDetail,AYPSummary


def display_ayp( request ):
    if "district" not in request.GET:
        district = "SPRINGFIELD R-XII"
    else:
        district = request.GET["district"]

    districts = District.objects.filter( active = True ).order_by('name')

    return render_to_response( 'schools/ayp.html', { 'districts': districts, 'district': district }, context_instance = RequestContext( request ) )

def get_schools( request ):
    if "school_type" not in request.GET:
        school_type = "high"
    else:
        school_type = request.GET["school_type"]

    if "district" not in request.GET:
        district = "SPRINGFIELD R-XII"
    else:
        district = request.GET["district"]
    schools = School.objects.filter( district = District.objects.get( name= district ) ).order_by( 'school_type','name' )
    districts = District.objects.filter( active = True ).order_by('name')
    return render_to_response( 'schools/school_detail.html', {'schools': schools, 'district': district, 'districts': districts, 'school_name': schools[0].name }, context_instance = RequestContext( request ) )

def get_school_ayp_xml( request, district = None, school = None ):
    if district is None:
        district = "SPRINGFIELD R-XII"
    if school is None:
        if "school" not in request.GET:
            schools = School.objects.filter( district = District.objects.get( name = district ) )
            school = schools[0].name
        else:
            school = request.GET["school"]
    school = School.objects.get( name = school, district = District.objects.get( name = district ) )
    details = AYPDetail.objects.filter( school = school ).order_by( "year" )

    chart_string = "<chart>"
    chart_string += "<license>ETA6GP4F771O.945CWK-2XOI1X0-7L</license>"
    chart_string += "<chart_type>line</chart_type>"
    chart_string += "<chart_data>"
    chart_string += "<row>"
    chart_string += "<null />"
    chart_string += "<string>2006</string>"
    chart_string += "<string>2007</string>"
    chart_string += "<string>2008</string>"
    chart_string += "<string>2009</string>"
    chart_string += "<string>2010</string>"
    chart_string += "<string>2011</string>"
    chart_string += "</row>"

    #communication arts
    chart_string += "<row>"
    chart_string += "<string>Communication Arts</string>"
    for detail in details:
        chart_string += "<number tooltip=\"%s\">%f</number>" % ( "Communication Arts", detail.comm_school_total )
    chart_string += "</row>"
    
    #math
    chart_string += "<row>"
    chart_string += "<string>Mathematics</string>"
    for detail in details:
            chart_string += "<number tooltip=\"%s\">%f</number>" % ( "Mathematics", detail.math_school_total )
    chart_string += "</row>"
    
    #attendance
    chart_string += "<row>"
    chart_string += "<string>Attendance</string>"
    for detail in details:
            chart_string += "<number tooltip=\"%s\">%f</number>" % ("Attendance", detail.attendance_pct )
    chart_string += "</row>"
    
    if school.school_type == "high":
        #graduation
        chart_string += "<row>"
        chart_string += "<string>Graduation</string>"
        for detail in details:
                chart_string += "<number tooltip=\"%s\">%f</number>" % ("Graduation", detail.graduation_pct )
        chart_string += "</row>"
    chart_string += "</chart_data>"
    chart_string += "<draw><text shadow='high' size='24' x='20' y='-35' width='400' height='75' h_align='center' v_align='bottom'>%s</text></draw>" % str(school).title()
    chart_string += "<legend layout='vertical' y='250' />"
    chart_string += """<chart_guide horizontal='true'
                    vertical='false'
                    thickness='1' 
                    color='ff4400' 
                    alpha='75' 
                    type='dashed' 
                    radius='8'
                    fill_alpha='0'
                    line_color='ff4400'
                    line_alpha='75'
                    line_thickness='4'
                    size='10'
                    text_color='ffffff'
                    background_color='ff4400'
                    text_h_alpha='90'
                    text_v_alpha='90' 
                    />"""
    chart_string += "<link_data url='' />"
    chart_string += """<axis_value min='0'  
                max='100' 
                mode='stretch'  
                suffix='%' 
                show_min='false' 
                   />"""
    chart_string += "<chart_label position='cursor' />"
    chart_string += "</chart>"

    return HttpResponse( chart_string, content_type="application/xml" )

def ayp_xml( request, school_type = None, district = None ):
    chart_string = "<chart>"
    chart_string += "<license>ETA6GP4F771O.945CWK-2XOI1X0-7L</license>"
    chart_string += "<chart_type>line</chart_type>"
    chart_string += "<chart_data>"
    chart_string += "<row>"
    chart_string += "<null />"
    chart_string += "<string>2006</string>"
    chart_string += "<string>2007</string>"
    chart_string += "<string>2008</string>"
    chart_string += "<string>2009</string>"
    chart_string += "<string>2010</string>"
    chart_string += "<string>2011</string>"
    chart_string += "</row>"
    #now our data
    if "school_type" in request.GET and request.GET["school_type"]:
        schl_type = request.GET["school_type"]
    else:
        schl_type = "high"
    if district is None:
        if "district" in request.GET:
            schools = School.objects.filter( district = District.objects.filter( name = request.GET["district"].upper() ), active=True, school_type=schl_type )
        else:
            schools = School.objects.filter( district = District.objects.filter( name = "SPRINGFIELD R-XII" ), active= True, school_type=schl_type )
    else:
        schools = School.objects.all( school_type= "high", active= True )
    for school in schools: 
        details = AYPDetail.objects.filter( school = school ).order_by( 'year' )
        chart_string += "<row>"
        chart_string += "<string>%s</string>" % school.name
        for detail in details:
            if "display_type" in request.GET and request.GET["display_type"]:
                if request.GET["display_type"] == "comm_arts":
                    if detail.comm_school_total is None:
                        detail.comm_school_total = 0
                    chart_string += "<number tooltip=\"%s\">%f</number>" % ( str( school.name ).title(), detail.comm_school_total )
                elif request.GET["display_type"] == "math":
                    if detail.math_school_total is None:
                        detail.math_school_total = 0
                    chart_string += "<number tooltip=\"%s\">%f</number>" % ( str( school.name ).title(), detail.math_school_total )
                elif request.GET["display_type"] == "attendance":
                    if detail.attendance_pct is None:
                        detail.attendance_pct = 0
                    chart_string += "<number tooltip=\"%s\">%f</number>" % ( str( school.name ).title(), detail.attendance_pct )
                elif request.GET["display_type"] == "graduation":
                    if detail.graduation_pct is None:
                        detail.graduation_pct = 0
                    chart_string += "<number tooltip=\"%s\">%f</number>" % ( str( school.name ).title(), detail.graduation_pct )
            else:
                #default to comm_arts
                chart_string += "<number tooltip=\"%s\">%f</number>" % ( str( school.name ).title(), detail.comm_school_total )
        chart_string += "</row>"
    if "display_type" in request.GET:
        if request.GET["display_type"] == "comm_arts":
            chart_lbl = "Communication Arts"
        elif request.GET["display_type"] == "math":
            chart_lbl = "Mathematics"
        elif request.GET["display_type"] == "attendance":
            chart_lbl = "Attendance"
        elif request.GET["display_type"] == "graduation":
            chart_lbl = "Graduation"
    else:
        chart_lbl = "Communication Arts"
    chart_string += "</chart_data>"
    chart_string += "<draw><text shadow='high' size='24' x='20' y='-35' width='400' height='75' h_align='center' v_align='bottom'>%s</text></draw>" % chart_lbl
    chart_string += "<legend layout='hide' />"
    chart_string += """<chart_guide horizontal='true'
                    vertical='false'
                    thickness='1' 
                    color='ff4400' 
                    alpha='75' 
                    type='dashed' 
                    radius='8'
                    fill_alpha='0'
                    line_color='ff4400'
                    line_alpha='75'
                    line_thickness='4'
                    size='10'
                    text_color='ffffff'
                    background_color='ff4400'
                    text_h_alpha='90'
                    text_v_alpha='90'
                    />"""
    chart_string += "<link_data url='' />"
    chart_string += """<axis_value min='0'
                max='100'
                mode='stretch'
                suffix='%'
                show_min='false'
                   />"""
    chart_string += "<chart_label position='cursor' />"
    chart_string += "</chart>"
    
    
    return HttpResponse( chart_string, content_type='application/xml' )
