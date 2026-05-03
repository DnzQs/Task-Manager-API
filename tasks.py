from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app_API.schemas import TaskResponse
from app_API.db import get_db
from app_API.models import User, Task
from app_API.schemas import TaskCreate
from app_API.auth_utils import get_current_user

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


@router.get("/", response_model=List[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    user_email: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return Task.query.filter(Task.user_id == user.id).all()


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
        task_id: int,
        task: TaskCreate,
        db: Session = Depends(get_db),
        user_email: str = Depends(get_current_user),
):
    user = db.query(User).filter(User.email == user_email).first()

    db_task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user.id
    ).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task.title
    db_task.description = task.description

    db.commit()
    db.refresh(db_task)

    return db_task


@router.delete("/{task_id}")
def delete_task(
        task_id: int,
        db: Session = Depends(get_db),
        user_email: str = Depends(get_current_user),
):
    user = db.query(User).filter(User.email == user_email).first()

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user.id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task successfully deleted"}



