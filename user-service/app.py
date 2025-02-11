from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the User Service"}), 200

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def register_user():
    user = request.json
    users.append(user)
    return jsonify({"message": "User registered", "user": user}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    for user in users:
        if user["id"] == user_id:
            user.update(request.json)
            return jsonify({"message": "User updated", "user": user}), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
