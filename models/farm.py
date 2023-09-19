from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from app import db
# models
class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    size_acres = db.Column(db.Float)

    def __init__(self, name, location, size_acres):
        self.name = name
        self.location = location
        self.size_acres = size_acres