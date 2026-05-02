from fastapi import FastAPI, HTTPException
from app_API.db import Base, engine
from app_API.models import User
from app_API.routes import auth
from app_API.routes import task

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth")

app.include_router(task.router, prefix="/task", tags=["task"])




