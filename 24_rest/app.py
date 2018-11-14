#Vincent Chi
#SoftDev1 pd08
#K24- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)

url = "https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=ppNyczCQivXxJ6yQddYXBHlX7DnuSStCN9fP1dyU"
url2 = "https://api.nasa.gov/planetary/apod?api_key=ppNyczCQivXxJ6yQddYXBHlX7DnuSStCN9fP1dyU"

@app.route("/")
def resting():
	request = urllib.request.urlopen(url)
	content = request.read()
	print(content)
	
	request2 = urllib.request.urlopen(url2)
	content2 = request2.read()
	print(content2)
	
	jstuff = json.loads(content)
	print(jstuff)
	
	jstuff2 = json.loads(content2)
	print(jstuff2)
	
	return render_template("index.html", pic = jstuff['url'], explanation = jstuff2['explanation'])
	
if __name__ == "__main__":
    app.debug = True
    app.run()