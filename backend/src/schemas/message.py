from pydantic import BaseModel
from typing import Optional


class MessageSchema(BaseModel):
    id: Optional[int] = None
    message: str
    category: str
    created_at: Optional[str] = None

    class Config:
        from_attributes = True