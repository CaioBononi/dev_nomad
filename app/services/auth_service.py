from app.repositories.interfaces.auth_repository import IAuthRepository
from app.repositories.interfaces.user_repository import IUserRepository
from app.models.user import User

class AuthService:
    def __init__(self, auth_repo: IAuthRepository, user_repo: IUserRepository):
        self.auth_repo = auth_repo
        self.user_repo = user_repo

    def verify_token(self, token: str) -> dict:
        """Verifies the JWT token from Firebase."""
        return self.auth_repo.verify_token(token)

    def register_user(self, email: str, password: str, full_name: str) -> User:
        """Registers a user in Firebase Auth and saves them in Firestore."""
        # Create user in Firebase Auth
        uid = self.auth_repo.create_user(email=email, password=password, display_name=full_name)
        
        # Create user entity
        user = User(
            user_id=0, # Placeholder
            email=email,
            full_name=full_name,
            firebase_uid=uid
        )
        
        # Save to Firestore
        self.user_repo.save_user(user)
        
        return user
