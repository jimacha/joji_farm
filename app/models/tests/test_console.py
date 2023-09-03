import unittest
import console  # Import your console.py module

class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up a test environment before each test."""
        # You can create a temporary database for testing if needed
        # Initialize your database connection here

    def tearDown(self):
        """Clean up the test environment after each test."""
        # Close the database connection or remove the temporary database
        pass

    def test_add_user(self):
        """Test adding user data to the database."""
        user_data = {
            "name": "Jimmy Macharia",
            "phone": "123-456-7890",
            "email": "macharia.com",
            "num_farms": 2,
            "farm_locations": ["Farm A", "Farm B"]
        }
        result = console.add_user(user_data)
        self.assertTrue(result)

    def test_update_user(self):
        """Test updating user data in the database."""
        user_id = 1  # Replace with a valid user ID from your database
        updated_data = {
            "name": "Updated Name",
            "phone": "987-654-3210",
            "email": "updated@example.com",
            "num_farms": 3,
            "farm_locations": ["Farm X", "Farm Y", "Farm Z"]
        }
        result = console.update_user(user_id, updated_data)
        self.assertTrue(result)

    def test_get_user(self):
        """Test retrieving user data from the database."""
        user_id = 1  # Replace with a valid user ID from your database
        user = console.get_user(user_id)
        self.assertIsNotNone(user)

    def test_get_all_users(self):
        """Test retrieving all user data from the database."""
        users = console.get_all_users()
        self.assertTrue(len(users) > 0)

if __name__ == '__main__':
    unittest.main()
