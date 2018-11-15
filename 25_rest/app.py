#Vincent Chi
#SoftDev1 pd08
#K25- Getting More REST
#2018-11-14

import urllib.request
import json

from flask import Flask, render_template

app = Flask(__name__)

url = "https://rickandmortyapi.com/api/character/1"

@app.route("/")
def resting():
	request = urllib.request.urlopen(url)
	content = request.read()
	print(content)
	
	jstuff = json.loads(content)
	print(jstuff)
	
	return render_template("index.html", pic = jstuff['image'], character = jstuff['name'])
	
if __name__ == "__main__":
    app.debug = True
    app.run()