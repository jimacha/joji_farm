#!/usr/bin/python3
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
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
    from models.blog import Blog
    # from forms import ProductForm
    
   
    @app.route('/shop', strict_slashes=True)
    def shop():
        """function that renders the shop template"""
        cache_id = str(uuid.uuid4())
        products = Product.query.all()
        return render_template('shop.html', products=products, cache_id=cache_id)

    @app.route('/')
    @app.route('/dashboard', strict_slashes=True)
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
   
        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("dashboard.html", desc=desc, city=city, temp_rnd=temp_rnd, cache_id=cache_id)


    @app.route('/login', methods=["POST"], strict_slashes=True)
    def login():
        """function that renders the branch template"""

        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("login.html", cache_id=cache_id)

    @app.route('/account', strict_slashes=True)
    def account():
        """function that renders the branch template"""

        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("account.html", cache_id=cache_id)
        
    @app.route('/profile', strict_slashes=True)
    def profile():
        """function that renders the branch template"""

        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("profile.html", cache_id=cache_id)
    
    @app.route('/profile/projects', strict_slashes=True)
    def projects():
        """function that renders the branch template"""

        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("projects.html", cache_id=cache_id)
    


    @app.route('/shop', strict_slashes=True)
    def edit_product():
        """function that renders the branch template"""

        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        products = Product.query.all()
        return render_template("shop.html", products=products, cache_id=cache_id)


    @app.route('/add_product', strict_slashes=True, methods=('GET', 'POST'))
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
            price = request.form['price']
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
                    price = price)
                db.session.add(product)
                db.session.commit()
                print("is it you file?", image_url)

            # return render_template("/add_product", success_statement=success_statement, error_statement=error_statement)
        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        return render_template("add_product.html", cache_id=cache_id)

    @app.route('/post_blog', strict_slashes=True, methods=('GET', 'POST'))
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

            title = request.form['title']
            body = request.form['blog']
            user = 'Admin'
            image_url = filename
            price = request.form['price']
            now = datetime.datetime.now()

            """Error handling"""
            if not title or not body or not image_url:
                error_statement = "All fields required..."
                return render_template("post_blog.html",
                                    error_statement=error_statement,
                                    title=title,
                                    body = body,
                                    image_url = image_url,
                                    cache_id=cache_id)
                print(error_statement)
            else:
                success_statement = "blog added Successfuly"
                product = Product(
                    title = title,
                    body = body,
                    user = user,
                    image_url = image_url,
                    created_at = now,
                    price = price)
                db.session.add(product)
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

