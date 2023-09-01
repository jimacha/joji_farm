import json

class Console:
    def __init__(self):
        self.data = {}

    def add_farm(self, user_id, crop_type, crop_size):
        if user_id not in self.data:
            return False

        user_data = self.data[user_id]
        farms = user_data.get('farms', [])
        farm_data = {'crop_type': crop_type, 'crop_size': crop_size}
        farms.append(farm_data)
        user_data['farms'] = farms

        return True

    def create_user(self, name, phone_number, email, password, confirm_password):
        user_id = len(self.data) + 1
        user_data = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
            'farms': []
        }
        self.data[user_id] = user_data
        return user_id

    def get_user(self, user_id):
        return self.data.get(user_id, None)

    def get_all_users(self):
        return list(self.data.values())

# Example usage:
if __name__ == '__main__':
    console = Console()
    user_id = console.create_user('Jimmy Machari', '1234567890', 'macharia.com', 'password123', 'password123')
    console.add_farm(user_id, 'Wheat', 10)
    console.add_farm(user_id, 'Corn', 8)

    user = console.get_user(user_id)
    print("User Data:")
    print(json.dumps(user, indent=2))

    all_users = console.get_all_users()
    print("\nAll Users:")
    print(json.dumps(all_users, indent=2))
