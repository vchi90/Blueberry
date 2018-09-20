#Vincent Chi
#SoftDev1 pd8
#K08 Fill Yer Flask
#2018-09-19

<yyyy>-<mm>-<dd>

from flask import Flask
app = Flask(__name__) #instantiates the Flask class using a constructor

@app.route('/')
def home():
    return 'Atom is the best religion'
 
@app.route('/something')
def derpy():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
 
app.debug = True
app.run()
