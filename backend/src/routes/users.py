from fastapi import APIRouter, Depends, status
from database.database import get_db
from sqlalchemy.orm import Session
from database.models.user import User
from schemas.user import UserSchema


user_router = APIRouter()

@user_router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_message(payload: UserSchema, db: Session = Depends(get_db)):
    message = User(**payload.dict())
    db.add(message)
    db.commit()
    db.refresh(message)

    return {"success": True, "message": message}

