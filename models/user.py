from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_bcrypt import Bcrypt

from app import db
bcrypt = Bcrypt()
# models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    # Required method: Check if the user is active
    def is_active(self):
        # For simplicity, assume all users are active
        return True

    # Required method: Check if the user is authenticated
    def is_authenticated(self):
        # In a real application, you can implement your authentication logic here
        # For example, return True if the user has provided valid credentials during login
        return True

    # Required method: Check if the user is anonymous (typically False for authenticated users)
    def is_anonymous(self):
        # For authenticated users, return False (not anonymous)
        return False

    # Required method: Get the user's unique identifier (usually the user ID)
    def get_id(self):
        # Return the user's ID as a string
        return str(self.id)
