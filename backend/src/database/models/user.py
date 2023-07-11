from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    subscribed = Column(JSONB)
    channels = Column(JSONB)