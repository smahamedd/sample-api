from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

users = []


@app.route('/users', methods=['POST'])
def create_user():

    data = request.get_json()
    name = data['name']
    email = data['email']
    phone_number = data['phone_number']
    added_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_id = len(users) + 1

    user = {'id': user_id, 'name': name, 'email': email,
            'phone_number': phone_number, 'added_date': added_date}
    users.append(user)

    return jsonify(user), 201


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)

    return jsonify({'error': 'User not found'}), 404


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone_number = data['phone_number']
    added_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for user in users:
        if user['id'] == user_id:
            user['name'] = name
            user['email'] = email
            user['phone_number'] = phone_number
            user['added_date'] = added_date

            return jsonify(user)

    return jsonify({'error': 'User not found'}), 404


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)

            return '', 204

    return jsonify({'error': 'User not found'}), 404


@app.route('/users', methods=['DELETE'])
def delete_all_users():
    global users
    users = []
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
