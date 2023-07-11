from fastapi import APIRouter, Depends, status
from database.database import get_db
from sqlalchemy.orm import Session
from database.models.notification import Notification
from schemas.notification import NotificationSchema


notification_router = APIRouter()

@notification_router.post("/notifications", status_code=status.HTTP_201_CREATED)
async def create_notification(payload: NotificationSchema, db: Session = Depends(get_db)):
    notification = Notification(**payload.dict())
    db.add(notification)
    db.commit()
    db.refresh(notification)

    return {"success": True, "notification": notification}

@notification_router.get("/notifications")
async def show_notifications(db: Session = Depends(get_db)):
    records = db.query(Notification).all()
    return records
