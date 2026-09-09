from app.repositories.interfaces.user_repository import IUserRepository
from app.models.user import User
from firebase_admin import firestore
import datetime

class FirestoreUserRepository(IUserRepository):
    def __init__(self):
        self.db = firestore.client()
        self.collection = self.db.collection('users')

    def get_user_by_firebase_uid(self, uid: str) -> User | None:
        doc_ref = self.collection.document(uid)
        doc = doc_ref.get()
        if not doc.exists:
            return None
        data = doc.to_dict()
        user = User(
            user_id=data.get('user_id', 0),
            email=data.get('email', ''),
            full_name=data.get('full_name', ''),
            role=data.get('role', 'user'),
            is_active=data.get('is_active', True),
            is_deleted=data.get('is_deleted', False),
            firebase_uid=uid
        )
        return user

    def save_user(self, user: User) -> None:
        if not user.firebase_uid:
            raise ValueError("User must have a firebase_uid to be saved in Firestore.")
        
        doc_ref = self.collection.document(user.firebase_uid)
        doc_ref.set({
            'user_id': user.user_id,
            'email': user.email,
            'full_name': user.full_name,
            'role': user.role,
            'is_active': user.is_active,
            'is_deleted': user.is_deleted,
            'created_at': user.created_at.isoformat() if isinstance(user.created_at, datetime.datetime) else user.created_at,
            'updated_at': user.updated_at.isoformat() if isinstance(user.updated_at, datetime.datetime) else user.updated_at,
            'id': str(user.id)
        }, merge=True)
