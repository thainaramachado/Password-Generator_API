from flask import Blueprint, jsonify, request
import secrets
import string

password_routes = Blueprint('password_routes', __name__)

@password_routes.route('/password_generator', methods=['GET'])
def password_generator():
    length = int(request.args.get('length', 12))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return jsonify({"password": password})

