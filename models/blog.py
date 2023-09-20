from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from app import db
# models
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)  # You can make this field nullable if needed
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Define a relationship to User for the blog's author
    author = db.relationship('User', backref=db.backref('blogs', lazy=True))

    def __init__(self, name, title, body, image_url, author_id, created_at):
        self.name = name
        self.title = title
        self.body = body
        self.image_url = image_url
        self.author_id = author_id
        self.created_at = self.created_at
