from flask import render_template, url_for, redirect
from app.auth import bp
from app.auth.forms import LoginForm, SignupForm

@bp.route('/login', methods=['GET','POST'])
@bp.route('/', methods=['GET','POST'])
@bp.route('/index', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('customer.usercenter', id=200))
    return render_template('login.html', title='Login',form=form)