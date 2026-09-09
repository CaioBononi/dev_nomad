from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService
from app.repositories.firebase_auth_repository import FirebaseAuthRepository
from app.repositories.firestore_user_repository import FirestoreUserRepository

auth_blueprint = Blueprint('auth', __name__)

# Basic Dependency Injection
auth_repo = FirebaseAuthRepository()
user_repo = FirestoreUserRepository()
auth_service = AuthService(auth_repo, user_repo)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    full_name = data.get('full_name')

    if not all([email, password, full_name]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        user = auth_service.register_user(email, password, full_name)
        return jsonify({"message": "User registered successfully", "uid": user.firebase_uid}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@auth_blueprint.route('/verify', methods=['POST'])
def verify():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing or invalid Authorization header"}), 401

    token = auth_header.split("Bearer ")[1]
    
    try:
        decoded_token = auth_service.verify_token(token)
        return jsonify({"message": "Token is valid", "uid": decoded_token.get('uid')}), 200
    except Exception as e:
        return jsonify({"error": "Invalid token"}), 401
