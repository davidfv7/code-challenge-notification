from fastapi import FastAPI
from database.database import engine
from database.base import Base
from fastapi.middleware.cors import CORSMiddleware

from routes.notifications import notification_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notification_router)


Base.metadata.create_all(bind=engine)