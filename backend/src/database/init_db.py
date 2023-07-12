from database.database import SessionLocal
from database.models.user import User






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