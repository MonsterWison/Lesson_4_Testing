from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from flask_login import UserMixin

class User(SQLModel, UserMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    password_hash: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
    preferred_language: str = Field(default='en')
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = None
    last_modified: Optional[datetime] = None
    last_modified_by: Optional[str] = None 