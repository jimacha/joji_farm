from app import db, create_app
from models.user import User

user1 = User(
            first_name='Jimmy',
            last_name='Mungai',
            email='machariajimmy68@gmail.com',
            password='101'
        )


app = create_app()
with app.app_context():
    db.session.add(user1)
   
    db.session.commit()