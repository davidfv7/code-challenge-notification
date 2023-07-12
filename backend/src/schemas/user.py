from pydantic import BaseModel
from typing import Optional, Any


class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    phone_number: Optional[str] = None
    subscribed: Optional[Any] = None
    channels: Optional[Any] = None

    class Config:
        from_attributes = True