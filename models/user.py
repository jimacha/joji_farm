from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, username, email, password, created_at=None):
        self.username = username
        self.email = email
        self.set_password(password)  # Hash the password before saving it
        if created_at is not None:
            self.created_at = created_at

    def set_password(self, password):
        # Hash the password using Werkzeug's generate_password_hash function
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Check if the provided password matches the hashed password
        return check_password_hash(self.password_hash, password)

