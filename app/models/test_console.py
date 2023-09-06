
import unittest
from console import Console

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = Console()

    def tearDown(self):
        self.console.close_connection()

    def clear_database(self):
        #clears all data
        self.console.session.query(Console.User).delete()
        self.console.session.query(Console.Farm).delete()
        self.console.session.commit()

    def test_create_user_and_get_user(self):
        user_id = self.console.create_user('Jimmy Macharia', '1234567890', 'jimmy@example.com', 'password123', 'password123')
        user = self.console.get_user(user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user['name'], 'Jimmy Macharia')
        self.assertEqual(user['phone_number'], '1234567890')
        self.assertEqual(user['email'], 'jimmy@example.com')
        self.assertEqual(user['password'], 'password123')
        self.assertEqual(user['confirm_password'], 'password123')

    def test_add_farm(self):
        user_id = self.console.create_user('Jimmy Macharia', '9876543210', 'jimmy@example.com', 'password456', 'password456')
        self.console.add_farm(user_id, 'Wheat', 10)
        self.console.add_farm(user_id, 'Corn', 8)

        user = self.console.get_user(user_id)
        self.assertIsNotNone(user)
        farms = user['farms']
        self.assertEqual(len(farms), 2)

        # Check the details of the first farm
        self.assertEqual(farms[0]['crop_type'], 'Wheat')
        self.assertEqual(farms[0]['crop_size'], 10)

        # Check the details of the second farm
        self.assertEqual(farms[1]['crop_type'], 'Corn')
        self.assertEqual(farms[1]['crop_size'], 8)

    def test_get_all_users(self):
        self.clear_database()


        user1_id = self.console.create_user('Alice Johnson', '1112223333', 'alice@example.com', 'pass123', 'pass123')
        user2_id = self.console.create_user('Bob Smith', '4445556666', 'bob@example.com', 'pass456', 'pass456')

        all_users = self.console.get_all_users()
        self.assertIsNotNone(all_users)
        self.assertEqual(len(all_users), 2)

        # Check the details of the first user
        user1 = all_users[0]
        self.assertEqual(user1['id'], user1_id)
        self.assertEqual(user1['name'], 'Alice Johnson')
        self.assertEqual(user1['phone_number'], '1112223333')
        self.assertEqual(user1['email'], 'alice@example.com')

        # Check the details of the second user
        user2 = all_users[1]
        self.assertEqual(user2['id'], user2_id)
        self.assertEqual(user2['name'], 'Bob Smith')
        self.assertEqual(user2['phone_number'], '4445556666')
        self.assertEqual(user2['email'], 'bob@example.com')

if __name__ == '__main__':
    unittest.main()
