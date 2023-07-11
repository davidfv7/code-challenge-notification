from fastapi import FastAPI
from database.database import engine, SessionLocal
from database.base import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}