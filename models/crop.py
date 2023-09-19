from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from app import db
# models
class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    planting_date = db.Column(db.DateTime(timezone=True))
    harvesting_date = db.Column(db.DateTime(timezone=True))
    yield_quantity = db.Column(db.Float)

    def __init__(self, name, planting_date, harvesting_date, yield_quantity):
        self.name = name
        self.planting_date = planting_date
        self.harvesting_date = harvesting_date
        self.yield_quantity = yield_quantity