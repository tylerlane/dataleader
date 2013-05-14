#!/usr/bin/env python
import sys
import datetime
import time

import socket
#seeing which path to use.
#from BeautifulSoup import BeautifulSoup
import urllib2
import urllib

import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders



def send_mail(send_from, send_to, subject, text, f=None, server="localhost"):
    # assert type(send_to)==list
    # assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )
    if f is not None:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

#this will pull in our page.
# url = 'http://www.springfieldmo.gov/spd/HowDoI/spd_calls_results.jsp'
url = "http://www.springfieldmo.gov/spd/generalinfo/mediareport/mediareport.pdf"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#have to set the refer or it will error out. kind of stupid but whatever.
headers = { "User-Agent" : user_agent, "Referer": "http://www.google.com" }
# data = urllib.urlencode( params )
# print data
try:
    req = urllib2.Request( url, headers=headers )
    response = urllib2.urlopen( req )
    # the_page = response.read()
    localFile = open('/tmp/mediareport.pdf', 'w')
    localFile.write(response.read())
    localFile.close()
except:
    send_mail('data@news-leader.com','webeditor@news-leader.com;spokin@gannett.com','SGF Police - Media Report','No media report was found.\r\nContact the front desk of the Springfield Police Department at 864-1810. Paper copies are available at the front desk daily even if the online version is not updated. The front desk is open 7 a.m. to 11 p.m. daily.')
    #pass
else:
    # email_message('Online Staff','tlane@news-leader.com','911 Calls Importer','python@nolongervalid.com','911 Calls Import: ' + today.strftime("%m-%d-%Y %I:%M %p"), output)
    send_mail('data@news-leader.com','webeditor@news-leader.com;spokin@gannett.com','SGF Police - Media Report','Here is the media report\r\nIf this report is not up to date, contact the front desk of the Springfield Police Department at 864-1810. Paper copies are avaliable at the front desk  daily even if the online version is not updated. The front desk is open from 7 a.m. to 11 p.m. daily.','/tmp/mediareport.pdf')
