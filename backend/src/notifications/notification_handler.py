
from notifications.email import EmailFactory
from notifications.push_notification import PushNotificationFactory
from notifications.sms import SmsFactory
from database.models.user import User
from database.models.message import Message


class NotificationHandler():
    FACTORIES = {
        "email": EmailFactory,
        "sms": SmsFactory,
        "push_notification": PushNotificationFactory
    }

    def __init__(self, message: Message, db):
        self.message = message
        self.db = db

    def sendNotifications(self):
        users = self.db.query(User).filter(User.subscribed.contains([self.message.category])).all()
        for user in users:
            if user.channels is not None:
                for channel in user.channels:
                    payload = {
                        "user": user,
                        "message": self.message,
                    }
                    self.FACTORIES[channel](self.db).send_notification(payload)