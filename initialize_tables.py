from app import db, create_app
from models.product import Product
from models.user import User
app = create_app()
with app.app_context():
    db.create_all()
