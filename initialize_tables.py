from app import db, create_app
from models.product import Product
from models.user import User
from models.crop import Crop
from models.farm import Farm
from models.blog import Blog

app = create_app()
with app.app_context():
    db.create_all()
