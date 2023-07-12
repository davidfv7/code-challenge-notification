from fastapi import APIRouter, Depends, status
from database.database import get_db
from database.base import Base
from sqlalchemy.orm import Session
from database.models.notification import Notification
from schemas.notification import NotificationSchema


notification_router = APIRouter()


@notification_router.get("/notifications")
async def show_notifications(page: int = 1, size: int = 5, db: Session = Depends(get_db)):
    '''Returns notifications and paginates depending on the page and size sent on the url'''
    records = db.query(Notification).offset((page - 1) * size).limit(size).all()
    return { "records": records, "total": db.query(Notification).count()}
