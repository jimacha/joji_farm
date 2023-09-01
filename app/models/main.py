from flask import Flask, request, jsonify
from models.user_model import UserModel

app = Flask(__name__)

# Create an instance of the UserModel class
user_model = UserModel()

# API routes for managing users
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = user_model.create_user(data)
    return jsonify({'message': 'User created successfully', 'user_id': user_id})

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_model.get_user(user_id)
    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/api/users', methods=['GET'])
def get_all_users():
    users = user_model.get_all_users()
    return jsonify({'users': users})

if __name__ == '__main__':
    app.run(debug=True)
