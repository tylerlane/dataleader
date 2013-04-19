#!/usr/bin/env python

import feedparser
from BeautifulSoup import BeautifulSoup
import ftplib
url = 'http://conmiorss.gannettonline.com/apps/pbcs.dll/section?Category=conmiorss&site=DO&cat=HEYMOM12&dys=999&nocache=1&mime=xml'
UPLOAD_HOST = "ftp3.moc.gbahn.net"
UPLOAD_USERNAME = "springfield-cms"
UPLOAD_PASSWORD = "b17biuT$"
UPLOAD_PATH = "/moc.news-leader.com/home/momcalendar"
TEMP_PATH = "/tmp/"

feed = feedparser.parse(url)

# we are going to assume that we will ONLY have one entry in the list of stories. we will work with the feed
# to make sure of this
story_text = feed.entries[0].content[0].value

#now that we have the text, lets do something with it.
soup = BeautifulSoup(story_text)

#now that its in beautifulsoup lets get all the p tags
ps = soup.findAll("p")
#and loop through them
cal_string = ""
#loop through our items and build the calendar text
for p in ps:
	#if the p tag has a bold tag in it. we will print it out a little different
	if p.findChild("b"):
		cal_string += "<li class=\"sep\">" + p.findChild("b").contents[0]  + "</li>\r\n"
	else:
		cal_string += "<li><a href=\"#detail\">" + str(p.contents[0]).replace("&amp;amp;", "&amp;") + " </a></li>\r\n"


#wrapper for the rest of the calendar text
cal_output = """
<html>
	<head>
		<meta charset="UTF-8" />
		<link title="Apple" href="themes/css/apple.css" rel="stylesheet">
		<script src="src/lib/zepto.min.js" type="text/javascript" charset="utf-8"></script>
		<script src="src/jqtouch.min.js" type="text/javascript" charset="utf-8"></script>
		<title>Hey MOM </title>
		<script type="text/javascript" charset="utf-8">
		var jQT = new $.jQTouch({
	        icon: 'jqtouch.png',
	        icon4: 'jqtouch4.png',
	        addGlossToIcon: false,
	        preloadImages: []
	    });
	    $(function(){

	        $("ul li a").click( function(){
	        	$("#detail_content").html( $(this).html());
	        	$("#title").html()

	        });
	        
	    });
		</script>
	 	<style type="text/css" media="screen">
	        #jqt.fullscreen #home .info {
	            display: none;
	        }
	        div#jqt #about {
	            padding: 100px 10px 40px;
	            text-shadow: rgba(0, 0, 0, 0.3) 0px -1px 0;
	            color: #999;
	            font-size: 13px;
	            text-align: center;
	            background: #161618;
	        }
	        div#jqt #about p {
	            margin-bottom: 8px;
	        }
	        div#jqt #about a {
	            color: #fff;
	            font-weight: bold;
	            text-decoration: none;
	        }
	    </style>
	</head>
	<body>
	    <div id="jqt">
	        <div id="about" class="selectable">
	                <p><img src="jqtouch.png" /></p>
	                <p><strong>jQTouch</strong><br>Version 1.0 beta<br>
	                    <a href="http://www.davidkaneda.com">By David Kaneda</a></p>
	                <p><em>Create powerful mobile apps with<br> just HTML, CSS, and jQuery.</em></p>
	                <p>
	                    <a target="_blank" href="http://twitter.com/jqtouch">@jQTouch on Twitter</a>
	                </p>
	                <p><br><br><a href="#" class="grayButton goback">Close</a></p>
	        </div>
	 		<div id="home" class="current">
	            <div class="toolbar">
	                <h1>7 Day Planner</h1>
	                <a class="back" href="http://m.news-leader.com">Home</a>
	            </div>
	            <ul class="edgetoedge scroll">
	            	<div style="width:400px;">
	            		<img src="http://www.news-leader.com/misc/heymom/HeyMomHeaderLogo-cropped.jpg" style="margin-left:auto;margin-right:auto;padding:5px;"/>
	            	</div>
	          		"""
#stick the calendar entries into the text
cal_output += cal_string
cal_output += """
	        </div>
	        <div id="detail" class="selectable">
	        	<div class="toolbar">
	                <h1>7 Day Planner</h1>
	                <a class="back" href="#">Back</a>
	            </div>
	        	
	        	<div class="scroll">
                    <h2 id='title'>Detail</h2>
                    <ul class="rounded">
                        <li id="detail_content"></li>
                    </ul>
                </div>
	       	</div>
	    </div>
	</body>
</html>"""
#replace the html codes with proper > and < and &'s
cal_output = str(cal_output).replace( "&gt;", ">").replace( "&lt;", "<").replace( "&amp;", "&")
# print cal_output

print "making our FTP connection"
ftp = ftplib.FTP()
ftp.connect( UPLOAD_HOST, 21 )
ftp.login( UPLOAD_USERNAME, UPLOAD_PASSWORD )
# move to the desired upload directory
ftp.cwd( UPLOAD_PATH )

print "Generating the new calendar file"
fh = open( TEMP_PATH + "/cal_temp.html", "w" )
fh.write( cal_output )
fh.close()

print "Uploading calendar!",
fh = open( TEMP_PATH + "/cal_temp.html" , 'rb' )
ftp.storbinary( 'STOR ' + "calendar.html", fh )
fh.close()
print "File Uploaded Successfully"

#closing our FTP connection
print "closing FTP connection"
ftp.quit()
