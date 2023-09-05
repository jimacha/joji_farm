import unittest
import sqlite3
from console import Console

class TestConsole(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database for testing
        self.conn = sqlite3.connect(':memory:')
        self.console = Console()
        self.console.create_tables()

    def tearDown(self):
        # Close the database connection
        self.conn.close()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone_number TEXT,
                email TEXT,
                password TEXT,
                confirm_password TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS farms (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                crop_type TEXT,
                crop_size INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        self.conn.commit()

    def test_create_user(self):
        user_id = self.console.create_user('Jimmy Macharia', '1234567890', 'jimmy@example.com', 'password123', 'password123')
        self.assertTrue(user_id > 0)

    def test_add_farm(self):
        user_id = self.console.create_user('Jimmy Macharia', '1234567890', 'jimmy@example.com', 'password123', 'password123')
        result = self.console.add_farm(user_id, 'Wheat', 10)
        self.assertTrue(result)

    def test_get_user(self):
        user_id = self.console.create_user('Jimmy Macharia', '1234567890', 'jimmy@example.com', 'password123', 'password123')
        self.console.add_farm(user_id, 'Wheat', 10)
        user_data = self.console.get_user(user_id)
        self.assertIsNotNone(user_data)
        self.assertEqual(user_data['name'], 'Jimmy Macharia')
        self.assertEqual(len(user_data['farms']), 1)

if __name__ == '__main__':
    unittest.main()
