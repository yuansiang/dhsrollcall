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

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import db
from google.appengine.api import users


class Persons(db.expando):
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
						The title for this page was automatically set from it&#8217;s referring link, no extra scripts required. Just include the extension and this happens.
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