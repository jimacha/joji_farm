import unittest
from models.user_model import UserModel

class TestUserModel(unittest.TestCase):

    def setUp(self):
        # Initialize the UserModel instance
        self.user_model = UserModel()

    def test_create_user(self):
        # Test the create_user method
        data = {
            'name': 'Jimmy Macharia',
            'phone_number': '1234567890',
            'email': 'macharia.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }
        user_id = self.user_model.create_user(data)
        self.assertIsInstance(user_id, int)

    def test_get_user(self):
        # Test the get_user method
        user = self.user_model.get_user(1)
        self.assertIsNone(user)

    def test_get_all_users(self):
        # Test the get_all_users method
        users = self.user_model.get_all_users()
        self.assertIsInstance(users, list)

if __name__ == '__main__':
    unittest.main()
