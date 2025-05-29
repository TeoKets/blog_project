import requests
from pprint import pprint
from flask import Flask,render_template,url_for,redirect


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

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__=="__main__":
    app.run(debug=True)


