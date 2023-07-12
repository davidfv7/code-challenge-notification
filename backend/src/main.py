from fastapi import FastAPI
from database.database import engine
from database.base import Base
from fastapi.middleware.cors import CORSMiddleware

from routes.notifications import notification_router
from routes.messages import message_router
from routes.users import user_router
from database.init_db import init

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
app.include_router(message_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)

init() 