from flask import render_template, url_for
from app.customer import bp


@bp.route('/user/<id>', methods=['GET','POST'])
def usercenter(id):
    return render_template("usercenter.html", title='User Account')