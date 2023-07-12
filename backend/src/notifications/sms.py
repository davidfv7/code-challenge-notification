from notifications.notification_factory import NotificationFactory
from database.models.notification import Notification
import datetime


class SmsFactory(NotificationFactory):
    def __init__(self, db):
        self.type = "sms"
        self.db = db

    def send_notification(self, payload):
        data = {
            "user_id": payload["user"].id,
            "message_id": payload["message"].id,
            "type": self.type,
            "send_at": datetime.datetime.utcnow()
        }
        record = Notification(**data)
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)