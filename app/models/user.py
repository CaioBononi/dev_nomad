import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class User:
    user_id: int 
    email: str
    hashed_password: Optional[str] = field(default=None, repr=False)
    firebase_uid: Optional[str] = field(default=None)
    full_name: str = field(default="")
    role: str = field(default="user")
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    is_active: bool = True 
    is_deleted: bool = False

    def deactive_user(self) -> None:
        if not self.is_active:
            raise ValueError("User is already inactive")
        self.is_active=False
        self.is_deleted=True
        self.updated_at = datetime.utcnow()