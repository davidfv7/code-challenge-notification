from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database.database import Base
from database.models.user import User
from database.models.message import Message
from sqlalchemy.orm import relationship


class Notification(Base):
    __tablename__ = "notifications_sent"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id))
    message_id = Column(Integer, ForeignKey(Message.id))
    type = Column(String)
    send_at = Column(DateTime, default=None)
    user = relationship('User', uselist=False, lazy='joined', backref="notifications_sent")
    message = relationship('Message', uselist=False, lazy='joined', backref="notifications_sent")
