from flask import render_template, url_for
from app.auth import bp

@bp.route('/login')
def login():
    return render_template('login.html')