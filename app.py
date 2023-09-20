#!/usr/bin/python3
# app.py

from codecs import strict_errors
from email.policy import strict
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt
from flask import jsonify
import requests
import uuid
import datetime

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.config["IMAGE_FOLDER"] = "static/images/"
    # Initialize CSRF protection
    # CSRFProtect(app)

    # Import models and forms here to avoid circular imports
    from models.product import Product
    from models.user import User
    from models.blog import Blog
    from models.farm import Farm
    from models.crop import Crop
    
    
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)
   
    @app.route('/shop', strict_slashes=True)
    @login_required
    def shop():
        """function that renders the shop template"""
        cache_id = str(uuid.uuid4())
        products = Product.query.all()
        return render_template('shop.html', products=products, cache_id=cache_id)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    @app.route('/dashboard', strict_slashes=True)
    @login_required
    def dashboard():
        """function that renders the branch template"""
        api_key = '57455f848e83c8c7e2e33f2142a43391'
        city = "Kiambu"

        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        response = requests.get(url)

        # print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            # print(data)
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            temp_rnd = round(temp - 273.15)
            # print('[+] Temperature:{} C'.format(round(temp - 273.15)))
            # print('[+] Description:{}'.format(desc))
        else:
            print('Error fetching weather data')
   

        blogs = Blog.query.all()
        users = User.query.all()
        username = current_user.first_name
        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("dashboard.html", desc=desc, blogs=blogs, username=username, users=users, city=city, temp_rnd=temp_rnd, cache_id=cache_id)


    @app.route('/login', methods=["GET","POST"], strict_slashes=True)
    def login():
        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()

            if user and user.check_password(password):
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Login failed. Please check your email and password.', 'danger')

        return render_template('login.html', cache_id = cache_id)
    
    # Logout route
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('You have been logged out.', 'info')
        return redirect(url_for('login'))


    @app.route('/delete_product/<int:id>', methods=['GET', 'POST'])
    @login_required
    def delete_product(id):
        # Remove the product by ID (replace with your actual data source)
        if request.method == 'POST':
            product = Product.query.get_or_404(id)
            db.session.delete(product)
            db.session.commit()

            # Redirect back to the product list after deleting
            return redirect('/products')
        else:
            return redirect('/products')
        

    @app.route('/account', strict_slashes=True)
    @login_required
    def account():
        """function that renders the branch template"""

        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("account.html", cache_id=cache_id)
    
    @app.route('/manage', strict_slashes=True)
    @login_required
    def manage():
        products = Product.query.all()
        farms = Farm.query.all()
        return render_template("manage.html", products = products, farms = farms) 
        
    @app.route('/profile', strict_slashes=True)
    @login_required
    def profile():
        """function that renders the branch template"""
        username = current_user.first_name
        blogs = Blog.query.all()
        users = User.query.all()
        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("profile.html",
                               username = username,
                               users = users,
                               blogs=blogs,
                               cache_id=cache_id)
    

    @app.route('/profile/projects', strict_slashes=True)
    @login_required
    def projects():
        """function that renders the branch template"""

        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("projects.html", cache_id=cache_id)
    
    
    @app.route('/profile/notifications', strict_slashes=True)
    @login_required
    def notifications():
        """function that renders the branch template"""

        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("notifications.html", cache_id=cache_id)
    

    @app.route('/shop', strict_slashes=True)
    @login_required
    def edit_product():
        """function that renders the branch template"""

        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        products = Product.query.all()
        return render_template("shop.html", products=products, cache_id=cache_id)

    @app.route('/add_farm', strict_slashes=True, methods=('GET', 'POST'))
    @login_required
    def add_farm():
        """
        """

        """ fuction to add products to the db"""
        if request.method == 'POST':
            
            name = request.form['name']
            location = request.form['location']
            size_acres = request.form['size_acres']
            owner_id = current_user.id
        
            """Error handling"""
            if not name or not location or not size_acres:
                error_statement = "All fields required..."
                print("inside the if not")
                return render_template("add_farm.html",
                                    error_statement=error_statement,
                                    name=name,
                                    location = location,
                                    size_acres = size_acres,
                                    cache_id = cache_id)
                print(error_statement)
            else:
                print("I am in the saving stage")
                success_statement = "product added Successfuly"
                farm = Farm(
                    name=name,
                    location = location,
                    owner_id=owner_id,
                    size_acres = size_acres)
                db.session.add(farm)
                db.session.commit()

            # return render_template("/add_product", success_statement=success_statement, error_statement=error_statement)
        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("add_farm.html", cache_id=cache_id)

    @app.route('/add_product', strict_slashes=True, methods=('GET', 'POST'))
    @login_required
    def add_product():
        """function that renders the dashboard and also most of the admin part
            name (str) : name of the product
            file (str) : file name of the product image
            category (str) : category of the the product
            m_category (str) : minor category of the prodduct
            short_description (str) : a short description of the product
            long_description (str) : a long description of the product
            price (int) : price of the product
        """

        """ fuction to add products to the db"""
        if request.method == 'POST':
            
            f = request.files['image_url']
            filename = secure_filename(f.filename)
            f.save(app.config['IMAGE_FOLDER'] + filename)

            name = request.form['name']
            category = request.form['category']
            m_category = request.form['m_category']
            short_description = request.form['short_description']
            long_description = request.form['long_description']
            image_url = filename
            # price = request.form['price']
            owner_id = current_user.id
            now = datetime.datetime.now()

            """Error handling"""
            if not name or not category or not m_category or not short_description or not image_url:
                error_statement = "All fields required..."
                print("inside the if not")
                return render_template("add_product.html",
                                    error_statement=error_statement,
                                    name=name,
                                    category = category,
                                    m_category = category,
                                    short_description = short_description,
                                    image_url = image_url,
                                    cache_id=cache_id)
                print(error_statement)
            else:
                print("I am in the saving stage")
                success_statement = "product added Successfuly"
                product = Product(
                    name = name,
                    category = category,
                    m_category = m_category,
                    long_description = long_description,
                    short_description = short_description,
                    image_url = image_url,
                    created_at = now,
                    owner_id = owner_id)
                db.session.add(product)
                db.session.commit()
                print("is it you file?", image_url)

            # return render_template("/add_product", success_statement=success_statement, error_statement=error_statement)
        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("add_product.html", cache_id=cache_id)

    @app.route('/post_blog', strict_slashes=True, methods=('GET', 'POST'))
    @login_required
    def post_blog():
        """function that renders the dashboard and also most of the admin part
            Title (str) : title of the blog
            file (str) : file name of the blog image
            body (str) : Blog body
        """

        """ fuction to add a blog to the db"""
        if request.method == 'POST':
            
            f = request.files['image_url']
            filename = secure_filename(f.filename)
            f.save(app.config['IMAGE_FOLDER'] + filename)
            name = request.form['name']
            title = request.form['title']
            body = request.form['body']
            author_id = current_user.id
            image_url = filename
            now = datetime.datetime.now()

            """Error handling"""
            if not title or not body or not image_url:
                error_statement = "All fields required..."
                return render_template("post_blog.html",
                                    error_statement=error_statement,
                                    name = name,
                                    title=title,
                                    body = body,
                                    
                                    image_url = image_url,
                                    cache_id=cache_id)
                print(error_statement)
            else:
                success_statement = "blog added Successfuly"
                blog = Blog(
                    title = title,
                    name = name,
                    body = body,
                    author_id = author_id,
                    image_url = image_url,
                    created_at = now,)
                db.session.add(blog)
                db.session.commit()
                print("is it you file?", image_url)

            # return render_template("/add_product", success_statement=success_statement, error_statement=error_statement)
        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("post_blog.html", cache_id=cache_id)

    return app  # Return the app instance here

if __name__ == '__main__':
    app = create_app()
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)

