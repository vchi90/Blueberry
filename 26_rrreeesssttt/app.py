#Vincent Chi
#SoftDev1 pd08
#K25- Getting More REST
#2018-11-15

import json
import urllib.request

from flask import Flask, render_template, request, session, url_for, redirect

key = "ppNyczCQivXxJ6yQddYXBHlX7DnuSStCN9fP1dyU"
url = "https://api.usa.gov/crime/fbi/sapi/api/agencies?api_key="

url2 = "https://opentdb.com/api.php?amount=10"

url3 = "https://aws.random.cat/meow"

peerURL1 = url + key

app = Flask(__name__)

@app.route("/")
def resting():
	request = urllib.request.urlopen(peerURL1)
	content = request.read()
	#print(content)
	
	jstuff = json.loads(content)
	#print(jstuff)
	
	request2 = urllib.request.urlopen(url2)
	content2 = request2.read()
	#print(content2)
	
	jstuff2 = json.loads(content2)
	#print(jstuff2)
	
	request3 = urllib.request.urlopen(url3)
	content3 = request3.read()
	#print(content3)
	
	jstuff3 = json.loads(content3)
	#print(jstuff3)
	
	return render_template("index.html", agency = jstuff['HI']['HI0010000']['agency_name'], type = jstuff['HI']['HI0010000']['agency_type_name'], triviaQ = jstuff2['results'][0]['question'], triviaA = jstuff2['results'][0]['correct_answer'], randomCat = jstuff3['file'])


if __name__ == "__main__":
    app.debug = True
    app.run()