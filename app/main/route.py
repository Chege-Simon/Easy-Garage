
from flask import render_template,url_for, Blueprint
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    return render_template("index.html", title='Home')

@bp.route('/myvehicles')
def myVehicles():
    return render_template("myvehicles.html", title='My Vehicles')

@bp.route('/user/<id>')
def usercenter(id):
    return render_template("usercenter.html", title='User Account')