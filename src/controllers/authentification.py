from flask import abort, request, jsonify
from src.models.user import User
from src import bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    return 'Wrong email or password', 401

@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200