import json

class UserModel:
    # ... (other methods and attributes)

    def to_dict(self):
        farms_data = [farm.to_dict() for farm in self.farms]
        user_data = {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'farms': farms_data
        }
        return user_data

    def save_to_json(self, filename):
        user_data = self.to_dict()
        with open(filename, 'w') as file:
            json.dump(user_data, file)

    # ... (other methods)
