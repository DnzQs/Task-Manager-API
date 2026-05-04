from fastapi import FastAPI, HTTPException
from app.db import Base, engine
from app.models import User
from app.routes import auth
from app.routes import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth")

app.include_router(task.router, prefix="/task", tags=["task"])




