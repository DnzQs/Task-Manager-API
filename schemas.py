from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class Taskcreate(BaseModel):
    title: str
    description: str | None=None
