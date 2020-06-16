import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html", author = "Rok")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    exercises = [{"title": "Boogle", "author": "Rok", "url": "/portfolio/boogle"},
                 {"title": "Fakebook", "author": "Rok", "url": "/portfolio/fakebook"},
                 {"title": "Hair Salon", "author": "Rok", "url": "/portfolio/hair-salon"}]
    return render_template("portfolio.html", exercises = exercises)


@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")


@app.route("/portfolio/boogle")
def boogle():
    return render_template("boogle.html")


@app.route("/portfolio/hair-salon")
def hair_salon():
    return render_template("hair-salon.html")


if __name__ == '__main__':
    app.run()
