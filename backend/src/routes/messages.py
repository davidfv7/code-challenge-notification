from fastapi import APIRouter, Depends, status
from database.database import get_db
from sqlalchemy.orm import Session
from database.models.message import Message
from schemas.message import MessageSchema


message_router = APIRouter()

@message_router.post("/messages", status_code=status.HTTP_201_CREATED)
async def create_message(payload: MessageSchema, db: Session = Depends(get_db)):
    message = Message(**payload.dict())
    db.add(message)
    db.commit()
    db.refresh(message)

    return {"success": True, "message": message}

@message_router.get("/messages")
async def show_messages(db: Session = Depends(get_db)):
    records = db.query(Message).all()
    return records
