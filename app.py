from flask import Flask, request, jsonify
import bcrypt
import jwt
import datetime
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({"message": "User already exists"}), 409

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed_pw

    return jsonify({"message": "registerd"}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    hashed_pw = users.get(username)
    if not hashed_pw or not bcrypt.checkpw(password.encode(), hashed_pw):
        return jsonify({"message": "Invalid try again"}), 401

    token = jwt.encode({
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({"token": token})


@app.route('/profile', methods=['GET'])
def profile():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"message": "Missing token"}), 401

    try:
        token = auth_header.split()[1]
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return jsonify({"message": f"Welcome, {data['username']}!"})
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401

if __name__ == '__main__':
    app.run(debug=True)
