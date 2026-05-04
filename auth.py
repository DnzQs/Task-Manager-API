from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth_utils import get_current_user
from app.db import get_db
from app.models import User
from app.schemas import UserCreate
from app.utils import hash_password, create_access_token
from test1.auth import verify_password

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created"}


@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="Incorrect email or password")

    if not verify_password(password, user.hashed_password):
        return {"message": "Incorrect credentials"}

    token = create_access_token({"sub": user.email})

    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return {"email": user}