import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




load_dotenv()
DB_PORT = os.getenv("DB_PORT")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db(db):
    if db.query(User).count() == 0:
        user1 = {
            "name": "Mariana",
            "email": "mar@test.com",
            "phone_number": "988266356",
            "subscribed": ["Sports", "Movies", "Finance"],
            "channels": ["email", "sms", "push_notification"]
        }
        user2 = {
            "name": "David",
            "email": "david@test.com",
            "phone_number": "988266356",
            "subscribed": ["Finance", "Movies"],
            "channels": ["sms", "push_notification" ]
        }
        user3 = {
            "name": "Alex",
            "email": "alex@test.com",
            "phone_number": "988266356",
            "subscribed": ["Sports", "Movies"],
            "channels": ["email", "sms"]
        }
        users = [
            User(**user1),
            User(**user2),
            User(**user3)
        ]
        for user in users:
            db.add(user)

        db.commit()


def init():
    db = SessionLocal()
    init_db(db)


def celery_connection():
    return SessionLocal()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()