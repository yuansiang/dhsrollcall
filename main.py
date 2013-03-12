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
  
class MainPage(webapp2.RequestHandler):
  def get(self):
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
                    <h1>Attendance Taking</h1>
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
                <div class="info">
                    The title for this page was automatically set from it&#8217;s referring link, no extra scripts required. Just include the extension and this happens.
                </div>
            </div>
			<div id="mc">
                <div class="toolbar">
                    <a href="#" class="back">Back</a>
                    <h1><!-- Will be filled in --></h1>
                </div>
                <div class="info">
                     <form method="post" action="%=blobstoreService.createUploadUrl("/upload")%" enctype="multipart/form-data"> 
						 Description:<br> 
						 <input type="text" name="form_description" size="40"> 
						 <input type="hidden" name="MAX_FILE_SIZE" value="1000000"> 
						 <br>File to upload:<br> 
						 <input type="file" name="form_data" size="40"> 
						 <p><input type="submit" name="submit" value="submit"> 
					 </form> 
                </div>
            </div>
        </div>
    </body>
</html>
	  ''')

class About(webapp2.RequestHandler):	  
	def get(self):
	  self.response.out.write('''
	  HGaha
	  ''')


app = webapp2.WSGIApplication([('/', MainPage), ('/about', About)],
                              debug=True)