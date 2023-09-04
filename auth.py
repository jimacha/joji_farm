from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")
@auth.route('/logout')
def logout():
    pass
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        f_name = request.form.get('f_name')
        password = request.form.get('password')
        conf_password = request.form.get('conf_password')

        if len(email) < 4:
            flash('email too short', category='error')
        elif len(f_name) < 2:
            flash('first name too short', category='error')
        elif password != conf_password:
            flash('the two passwords are not the same', category='error')
        else:
            flash('account created succesfully')
    return render_template("register.html")