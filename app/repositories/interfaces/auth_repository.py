from abc import ABC, abstractmethod
from typing import Optional

class IAuthRepository(ABC):
    @abstractmethod
    def verify_token(self, token: str) -> Optional[dict]:
        """Verifies a JWT token and returns the decoded payload."""
        pass
        
    @abstractmethod
    def create_user(self, email: str, password: str, display_name: str = None) -> str:
        """Creates a new user in the authentication provider and returns the provider UID."""
        pass
