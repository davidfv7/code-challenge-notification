from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from database.database import Base
from database.models.user import User
import datetime


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    category = Column(String)
    status = Column(String, default="QUEUED")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
