#Vincent Chi
#SoftDev Pd8
#K13 -- Echo Echo Echo
#2018-09-30

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("toEcho.html")

@app.route("/auth", methods = ["GET", "POST"])
def authenticate():
    return render_template("theEcho.html", name = request.args['username'], method = request.method)        


if __name__ == "__main__":
    app.debug = True
    app.run()