from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    password = Column(String)
    confirm_password = Column(String)

    farms = relationship('Farm', back_populates='user')

class Farm(Base):
    __tablename__ = 'farms'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    crop_type = Column(String)
    crop_size = Column(Integer)

    user = relationship('User', back_populates='farms')

class Console:
    def __init__(self):
        self.engine = create_engine('sqlite:///users.db')  # Replace 'users.db' with your desired database URL
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_tables(self):
        pass  # No longer needed, as tables are created using SQLAlchemy declarative_base

    def add_farm(self, user_id, crop_type, crop_size):
        new_farm = Farm(user_id=user_id, crop_type=crop_type, crop_size=crop_size)
        self.session.add(new_farm)
        self.session.commit()
        return True

    def create_user(self, name, phone_number, email, password, confirm_password):
        new_user = User(
            name=name,
            phone_number=phone_number,
            email=email,
            password=password,
            confirm_password=confirm_password
        )
        self.session.add(new_user)
        self.session.commit()
        return new_user.id

    def get_user(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        if user:
            farms = self.session.query(Farm).filter_by(user_id=user_id).all()
            user_data = {
                'id': user.id,
                'name': user.name,
                'phone_number': user.phone_number,
                'email': user.email,
                'password': user.password,
                'confirm_password': user.confirm_password,
                'farms': [{'crop_type': farm.crop_type, 'crop_size': farm.crop_size} for farm in farms]
            }
            return user_data
        else:
            return None

    def get_all_users(self):
        users = self.session.query(User).all()
        users_data = []

        for user in users:
            farms = self.session.query(Farm).filter_by(user_id=user.id).all()
            user_data = {
                'id': user.id,
                'name': user.name,
                'phone_number': user.phone_number,
                'email': user.email,
                'password': user.password,
                'confirm_password': user.confirm_password,
                'farms': [{'crop_type': farm.crop_type, 'crop_size': farm.crop_size} for farm in farms]
            }
            users_data.append(user_data)

        return users_data

    def close_connection(self):
        self.session.close()

# Example usage:
if __name__ == '__main__':
    console = Console()
    user_id = console.create_user('Jimmy Macharia', '1234567890', 'jimmy@example.com', 'password123', 'password123')
    console.add_farm(user_id, 'Wheat', 10)
    console.add_farm(user_id, 'Corn', 8)

    user = console.get_user(user_id)
    print("User Data:")
    print(user)

    all_users = console.get_all_users()
    print("\nAll Users:")
    print(all_users)

    console.close_connection()
