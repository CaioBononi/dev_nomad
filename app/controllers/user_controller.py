from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.repositories.firestore_user_repository import FirestoreUserRepository
from app.repositories.firebase_auth_repository import FirebaseAuthRepository

user_blueprint = Blueprint('user', __name__)

user_repo = FirestoreUserRepository()
user_service = UserService(user_repo)
auth_service = AuthService(FirebaseAuthRepository(), user_repo)

def get_current_user_uid():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        return None
    token = auth_header.split("Bearer ")[1]
    try:
        decoded_token = auth_service.verify_token(token)
        return decoded_token.get('uid')
    except:
        return None

@user_blueprint.route('/profile', methods=['GET'])
def get_profile():
    uid = get_current_user_uid()
    if not uid:
        return jsonify({"error": "Unauthorized"}), 401

    user = user_service.get_user_profile(uid)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "email": user.email,
        "full_name": user.full_name,
        "role": user.role,
        "is_active": user.is_active
    }), 200

@user_blueprint.route('/profile', methods=['PUT'])
def update_profile():
    uid = get_current_user_uid()
    if not uid:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    full_name = data.get('full_name')

    if not full_name:
        return jsonify({"error": "Missing required fields"}), 400

    user = user_service.update_user_profile(uid, full_name)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "Profile updated successfully"}), 200
