#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import urllib
import jinja2
import os
import datetime
import wsgiref.handlers

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import db
from google.appengine.api import users


class Persons(db.Expando):
	pid = db.StringProperty(required=True)
	name = db.StringProperty(required=True)
	user_class = db.StringProperty(required=True)
	email = db.EmailProperty(required=True)

class MainPage(webapp2.RequestHandler):
  def get(self):
	upload_url = blobstore.create_upload_url('/upload')
	self.response.out.write('''
		<!doctype html>
	<html>
		<head>
			<meta charset="UTF-8" />
			<title>RollCall@DHS</title>
			 <link rel="stylesheet" href="/static/themes/css/vanilla.css">
			<script src="/static/src/lib/zepto.min.js" type="text/javascript" charset="utf-8"></script>
			<script src="/static/src/jqtouch.min.js" type="text/javascript" charset="utf-8"></script>
			

			<script src="/static/extensions/jqt.autotitles.min.js" type="application/x-javascript" charset="utf-8"></script>

			<script type="text/javascript" charset="utf-8">
				var jQT = new $.jQTouch({
					useFastTouch: false,
					icon: 'jqtouch.png',
					addGlossToIcon: false,
					startupScreen: 'jqt_startup.png',
					statusBar: 'black'
				});
			</script>
		</head>
		<body>
			<div id="jqt">
				<div id="page1">
					<div class="toolbar">
						<h1>RollCall</h1>
					</div>
					<ul class="edgetoedge">
						<li><a href="#attendance">Attendance Taking</a></li>
						<li><a href="#leaveform">Leave Form</a></li>
						<li><a href="#mc">MC Submission</a></li>
					</ul>
				</div>
				<div id="attendance">
					<div class="toolbar">
						<a href="#" class="back">Back</a>
						<h1><!-- Will be filled in --></h1>
					</div>
					<div class="info">
						<ul class = "edgetoedge">
							<li><a href="#13y1a">13Y1A</a></li>
						</ul>
					</div>
				</div>
				<div id="13y1a">
					<div class="toolbar">
						<a href="#" class="back">Back</a>
						<h1><!-- Will be filled in --></h1>
					</div>
					<div class="info">
						<form class ="form" method ="post" action="13y1a">
							<p align="right">1 AMANDA ANG XIN RONG <input type = "checkbox" value = "13Y1A1"></p>
							<p align="right">2 AMIDALA LEE JIEYI<input type = "checkbox" value = "13Y1A2"></p>
							<p align="right">3 ANG XIN LING ADELLE<input type = "checkbox" value = "13Y1A3"></p>
							<p align="right">4 CHAN KE QING<input type = "checkbox" value = "13Y1A4"></p>
							<p align="right">5 CHEN JING<input type = "checkbox" value = "13Y1A5"></p>
							<p align="right">6 CHEONG JIA YUN BRENDA<input type = "checkbox" value = "13Y1A6"></p>
							<p align="right">7 CHERYL POH JINGTING<input type = "checkbox" value = "13Y1A7"></p>
							<p align="right">8 CHIN NGIOK YONG<input type = "checkbox" value = "13Y1A8"></p>
							<p align="right">9 CHLOE KANG YUN HUI<input type = "checkbox" value = "13Y1A9"></p>
							<p align="right">10 CHUA JIA RONG<input type = "checkbox" value = "13Y1A10"></p>
							<p align="right">11 HSU YI-NING<input type = "checkbox" value = "13Y1A11"></p>
							<p align="right">12 LOH WEN YU<input type = "checkbox" value = "13Y1A12"></p>
							<p align="right">13 LOW YUAN JIA DANNICA<input type = "checkbox" value = "13Y1A13"></p>
							<p align="right">14 MAN WAI TING<input type = "checkbox" value = "13Y1A14"></p>
							<p align="right">15 NG CUI TING CHRISTINE<input type = "checkbox" value = "13Y1A15"></p>
							<p align="right">16 RACHEL NG MIN YEE<input type = "checkbox" value = "13Y1A16"></p>
							<p align="right">17 SNG QIWEN<input type = "checkbox" value = "13Y1A17"></p>
							<p align="right">18 TAN SI JIE<input type = "checkbox" value = "13Y1A18"></p>
							<p align="right">19 TAN WEI SHUANG<input type = "checkbox" value = "13Y1A19"></p>
							<p align="right">20 VICTORIA QUEK XIAOXUAN<input type = "checkbox" value = "13Y1A20"></p>
							<p align="right">21 YANG YUE SHAN<input type = "checkbox" value = "13Y1A21"></p>
							<p align="right">22 CHUA LIANG WEI COLLIN<input type = "checkbox" value = "13Y1A22"></p>
							<p align="right">23 DARREN CHEE ZHE LIANG<input type = "checkbox" value = "13Y1A23"></p>
							<p align="right">24 DEE MU RUI MARCUS<input type = "checkbox" value = "13Y1A24"></p>
							<p align="right">25 EE ANSHENG<input type = "checkbox" value = "13Y1A25"></p>
							<p align="right">26 FOONG HAO HAN ISAAC<input type = "checkbox" value = "13Y1A26"></p>
							<p align="right">27 GAN RUI YI<input type = "checkbox" value = "13Y1A27"></p>
							<p align="right">28 JEREMY CHAN KWANG JIE<input type = "checkbox" value = "13Y1A28"></p>
							<p align="right">29 LIU ZIXIN<input type = "checkbox" value = "13Y1A29"></p>
							<p align="right">30 NG TZE ANN JONATHAN<input type = "checkbox" value = "13Y1A30"></p>
							<p align="right">31 NIGEL TAN YI CHER<input type = "checkbox" value = "13Y1A31"></p>
							<p align="right">32 RYAN LIM ZI AN<input type = "checkbox" value = "13Y1A32"></p>
							<p align="right">33 TAN EE HENG<input type = "checkbox" value = "13Y1A33"></p>
							<p align="right">34 TAN KAIHENG<input type = "checkbox" value = "13Y1A34"></p>
							<p align="right">35 TAN ZIYANG HENRY<input type = "checkbox" value = "13Y1A35"></p>
							<p align="right">36 XAVIER TAN JUN HAN<input type = "checkbox" value = "13Y1A36"></p>
							<div><input type="submit" name="Submit" value="Submit" onclick="submit()" /></div>
							</form>
					</div>
				</div>
				<div id="leaveform">
					<div class="toolbar">
						<a href="#" class="back">Back</a>
						<h1><!-- Will be filled in --></h1>
					</div>
					<div class="info">''')
	self.response.out.write("""
              <form action="/leaveform" method="post" class="form">
				<p>I wish to apply leave from: <input type="date" name="leavefrom"> to <input type="date" name="leaveto">. 
				(<input type="number" name="numdays"> of days.)</p>
				<p>Reason For Application:</p>
				<textarea rows ="4" cols = "50" name = "reason">Enter reason here</textarea>
				<p>Name of Parent/Guardian: <input type = "text" name ="parentname"></p>
				<p>Contact: <input type = "number" name="homenum">(Home)</p>
				<p>Contact: <input type = "number" name = "officenum">(Office)</p>
				<p>Contact: <input type = "number" name = "handphone">(Handphone)</p>
				<p>Test(s) missed during leave</p>
				<textarea rows ="4" cols = "50" name = "testsmissed">Enter in format Subject:Date</textarea>
				<p>I hereby confirm that all of the above is truthful and accept the consequences were I to falsify or manipulate any information in any way<input type="checkbox" name="confirm" value="yay"></p>
                <div><input type="submit" name="Submit" value="Submit" onclick="submit()" /></div>
              </form>
            </body>
          </html>""")
	self.response.out.write('''
					</div>
				</div>
				<div id="mc">
					<div class="toolbar">
						<a href="#" class="back">Back</a>
						<h1><!-- Will be filled in --></h1>
					</div>
					<div class="info">
						 ''')
	self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data" class="form">' % upload_url)
	self.response.out.write("""Please upload a copy of your MC in any format!<br/>
								Note that falsified entries will be dealt with with discplinary action<br/>
								<input type="file" name="file">
	
	<input type="submit" name="Submit" value="Submit" onclick="submit()" /></form>
			</div>
				</div>
			</div>
		</body>
	</html>""")
class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
  def post(self):
    upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
    blob_info = upload_files[0]
    self.redirect('/serve/%s' % blob_info.key())

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self, resource):
    resource = str(urllib.unquote(resource))
    blob_info = blobstore.BlobInfo.get(resource)
    self.send_blob(blob_info)


app = webapp2.WSGIApplication([('/', MainPage), 
							   ('/upload', UploadHandler),
                               ('/serve/([^/]+)?', ServeHandler)],
                              debug=True)