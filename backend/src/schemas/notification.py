from pydantic import BaseModel
from typing import Optional


class NotificationSchema(BaseModel):
    id: Optional[int] = None
    user_id: int
    message: str
    category: str
    status: str = "QUEUED"
    created_at: Optional[str] = None
    send_at: Optional[str] = None

    class Config:
        from_attributes = True