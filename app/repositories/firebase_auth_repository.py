from app.repositories.interfaces.auth_repository import IAuthRepository
from firebase_admin import auth

class FirebaseAuthRepository(IAuthRepository):
    def verify_token(self, token: str) -> dict:
        try:
            return auth.verify_id_token(token)
        except Exception as e:
            raise ValueError(f"Invalid token: {e}")

    def create_user(self, email: str, password: str, display_name: str = None) -> str:
        try:
            user_record = auth.create_user(
                email=email,
                password=password,
                display_name=display_name
            )
            return user_record.uid
        except Exception as e:
            raise ValueError(f"Failed to create user: {e}")
