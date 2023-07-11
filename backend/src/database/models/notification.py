from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from database.database import Base
from database.models.user import User
import datetime


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id))
    status = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    send_at = Column(DateTime, default=datetime.datetime.utcnow)
