# -*- coding:utf-8 -*-
#!/usr/bin/env python26
import os
import sys
import datetime
import time
# from django.contrib.gis.geos import fromstr
# from geopy import geocoders
from lib import bail,log_me,email_message
import socket

#django specific stuff
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from restaurants.models import Restaurant,Attribute


attributes = Attribute.objects.filter(name='payment methods accepted')
#good_list = ['casual','family friendly','formal','laid back','lively','quiet','romantic']
#i'll have to do this in stages.. get all of the checks fixed and then all of the cash and cards fixed finally
# good_list = ['debit','credit','debit cards','credit cards','credit and debit cards','debit and credit cards',
#             'major credit cards','credit or debit cards','major credit cards accepted','debit card','discover card',
#             'mastercard','american express','visa','not amex','no discover']

good_list = [ 'credit and/or debit cards','credit cards accepted']
for attribute in attributes:
    attr_string = ""
    vals = str(attribute.value).split(",")
    #print "%s vals in %s" % ( attribute.name, len(vals))
    count = 0
    for val in vals:
        count += 1
        #print "checking %s against good_list" % val
        #remove white space
        val = val.strip()
        if val in good_list:
            if not "credit and/or debit cards" in attr_string:
                attr_string  += "credit and/or debit cards"
                if count != len(vals):
                    #if it's not the end of the list, lets stick a comma on it
                    attr_string += ", "
        else:
            attr_string += val
            if count != len(vals):
                #if it's not the end of the list, lets stick a comma on it
                attr_string += ", "

    
    print "Updating the payment methods accepted with %s" % attr_string
    attribute.value = attr_string
    attribute.save()
    print "-------------------"