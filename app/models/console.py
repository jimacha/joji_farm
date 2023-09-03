import sqlite3

class Console:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.create_tables()

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

    def add_farm(self, user_id, crop_type, crop_size):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO farms (user_id, crop_type, crop_size) VALUES (?, ?, ?)', (user_id, crop_type, crop_size))
        self.conn.commit()
        return True

    def create_user(self, name, phone_number, email, password, confirm_password):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO users (name, phone_number, email, password, confirm_password)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, phone_number, email, password, confirm_password))
        self.conn.commit()
        return cursor.lastrowid

    def get_user(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            cursor.execute('SELECT crop_type, crop_size FROM farms WHERE user_id = ?', (user_id,))
            farms = cursor.fetchall()
            user_data = dict(user_data)
            user_data['farms'] = [{'crop_type': farm[0], 'crop_size': farm[1]} for farm in farms]

        return user_data

    def get_all_users(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users')
        users_data = cursor.fetchall()
        users = []

        for user_data in users_data:
            user_id = user_data[0]
            cursor.execute('SELECT crop_type, crop_size FROM farms WHERE user_id = ?', (user_id,))
            farms = cursor.fetchall()
            user_data = dict(user_data)
            user_data['farms'] = [{'crop_type': farm[0], 'crop_size': farm[1]} for farm in farms]
            users.append(user_data)

        return users

    def close_connection(self):
        self.conn.close()

# Example usage:
if __name__ == '__main__':
    console = Console()
    user_id = console.create_user('Jimmy Macharia', '1234567890', 'macharia.com', 'password123', 'password123')
    console.add_farm(user_id, 'Wheat', 10)
    console.add_farm(user_id, 'Corn', 8)

    user = console.get_user(user_id)
    print("User Data:")
    print(user)

    all_users = console.get_all_users()
    print("\nAll Users:")
    print(all_users)

    console.close_connection()
