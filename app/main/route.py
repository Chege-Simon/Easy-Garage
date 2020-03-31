
from flask import render_template,url_for
from app.main import bp

@bp.route('/myvehicles', methods=['GET','POST'])
def myVehicles():
    return render_template("myvehicles.html", title='My Vehicles')
