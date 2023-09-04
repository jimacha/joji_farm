import sqlite3
import os

class Console:
    def __init__(self):
        db_file = 'users.db'
        new_db = not os.path.isfile(db_file)

        self.conn = sqlite3.connect(db_file)

        if new_db:
            self.create_tables()

    # ... (rest of your Console class methods)

    def create_tables(self):
        # Your table creation code here

    # ... (rest of your Console class methods)

    def close_connection(self):
        self.conn.close()

if __name__ == '__main__':
    console = Console()
    user_id = console.create_user('John Doe', '1234567890', 'john@example.com', 'password123', 'password123')
    console.add_farm(user_id, 'Wheat', 10)
    console.add_farm(user_id, 'Corn', 8)

    user = console.get_user(user_id)
    print("User Data:")
    print(user)

    all_users = console.get_all_users()
    print("\nAll Users:")
    print(all_users)

    console.close_connection()

