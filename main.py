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
import urllib

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write('<html><head>')
	self.reponse.out.write("""<link rel="stylesheet" href="assets/style.css"/>
		<script src="assets/script.js"></script>
		<script type="text/javascript">

			  var _gaq = _gaq || [];
			  _gaq.push(['_setAccount', 'UA-39127932-1']);
			  _gaq.push(['_trackPageview']);

			  (function() {
				var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
				ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
				var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
			  })();

		</script>
		</head>
		<body>
		<h1>ROLLCALL</h1>
		<h2>Dunman High School Attendance Taking App</h2>
			<p>I like taking attendance</p>
	</body>
	</html>""")
		

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
