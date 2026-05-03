from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreate(BaseModel):
    pass


class TaskResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True

