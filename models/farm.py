from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from app import db
# models
class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    size_acres = db.Column(db.String(255), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # Define a relationship to User for the farm's owner
    owner = db.relationship('User', backref=db.backref('farms', lazy=True))

    def __init__(self, name, location, owner_id, size_acres, created_at=None):
        self.name = name
        self.location = location
        self.owner_id = owner_id
        self.size_acres = size_acres
        if created_at is not None:
            self.created_at = created_at