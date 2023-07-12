from celery import Celery
from celery.schedules import crontab
from database.database import celery_connection
from database.models.message import Message
from database.models.user import User
import os
from notifications.notification_handler import NotificationHandler

app = Celery()
app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379")
app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379")


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(6.0, sendNotifications.s(), name='poll every 6s')

db = celery_connection()
@app.task
def sendNotifications():
    messages = db.query(Message).filter_by(status="QUEUED").all()
    for message in messages:
        NotificationHandler(message, db).sendNotifications()
        message.status = "SENT"
    
    db.commit()
