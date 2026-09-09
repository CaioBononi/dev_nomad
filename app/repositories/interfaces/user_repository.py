from abc import ABC, abstractmethod
from typing import Optional
from app.models.user import User

class IUserRepository(ABC):
    @abstractmethod
    def get_user_by_firebase_uid(self, uid: str) -> Optional[User]:
        pass

    @abstractmethod
    def save_user(self, user: User) -> None:
        pass
