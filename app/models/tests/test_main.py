import unittest
from main import app

class TestMain(unittest.TestCase):

    def setUp(self):
        # Create a test client for the Flask app
        self.client = app.test_client()

    def test_create_user(self):
        # Test the create_user API route
        data = {
            'name': 'Jimmy Macharia',
            'phone_number': '1234567890',
            'email': 'macharia.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }
        response = self.client.post('/api/users', json=data)
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        # Test the get_user API route
        response = self.client.get('/api/users/1')
        self.assertEqual(response.status_code, 404)

    def test_get_all_users(self):
        # Test the get_all_users API route
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
