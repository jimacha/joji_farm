from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import farm, user
from sqlalchemy.sql import func

from app import db
# models
class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    planting_date = db.Column(db.DateTime(timezone=True))
    harvesting_date = db.Column(db.DateTime(timezone=True))
    yield_quantity = db.Column(db.Float)
    farm_id = db.Column(db.Integer, db.ForeignKey('farm.id'))

    def __repr__(self):
        return f'<crop "{self.name}">'

    def __init__(self, name, planting_date, harvesting_date, yield_quantity, farm, user):
        self.name = name
        self.planting_date = planting_date
        self.harvesting_date = harvesting_date
        self.yield_quantity = yield_quantity
        self.farm = farm
        self.user = user
