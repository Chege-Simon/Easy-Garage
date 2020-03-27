from app import app
from flask import render_template,url_for

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home')

@app.route('/myvehicles')
def myVehicles():
    return render_template("myvehicles.html", title='My Vehicles')

@app.route('/user/<id>')
def usercenter(id):
    return render_template("usercenter.html", title='User Account')