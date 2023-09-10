from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from app import db
# models
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(255), nullable=False)
    user = db.Column(db.String(255), nullable=False)
    title= db.Column(db.String(255), nullable=False)                                   
    body = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __init__(self, user, title, body, image_url, created_at):
        # self.name = name
        self.user = user
        self.title = title
        self.body = body
        self.image_url = image_url
        self.created_at = created_at