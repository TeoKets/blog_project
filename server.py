from email.feedparser import headerRE
from operator import itemgetter

import requests
from pprint import pprint
from flask import Flask,render_template,url_for,redirect,request


respond=requests.get("https://api.npoint.io/c8f2cc570fd551ae00f1")
respond.raise_for_status()
blogs=respond.json()


app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html",blogs=blogs)

@app.route("/about")
def about():
    return render_template("about.html")


#i dont get the info yet
@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method=="GET":
        return render_template("contact.html")
    else:

        data = request.form

        return render_template("contact.html",nav="success")





if __name__=="__main__":
    app.run(debug=True)


