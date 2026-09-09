from app.repositories.interfaces.user_repository import IUserRepository
from app.models.user import User
from typing import Optional

class UserService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def get_user_profile(self, uid: str) -> Optional[User]:
        """Retrieves the user profile using their Firebase UID."""
        return self.user_repo.get_user_by_firebase_uid(uid)

    def update_user_profile(self, uid: str, full_name: str) -> Optional[User]:
        """Updates user profile information."""
        user = self.user_repo.get_user_by_firebase_uid(uid)
        if not user:
            return None
        
        user.full_name = full_name
        self.user_repo.save_user(user)
        return user
