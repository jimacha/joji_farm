class UserModel:
    def __init__(self):
        self.users = []

    def register_user(self, name, phone_number, email, password, confirm_password):
        if password != confirm_password:
            return {'message': 'Password and Confirm Password do not match'}, 400

        user = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'password': password,
            'farms': []  # A list to store farm information
        }

        self.users.append(user)
        return {'message': 'User registered successfully'}, 201

    def add_farms(self, user_id, num_farms):
        for user in self.users:
            if user['id'] == user_id:
                user['farms'] = []
                for i in range(num_farms):
                    farm_location = input(f"Enter location for Farm {i + 1}: ")
                    user['farms'].append({'location': farm_location})
                return {'message': f'Added {num_farms} farms successfully'}, 201
        return {'message': 'User not found'}, 404

    def get_user_farms(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return {'farms': user['farms']}
        return {'message': 'User not found'}, 404
