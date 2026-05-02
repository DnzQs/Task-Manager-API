from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app_API.db import get_db
from app_API.models import User, Task
from app_API.schemas import Taskcreate
from app_API.auth_utils import get_current_user
from project1.project_genius.schemas import TaskCreate

router = APIRouter()


@router.post("/")
def create_task(
        task: TaskCreate,
        db: Session = Depends(get_db),
        user_email: str = Depends(get_current_user),
):
    user = db.query(User).filter(User.email == user_email).first()

    new_task = Task(
        tittle=task.title,
        description=task.description,
        user_id=user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get("/")
def get_tasks(
    db: Session = Depends(get_db),
    user_email: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return Task.query.filter(Task.user_id == user.id).all()

