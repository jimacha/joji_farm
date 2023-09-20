from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from app import db
# models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    m_category = db.Column(db.String(255), nullable=False)
    short_description = db.Column(db.Text)
    long_description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    price = db.Column(db.Integer, nullable=False, default=0)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<product "{self.name}">'
    
    def __init__(self, name, short_description, long_description, image_url, price, created_at, category, m_category, owner_id):
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.image_url = image_url
        self.price = price
        self.created_at = created_at
        self.category = category
        self.m_category = m_category
        self.owner_id = owner_id
